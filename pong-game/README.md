# Pong Game 🏓

> A modern, refactored implementation of the classic **Pong** game using Python's `turtle` graphics library. Smooth paddle controls, clean modular code, and an easy-to-read structure make this ideal for learning and extending.

<br/>

## ✨ Features

- **Two-player mode** with smooth paddle movement on key hold.
- **Dynamic ball speed** — increases after each paddle hit.
- **Score tracking** with on-screen display.
- **Clean architecture** split across:
  - `main.py` — game loop & event handling
  - `paddle.py` — paddle movement logic
  - `ball.py` — ball movement & collision handling
  - `scoreboard.py` — score tracking & rendering
  - `constants.py` — all configurable constants

<br/>

## 🖥 Controls

| Player       | Move Up   | Move Down |
| ------------ | --------- | --------- |
| Left Paddle  | `W`       | `S`       |
| Right Paddle | `↑` Arrow | `↓` Arrow |

<br/>

## 🧠 Concepts Practiced

This project solidifies core Python and OOP concepts:

- Classes, methods, and encapsulation
- `turtle` graphics and animation loops
- Keyboard event handling
- Collision detection (`distance()`)
- Clean modular architecture

<br/>

## 🛠️ Prerequisites

- Python **3.8+**
- No external dependencies — uses Python's built-in `turtle` module.

<br/>

## 💻 How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/pong-game
```

**2. Run the script:**

```bash
python main.py
```

<br/>

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

## 🤝 Contributing

Contributions are welcome and encouraged — whether you're fixing a typo, improving documentation, or adding a new mini-project to the lab!

<br/>

> [!IMPORTANT]
> Before you begin, please read our [**Contributing Guidelines**](/CONTRIBUTING.md).

<br/>

### 🧪 Future Improvements (Suggestions)

- Add sound effects for paddle hits and scoring
- Implement single-player mode with AI opponent
- Add pause/resume and restart functionality
- Introduce score limit & match-winning conditions
- Add game start menu and custom themes

<br/>

## ⚙ Configuration

Edit `constants.py` to change:

- Screen size
- Paddle boundaries
- Ball speed increment factor
- Starting ball position

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

<br/>

![Star](/assets/docs/star.png)
