# Turtle Crossing Game 🐢

> A Python `turtle` graphics game where you control a turtle crossing a busy road filled with moving cars.Reach the finish line to level up, but avoid collisions or it’s game over!

<br/>

## 🎮 How to Play

- Press **Up Arrow** to move your turtle forward.
- Cross the road without getting hit by a car.
- Each successful crossing:
  - Increases your level.
  - Increases the car speed (making it harder).
- The game ends if a car hits your turtle.

<br/>

## 📂 Project Structure

```bash
turtle-crossing/
│
├── main.py # Game loop and collision logic
├── player.py # Player (turtle) movement and reset logic
├── car_manager.py # Car creation, movement, and speed control
└── scoreboard.py # Level tracking and game over display
```

<br/>

## 🧠 Concepts Practiced

This project strengthens your understanding of:

- **Object-Oriented Programming**:
  Encapsulation using `Player`, `CarManager`, and `Scoreboard` classes.
- **Event-driven programming**:
  Listening for keyboard input (`screen.onkey`).
- **Game loop mechanics**:
  Updating screen frames, time delay, and object movement.
- **Collision detection**:
  Using `distance()` method for turtle-to-car collision checks.
- **Incremental difficulty**:
  Increasing speed as the game progresses.

<br/>

## 🛠️ Prerequisites

- Python 3.8+
- Built-in modules:
  - `turtle` — to create drawings and animations
  - `random` — for number generation

<br/>

## 💻 How to Run

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/turtle-crossing
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

- Add multiple movement controls (Left/Right)
- Randomize car spawn rate dynamically
- High score tracking
- Sound effects

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

<br/>

![Star](/assets/docs/star.png)
