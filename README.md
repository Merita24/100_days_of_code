# 🐍 Python Iterators & Generators Practice

This repository contains beginner-friendly Python exercises that explore the concepts of **iterators** and **generators**. These exercises were designed to solidify core Python fundamentals and build confidence working with custom iteration logic.

---

## 🧠 Exercises Covered

### ✅ 1. Countdown Iterator
A custom class-based iterator that counts down from a given number to 0.

```python
for num in Countdown(5):
    print(num)
# Output: 5 4 3 2 1 0
✅ 2. Even Numbers Generator
A generator function that yields all even numbers up to a given number n.

python
Copy
Edit
for num in generate_evens(10):
    print(num)
# Output: 0 2 4 6 8 10
✅ 3. Reverse List Iterator
An iterator that yields items of a list in reverse order.

python
Copy
Edit
for item in ReverseList(['a', 'b', 'c']):
    print(item)
# Output: c b a
✅ 4. Skip Iterator
An iterator that skips every second element from a list (yields index 0, 2, 4...).

python
Copy
Edit
for item in SkipIterator([1, 2, 3, 4, 5, 6]):
    print(item)
# Output: 1 3 5
✅ 5. Fibonacci Generator
A generator that yields the first n numbers of the Fibonacci sequence.

python
Copy
Edit
for num in fibonacci(7):
    print(num)
# Output: 0 1 1 2 3 5 8
