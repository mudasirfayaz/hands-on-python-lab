# 🧠 Quiz Game

> A simple terminal-based quiz app built using Python and Object-Oriented Programming (OOP). The application reads True/False questions from a data source and quizzes the user interactively, tracking the score and validating inputs.

<br/>

## 🎯 Project Objective

- Reinforce Python OOP principles through a real-world-style mini-project
- Practice encapsulation, class design, and method delegation
- Learn basic input validation and quiz scoring logic

<br/>

## Features

- Presents a series of True/False questions
- Validates user input (rejects anything other than "True" or "False")
- Tracks and displays score in real-time
- Modular class-based design using clean separation of responsibilities
- Extendable for future enhancements (e.g., GUI, file-based questions, multiple users)

<br/>

## 🧠 Concepts Reinforced in This Project

| Concept                    | Demonstrated In                                             |
| :------------------------- | :---------------------------------------------------------- |
| Classes & Objects          | `Question`, `QuizBrain`                                     |
| Encapsulation              | Attributes like `question_list`, `score`, `question_number` |
| Input Validation           | `invalid_answer()` method filters invalid entries           |
| List & Dictionary Handling | Used in data parsing (`question_data`)                      |
| Looping & Conditionals     | `while` loop to run the quiz logic                          |
| Responsibility Delegation  | Each class handles a single concern                         |

<br/>

## 🛠️ Prerequisites

- Python 3.6 or higher
- No external libraries required

<br/>

## 💻 How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/python-learning-projects.git
cd python-learning-projects/02-Intermediate/quiz-game
```

**2. Run the script:**

```bash
python main.py
```

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

## 🧪 Example Output

```bash
Q.1: Linux was first created as an alternative to Windows XP. (True/False): false
Wright answer ✅

Q.2: A Mac is not a PC (True/False): true
Wrong answer ❌

...

You've completed the quiz
Your final score is: 8/10
```

<br/>

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change or improve.

<br/>

### 🧪 Future Improvements (Suggestions)

- Add support for loading questions from an external file (CSV/JSON/API)
- Difficulty levels: Easy/Medium/Hard
- Different categories: Computers/Mathematics/Geography
- GUI version using Tkinter or PyQt
- Display final percentage score and answer summary
- Timer or countdown mode

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
