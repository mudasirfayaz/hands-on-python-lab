from question_model import Question
from quiz_brain import QuizBrain
import random
import requests

# Available settings
difficulties = ["easy", "medium", "hard"]
topics = {
    "general": 9,
    "books": 10,
    "film": 11,
    "music": 12,
    "science": 17,
    "computers": 18,
    "sports": 21,
}


def fetch_questions(amount, difficulty, category):
    parameters = {
        "amount": amount,
        "difficulty": difficulty,
        "type": "multiple",
        "category": category,
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response.json()["results"]


while True:
    # Show available settings
    print(" ")
    print("Available difficulties:", ", ".join(difficulties))
    print("Available topics:", ", ".join(topics.keys()))
    print(" ")

    # Get user input
    difficulty = input("Choose difficulty: ").strip().lower()
    topic = input("Choose topic: ").strip().lower()

    # Validate input
    if difficulty not in difficulties or topic not in topics:
        print("\n❌ Invalid choice. Please try again.\n")
        continue

    # Fetch and prepare questions
    question_data = fetch_questions(10, difficulty, topics[topic])
    question_bank = []

    print(" ")
    for question in question_data:
        q_text = question["question"]
        q_answer = question["correct_answer"]
        q_options = question["incorrect_answers"]
        q_options.insert(random.randint(0, 3), q_answer)
        new_question = Question(q_text, q_answer, q_options)
        question_bank.append(new_question)

    # Run quiz
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score is: {quiz.score}/{len(question_bank)}")
    print(" ")

    # Replay option
    if input("Do you want to take another quiz? (Y/N): ").strip().lower() == "n":
        break
