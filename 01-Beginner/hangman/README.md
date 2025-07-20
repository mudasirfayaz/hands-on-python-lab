# Hangman Game

> A simple command-line implementation of the classic Hangman game in Python.

<br/>

## 🚀 Features

- Random word selection from a predefined list
- Visual hangman stages that update with incorrect guesses
- Hint system that shows 3 random letters from the chosen word
- Life counter (6 incorrect guesses allowed)
- Win/lose messages with ASCII art
- Input validation (prevents duplicate guesses)

<br/>

## 🛠️ Prerequisites

- Python 3.8+
- Built-in modules:
  - `random` — for number generation

<br/>

## 💻 How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/python-learning-projects.git
cd python-learning-projects/01-Beginner/hangman
```

**2. Run the script:**

```bash
python hangman.py
```

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

**3. You'll see the Hangman logo and a hint showing 3 random letters from the word.**

**4. Guess letters one at a time by typing them and pressing Enter.**

**5. Correct guesses will reveal the letter's position(s) in the word.**

**6. Incorrect guesses will:**

- Deduct one life
- Show the updated hangman stage
- Display the incorrect letter

**7. The game ends when:**

- You guess all letters correctly (win)
- You run out of lives (lose)

<br/>

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change or improve.

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_
