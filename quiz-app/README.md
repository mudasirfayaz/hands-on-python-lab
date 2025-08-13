# Quiz App 🧠

> A command-line multiple-choice quiz game built in Python using the [Open Trivia Database API](https://opentdb.com/).  
> The game lets you choose **difficulty** and **topic** before starting, then presents 10 randomized MCQs.  
> Your score is tracked and displayed at the end of each round.

<br/>

## Features

- **Dynamic Questions** – Fetched live from Open Trivia DB API.
- **Custom Difficulty** – Choose from `easy`, `medium`, or `hard`.
- **Topic Selection** – Choose from multiple categories like _science_, _sports_, _computers_, and more.
- **Multiple Choice Questions** – Four randomized options per question.
- **Score Tracking** – Final score displayed at the end.
- **Replay Option** – Play as many rounds as you want without restarting.

<br/>

## 🧠 Concepts Reinforced

This project improves understanding of:

| Concept                         | Demonstrated In                                                     |
| :------------------------------ | :------------------------------------------------------------------ |
| **Object-Oriented Programming** | Classes for `Question` and `QuizBrain`.                             |
| **API Integration**             | Fetching JSON data with query parameters.                           |
| **Data Handling**               | Shuffling and inserting the correct answer among incorrect answers. |
| **Input Validation**            | Handling invalid difficulty/topic entries gracefully.               |
| **Game Loop Logic**             | Replay functionality and score tracking.                            |

<br/>

## 🛠️ Prerequisites

- Python 3.6 or higher
- Internet connection (for API calls)

<br/>

## 💻 How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/quiz-app
```

**2. Install Dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the script:**

```bash
python main.py
```

<br/>

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

## 🧪 Example Output

```bash
Available difficulties: easy, medium, hard
Available topics: general, books, film, music, science, computers, sports

Choose difficulty: easy
Choose topic: computers

Q.1: According to the International System of Units, how many bytes are in a kilobyte of RAM?
A. 512
B. 1024
C. 1000
D. 500
Your answer (A/B/C/D): b
❌ Wrong answer! The correct option is: C. '1000'.

...

You've completed the quiz
Your final score is: 8/10
```

<br/>

## 📜 Available Choices

| Difficulty         | Topics                                                  |
| ------------------ | ------------------------------------------------------- |
| easy, medium, hard | general, books, film, music, science, computers, sports |

> **Tip:** Enter your choice in lowercase when prompted in the game.

<br/>

## 🤝 Contributing

Contributions are welcome and encouraged — whether you're fixing a typo, improving documentation, or adding a new mini-project to the lab!

<br/>

> [!IMPORTANT]
> Before you begin, please read our [**Contributing Guidelines**](/CONTRIBUTING.md).

<br/>

### 🧪 Future Improvements (Suggestions)

- Add timed mode for answering questions.
- Save high scores locally.
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
