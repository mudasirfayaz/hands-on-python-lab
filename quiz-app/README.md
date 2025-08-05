# Quiz App 🧠

> A simple terminal-based quiz app built using Python and Object-Oriented Programming (OOP). The application reads Multiple Choice Questions from a data source and quizzes the user interactively, tracking the score and validating inputs.

<br/>

## 🎯 Project Objective

- Reinforce Python OOP principles through a real-world-style mini-project
- Practice encapsulation, class design, and method delegation
- Learn basic input validation and quiz scoring logic

<br/>

## Features

- Presents a series of Multiple Choice Questions (MCQs)
- Validates user input (rejects anything other than A, B, C or D)
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
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/quiz-app
```

**2. Run the script:**

```bash
python main.py
```

<br/>

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

## 🧪 Example Output

```bash
Q.1: What programming language was GitHub written in?
A. Swift
B. Kotlin
C. JavaScript
D. C#
Your answer (A/B/C/D): a
Wrong answer!. (The correct answer is Kotlin)

...

You've completed the quiz
Your final score is: 8/10
```

<br/>

## 🤝 Contributing

Contributions are welcome and encouraged — whether you're fixing a typo, improving documentation, or adding a new mini-project to the lab!

<br/>

> [!IMPORTANT]
> Before you begin, please read our [**Contributing Guidelines**](/CONTRIBUTING.md).

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

<br/>

![Star](/assets/docs/star.png)
