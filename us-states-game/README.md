# U.S. States Game 🗺️

> An interactive Python-based educational game where players guess all 50 U.S. states. Built with Turtle graphics and Pandas for data handling, this project combines fun gameplay with a touch of data-driven logic.

<br/>

## Game Objective 🎯

The goal is simple: Guess all 50 U.S. states by typing their names. Correct guesses are displayed on the U.S. map, while missed states are revealed in red when you exit the game.

<br/>

## Preview 🖼️

![Preview](blank_states_img.gif)

<br/>

## Features ⚙️

- Interactive Gameplay – Guess states via a text prompt.
- Data Integration – Reads coordinates from `50_states.csv`.
- Dynamic Map Updates – Correct states appear in black, missed states in red.
- Replay Value – Learn and improve geography knowledge through repeated play.
- Missed States CSV – Saves all unguessed states to `states_to_learn.csv` for future practice.

<br/>

## 📦 Installation & Setup

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/us-states-game
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

# 📝 How to Play

1. Run the game — a blank U.S. map will appear.
2. Enter the name of a U.S. state when prompted.
3. Correct guesses will appear on the map.
4. Type Exit to end the game early:

- Missed states will be shown in red.
- A file `states_to_learn.csv` will be created with the names of those states for practice.

<br/>

## 🛠️ Technologies Used

- Python (Core programming language)
- Turtle (Graphics and map rendering)
- Pandas (CSV reading, writing, and data handling)

<br/>

## 📂 Project Structure

```bash
us-states-game/
│
├── main.py                # Game logic
├── 50_states.csv          # State names with coordinates
├── blank_states_img.gif   # U.S. map outline
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── states_to_learn.csv    # (Generated) States you missed in your last game
```

## 🤝 Contributing

Contributions are welcome and encouraged — whether you're fixing a typo, improving documentation, or adding a new mini-project to the lab!

<br/>

> [!IMPORTANT]
> Before you begin, please read our [**Contributing Guidelines**](/CONTRIBUTING.md).

<br/>

### 🚀 Future Enhancements

- Add a timer mode for extra challenge.
- Track and display high scores.
- Include hints for difficult states.

<br/>

## 🧑‍💻 Author

**[Mudasir Fayaz](https://github.com/mudasirfayaz/)** - Student | Tech Enthusiast | Lifelong Learner<br/>
_Building fun and useful Python tools_

<br/>

# 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

<br/>

![Star](/assets/docs/star.png)
