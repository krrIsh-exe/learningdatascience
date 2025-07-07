# AI Motion Detection + Smart Alert System
# By ChatGPT for Krish

import cv2
import smtplib
import time
import os
from email.message import EmailMessage

# ----- CONFIG -----
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password_or_app_password'
SEND_TO = 'receiver_email@gmail.com'
CAPTURE_DIR = 'captures/'
MOTION_THRESHOLD = 1500  # sensitivity

# ----- SETUP -----
os.makedirs(CAPTURE_DIR, exist_ok=True)
cap = cv2.VideoCapture(0)
_, frame1 = cap.read()
_, frame2 = cap.read()

# ----- EMAIL FUNCTION -----
def send_email_alert(image_path):
    msg = EmailMessage()
    msg['Subject'] = '🚨 Motion Detected Alert!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = SEND_TO
    msg.set_content('Motion detected. See the attached image.')

    with open(image_path, 'rb') as img:
        msg.add_attachment(img.read(), maintype='image', subtype='jpeg', filename=os.path.basename(image_path))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("✅ Alert email sent!")

# ----- MAIN LOOP -----
motion_sent = False
last_sent_time = 0
COOLDOWN = 30  # seconds

print("📹 Motion detector running. Press 'q' to quit.")

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < MOTION_THRESHOLD:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        current_time = time.time()
        if not motion_sent or (current_time - last_sent_time) > COOLDOWN:
            filename = f"{CAPTURE_DIR}motion_{int(current_time)}.jpg"
            cv2.imwrite(filename, frame1)
            send_email_alert(filename)
            motion_sent = True
            last_sent_time = current_time

    cv2.imshow("Motion Detection", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if not ret:
        break

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
