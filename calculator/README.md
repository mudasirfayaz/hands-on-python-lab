# Command-Line Calculator 🧮

> A clean, interactive, and beginner-friendly command-line calculator built in Python. This utility supports basic arithmetic operations (`+`, `-`, `*`, `/`) with intuitive flow control for continuous calculations, restarts, and safe exits.

<br/>

## 🚀 Features

- ✅ Handles addition, subtraction, multiplication, and division
- ✅ Graceful handling of invalid inputs (non-numeric, divide-by-zero, invalid operator)
- ✅ Option to:
  - Continue calculating with the previous result
  - Start a new calculation
  - Exit the application
- ✅ Rounded result output for clean readability
- ✅ Auto-removes unnecessary `.0` for whole number inputs (e.g., `5.0 → 5`)
- ✅ Uses Python’s `operator` module for clean, maintainable logic

<br/>

## 🛠️ Prerequisites

- Python 3.8+
- Standard Libraries:
  - `operator` — for mapping arithmetic operators to functions

<br/>

## 💻 How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/calculator
```

**2. Run the script:**

```bash
python calculator.py
```

<br/>

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

## 🧠 Sample Output

```bash
Enter first no: 12
Enter operation (+ - * /): *
Enter second no: 4

12 * 4 = 48.0

Type 'c' to continue calculating with 48.0.
Type 's' to start a new calculation.
Type 'q' to quit: c

Enter operation (+ - * /): -
Enter second no: 8

48.0 - 8 = 40.0
```

<br/>

## 📈 Future Enhancements (Optional Ideas)

- Support for advanced operators: \*\*, //, %
- GUI version using Tkinter
- Command-line argument support (via argparse)
- Export calculation history to a .txt file

<br/>

## 🤝 Contributing

Contributions are welcome and encouraged — whether you're fixing a typo, improving documentation, or adding a new mini-project to the lab!

<br/>

> [!IMPORTANT]
> Before you begin, please read our [**Contributing Guidelines**](/CONTRIBUTING.md).

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

<br/>

![Star](/assets/docs/star.png)
