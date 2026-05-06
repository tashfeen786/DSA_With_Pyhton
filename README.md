# 🧩 DSA With Python

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat&logo=jupyter)
![Problems](https://img.shields.io/badge/Problems-30+-brightgreen?style=flat)
![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-yellow?style=flat)
![Stars](https://img.shields.io/badge/Stars-2⭐-gold?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> 📚 A structured collection of **Data Structures & Algorithms** problems
> solved in Python — covering arrays, recursion, sorting algorithms,
> searching, hashing, and LeetCode problems with clean implementations.

---

## 📋 Problems Index

### 🔢 Arrays
| Problem | File |
|---------|------|
| Find Largest Element in Array | `Find the Largest Element in an Array.ipynb` |
| Find Second Largest (Without Sorting) | `Find the Second Largest Element in an Array Without Sorting.ipynb` |
| Check if Array is Sorted | `Check if an Array is Sorted.ipynb` |
| Remove Duplicates from Sorted Array | `Remove Duplicates from a Sorted Array.ipynb` |
| Right Rotate Array by One Place | `Right Rotate an Array by One Place.ipynb` |
| Move Zeros to End (LeetCode #283) | `Leetcode 283 Move Zeros to the End of theList.ipynb` |

### 🔄 Sorting Algorithms
| Algorithm | Time Complexity | File |
|-----------|----------------|------|
| Bubble Sort | O(n²) | `Bubble sort.ipynb` |
| Selection Sort | O(n²) | `Selection Sort in Python.ipynb` |
| Insertion Sort | O(n²) | `insertion sort.ipynb` |
| Merge Sort | O(n log n) | `Merge Sort.ipynb` |
| Quick Sort | O(n log n) avg | `QuickSort.ipynb` |

### 🔍 Searching
| Problem | File |
|---------|------|
| Linear Search | `Implementing Linear Search.ipynb` |

### 🔁 Recursion & Backtracking
| Problem | File |
|---------|------|
| Basic Recursion | `Recursion.py` |
| Recursion with Parameters | `Recursion using Parameter.py` |
| Print 1 to N (Recursion) | `print 1 to N using Recursion.py` |
| Print 1 to N (Backtracking) | `print 1 to N using BackTracking.py` |
| Sum 1 to N (Functional Recursion) | `1 to N sum using funcational recursion.py` |
| Sum 1 to N (Parameterized) | `sum of 1 to N using Parameterized.py` |
| Factorial using Recursion | `Factorial using recursion.py` |
| Reverse Array using Recursion | `Reverse an Array Using Recursion.py` |

### 🔣 Strings
| Problem | File |
|---------|------|
| Check Palindrome | `Check_palindrome.py` |
| Check String Palindrome | `Check if a String is Palindrome or Not.ipynb` |

### 🗂️ Hashing & Data Structures
| Problem | File |
|---------|------|
| Hashing in Python | `Hashing_in_Python.py` |
| Store Frequency in Dictionary | `Store_frequencyIn_Dictionary.py` |

### 🔢 Number Theory
| Problem | File |
|---------|------|
| Count Digits in Integer | `Count the number of digits in interger.py` |
| Check Armstrong Number | `Check_Armstrong_Number.py` |
| Print Factors of Number | `Print_Factors_Given_Number.py` |
| Find Fibonacci Number | `Find the Fibonacci Number.ipynb` |

---

## 💡 Key Concepts Demonstrated

### Recursion Types
```python
# 1. Functional Recursion — returns value
def sum_n(n):
    if n == 0: return 0
    return n + sum_n(n - 1)

# 2. Parameterized Recursion — passes result in parameter
def sum_n(n, total=0):
    if n == 0: return total
    return sum_n(n - 1, total + n)

# 3. Backtracking — undo and try again
def print_1_to_n(n, i=1):
    if i > n: return
    print(i)
    print_1_to_n(n, i + 1)
```

### Sorting Comparison
```
Algorithm     | Best    | Average | Worst   | Space
--------------|---------|---------|---------|------
Bubble Sort   | O(n)    | O(n²)   | O(n²)   | O(1)
Selection Sort| O(n²)   | O(n²)   | O(n²)   | O(1)
Insertion Sort| O(n)    | O(n²)   | O(n²)   | O(1)
Merge Sort    | O(nlogn)| O(nlogn)| O(nlogn)| O(n)
Quick Sort    | O(nlogn)| O(nlogn)| O(n²)   | O(logn)
```

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/tashfeen786/DSA_With_Pyhton.git
cd DSA_With_Pyhton

# Run any Python file
python Recursion.py
python Bubble_sort.py

# Or open Jupyter notebooks
jupyter notebook
```

---

## 🏗️ Project Structure

```
DSA_With_Pyhton/
│
├── 📁 Arrays/
│   ├── Find the Largest Element in an Array.ipynb
│   ├── Find the Second Largest Element...ipynb
│   ├── Remove Duplicates from a Sorted Array.ipynb
│   └── Right Rotate an Array by One Place.ipynb
│
├── 📁 Sorting/
│   ├── Bubble sort.ipynb
│   ├── Selection Sort in Python.ipynb
│   ├── insertion sort.ipynb
│   ├── Merge Sort.ipynb
│   └── QuickSort.ipynb
│
├── 📁 Recursion/
│   ├── Recursion.py
│   ├── Factorial using recursion.py
│   └── Reverse an Array Using Recursion.py
│
├── 📁 LeetCode/
│   └── Leetcode 283 Move Zeros to the End.ipynb
│
└── README.md
```

---

## 🎯 Why DSA Matters for AI/ML Engineers

- ✅ **Efficient data processing** — sorting/searching large datasets
- ✅ **Algorithm optimization** — O(n) vs O(n²) matters at scale
- ✅ **Technical interviews** — DSA is tested at every AI company
- ✅ **Vector operations** — hashing used in embeddings & RAG systems
- ✅ **Recursion** — backbone of tree traversal in decision trees

---

## 🔮 Coming Soon

- [ ] Binary Search
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees & Graphs
- [ ] Dynamic Programming
- [ ] More LeetCode problems

---

## 👨‍💻 Author

**Tashfeen Aziz** — AI/ML Engineer & Python Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/tashfeen-aziz-b51361292)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/tashfeen786)
[![Email](https://img.shields.io/badge/Email-Contact-red?logo=gmail)](mailto:tashfeen247@gmail.com)

---

⭐ **If you found this helpful, please give it a star!**
