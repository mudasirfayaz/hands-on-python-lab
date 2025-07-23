# ☕ Object-Oriented Coffee Machine

> A Python CLI-based simulation of a [coffee vending machine](/02-Intermediate/coffee-machine/), re-architected using **object-oriented programming (OOP)** principles. This project models real-world interactions including coin-based payments, resource availability, and menu-driven drink selection — all wrapped in a clean, modular class structure.

<br/>

## 🎯 Project Objectives

- Practice OOP fundamentals (`classes`, `objects`, `encapsulation`, `responsibility delegation`)
- Structure a real-world system into reusable components
- Simulate coin transactions, resource tracking, and inventory checks
- Explore modular design and unit testing in Python

<br/>

## Features

- ☕ Drink options: Espresso, Latte, Cappuccino
- 💰 Coin-based payment system with change calculation
- 📊 Reports for current inventory and profit
- ❌ Resource availability checks with user feedback
- ✅ Modular design split across multiple Python classes
- 🧪 Ready for unit testing (testable, isolated logic)

<br/>

## 🛠️ Prerequisites

- Python 3.6 or higher
- No external libraries required

<br/>

## 💻 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mudasirfayaz/python-learning-projects.git
   cd python-learning-projects/02-Intermediate/coffee-machine-oop
   ```

2. **Run the script:**

   ```bash
   python main.py
   ```

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

📝 Commands

- `espresso`, `latte`, `cappuccino` — Order a drink

- `report` — Print current resources and money

- `off` — Shut down the machine

<br/>

## 🧪 Example Output

```bash
What would you like? (espresso/latte/cappuccino): latte
Please insert coins
How many quarters: 10
How many dimes: 0
How many nickles: 0
How many pennies: 0
Here is $0.0 in change.
Here is your latte ☕ Enjoy!
```

<br/>

## 💡 Concepts Reinforced in This Project

### 🧠 Object-Oriented Programming

- class/object creation
- Constructor methods (**init**)
- Class attributes vs instance attributes
- Data encapsulation
- Responsibility delegation

### 🧱 Software Design Principles

- Single Responsibility Principle (SRP)
- Modular structure for better testing and readability
- Separation of concerns (UI vs logic vs data)

### 🔁 Programming Logic

- Dictionary manipulation
- Loops & conditionals
- Input/output interaction
- Type conversion & rounding
- Defensive programming (handling bad input/invalid states)

<br/>

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change or improve.

<br/>

### 🧪 Future Improvements (Suggestions)

- Refill resources functionality
- Persistent profit tracking (via file/JSON)
- Multi-user mode with login
- GUI version using Tkinter or PyQT
- Custom drink creation by users

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
