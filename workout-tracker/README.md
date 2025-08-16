# Workout Tracker

> A Python project that uses the **Nutritionix API** and **Sheety API** to track workouts, calculate calories burned, and log the results into a Google Sheet.

<br/>

## Features

- Parse natural language workout input (e.g., _"Ran 2 miles and did 30 push-ups"_).
- Fetch exercise details (duration & calories) from **Nutritionix**.
- Log workouts into Google Sheets via **Sheety** API.
- Securely manage API keys using `.env`.

<br/>

## 🧠 Concepts Reinforced

This project reinforces several core programming and software development concepts:

| Concept                       | Key Takeaways                                                           |
| ----------------------------- | ----------------------------------------------------------------------- |
| **Working with APIs**         | Sending `POST` requests with headers & body; parsing JSON responses.    |
| **Authentication & Security** | Using API keys, App IDs, Bearer Tokens; managing secrets in `.env`.     |
| **Date & Time Handling**      | Using `datetime` to log workout date and time.                          |
| **Code Modularity**           | Splitting logic into functions for readability and maintainability.     |
| **Error Handling**            | Handling failed API requests gracefully with `try/except`.              |
| **Real-world Integration**    | Connecting Python with external services (Nutritionix + Google Sheets). |

<br/>

## 🛠️ Prerequisites

- Python 3.6 or higher
- Nutritionix API (for exercise parsing)
- Sheety API (for Google Sheets logging)
- Internet connection (for API calls)
- Libraries:
  ```bash
  pip install -r requirements.txt
  ```

<br/>

## 🚀 Getting Started

**1. Clone the repository:**

```bash
git clone https://github.com/mudasirfayaz/hands-on-python-lab.git
cd hands-on-python-lab/workout-tracker
```

<br/>

**2. Install Dependencies**

```bash
pip install -r requirements.txt
```

<br/>

**3. Setup Environment Variables**

Create a `.env` file inside the project folder with the following structure:

```bash
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
BEARER_TOKEN=your_sheety_bearer_token
SHEET_ENDPOINT=your_sheety_endpoint
```

> [!WARNING]
> Never push your `.env` file to GitHub. Keep it private.

<br/>

**4. Getting API Credentials**

Nutritionix API (for exercise parsing)

1. Go to [Nutritionix Developer Portal](https://developer.nutritionix.com).
2. Create a free account and log in.
3. Create a new app → you’ll get an `APP_ID` and an `API_KEY`.
4. Copy them into your `.env` file.

<br/>

Sheety API (for Google Sheets logging)

1. Go to [Sheety](https://sheety.co).
2. Sign in with your Google account.
3. Create a new project and connect it to your Google Sheet.
   - For example, create a Google Sheet with columns: `Date`, `Time`, `Exercise`, `Duration`, `Calories`.
4. Sheety will provide you with:
   - An endpoint URL (`SHEET_ENDPOINT`).
   - A Bearer Token (`BEARER_TOKEN`) if you enable authentication.
5. Add these to your `.env` file.

<br/>

**5. Run the script:**

```bash
python main.py
```

<br/>

When prompted, enter your workout in plain English, for example:

```bash
Tell me which exercises you did: Ran 3 km and cycled 20 minutes
```

<br/>

The script will:

- Send the query to Nutritionix.
- Receive structured exercise data (duration + calories).
- Log each workout entry into your Google Sheet via Sheety.

<br/>

> [!WARNING]
> Make sure you have Python 3 installed and accessible from your terminal or command prompt.

<br/>

## ✅ Example Google Sheet Output

| Date       | Time     | Exercise | Duration (min) | Calories |
| ---------- | -------- | -------- | -------------- | -------- |
| 16/08/2025 | 07:30:15 | Running  | 30             | 300      |
| 16/08/2025 | 07:30:15 | Cycling  | 20             | 200      |

<br/>

## 📌 Notes

- Make sure your Google Sheet columns match the JSON keys (`date`, `time`, `exercise`, `duration`, `calories`).
- Nutritionix works best with plain English input (e.g., “jogged 3 miles” instead of “3mi jog”).

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
