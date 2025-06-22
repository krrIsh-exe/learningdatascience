# 🧮 Day 1 - NumPy Basics

This is the first project in my **AI/ML 6-month journey**.  
In this project, I practiced fundamental NumPy operations — the foundation of data handling in machine learning.

---

## 📌 Topics Covered

- NumPy Arrays: Creation & Reshaping
- Array Indexing & Slicing
- Mathematical Operations on Arrays
- Finding Mean, Max, and other statistics
- Matrix Reshaping and Broadcasting

---

## 📁 Files

- `day1_numpy_basics.py`: Contains all NumPy practice code
- `README.md`: You're reading it 🙂

---

## 🧠 Sample Code

```python
import numpy as np

a = np.arange(1, 11)
b = a.reshape(2, 5)
row_mean = np.mean(b, axis=1)
c = b * 2

print("Original:", a)
print("Reshaped:\n", b)
print("Mean of Rows:", row_mean)
print("Doubled:\n", c)
