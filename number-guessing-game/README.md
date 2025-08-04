# 🔢 Number Guessing Game (Python CLI)

> A fun, interactive number guessing game built using Python. The game allows users to choose a difficulty level, guess a randomly generated number within a range, and get feedback until they win or exhaust their attempts.

<br/>

## 🎮 Game Features

- 🎯 **Three difficulty levels**:

  - Easy: 1–50 (10 attempts)
  - Medium: 1–75 (6 attempts)
  - Hard: 1–100 (3 attempts)

- 🔁 Replay options:

  - Guess again
  - Change difficulty level
  - Quit the game

- 🧠 Intelligent feedback:
  - "Too High" or "Too Low" hints after each guess
  - 🛡️ Robust input validation for levels and guesses
  - 🎉 Celebratory message on win, loss message on failure

<br/>

## 🛠️ Prerequisites

- Python 3.8+
- Built-in modules:
  - `random` — for number generation

<br/>

## 💻 How to Play

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mudasirfayaz/python-learning-projects.git
   cd python-learning-projects/01-Beginner/number-guessing-game
   ```

2. **Run the script:**

   ```bash
   python game.py
   ```

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

3. **Follow the prompts:**

   - Select a level: easy, medium, or hard

   - Guess the number within the range and remaining attempts

   - Get feedback and keep guessing until you win or lose

<br/>

## 🧪 Example Gameplay

```bash
Select a level (Easy/Medium/Hard): easy

Attempts left = 10

Guess the number between 1 to 50: 30
Too Low

Attempts left = 9

Guess the number between 1 to 50: 40
Too High

...

You won 🎉

Type 'g' to guess again.
Type 'c' to change level.
Type 'q' to quit:
```

<br/>

## 📈 Potential Improvements

- Track and display best score (fewest attempts)

- Add leaderboard or player name input

- Sound effects or visual elements with a GUI (Tkinter or Pygame)

- Unit tests for input handling and logic

<br/>

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change or improve.

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
