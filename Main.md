# 🐍 **REFRESHER ON PYTHON: CODE GUIDE**

---

## 📌 *1. Variables and Data Types**

```python
name = "Alice"        # String
age = 30              # Integer
height = 5.7          # Float
is_student = False    # Boolean
```

> **Tip:** Use `type(variable)` to check the data type.

---

## 📌 **2. Control Flow**

### **`if-elif-else` Block**

```python
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

---

### **Loops**

#### 🔁 `for` loop

```python
for i in range(5):
    print(i)
```

#### 🔁 `while` loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 📌 **3. Functions**

```python
def greet(name):
    return f"Hello, {name}!"
    
print(greet("Alice"))
```

---

## 📌 **4. Lists and Dictionaries**

### *List*

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # Access first element
```

### *Dictionary*

```python
person = {"name": "Alice", "age": 30}
print(person["name"])  # Access value by key
```

---

## 📌 **5. Classes and Objects**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

p = Person("Alice", 30)
p.greet()
```

---

## 📌 **6. File I/O**

```python
# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello, file!")

# Reading from a file
with open("sample.txt", "r") as f:
    print(f.read())
```

---

## 📌 **7. Exception Handling**

```python
try:
    x = int("abc")
except ValueError as e:
    print("Error:", e)
```

---

## 📌 **8. Useful Markdown Cheatsheet Table**

| Feature           | Syntax                     | Example                       |
|-------------------|----------------------------|-------------------------------|
| **Bold**          | `**text**` or `__text__`   | **Bold Text**                |
| *Italic*          | `*text*` or `_text_`       | *Italic Text*                |
| `Inline code`     | `` `code` ``               | `print("Hello")`             |
| Code block        | <code>\`\`\`python</code>  | ```python<br>print("Hi")<br>``` |
| Headers           | `#`, `##`, `###`, etc.     | # H1, ## H2, ### H3           |
| Bullet list       | `-` or `*`                 | - Item 1                      |
| Numbered list     | `1.`                       | 1. Item 1                     |
| Blockquote        | `>`                        | > This is a quote             |

---

> ✅ **Practice these basics daily to become a Python pro!**




```python

```
