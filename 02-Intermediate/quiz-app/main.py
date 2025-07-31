from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

difficulties = ["easy", "medium", "hard"]
while True:
    question_bank = []
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
    if difficulty not in difficulties:
        print("Invalid difficulty. Choose (Easy/Medium/Hard)")
        print(" ")
        continue

    print(" ")
    for question in question_data:
        if difficulty == question["difficulty"]:
            q_text = question["question"]
            q_answer = question["correct_answer"]
            q_options = question["options"]
            new_question = Question(q_text, q_answer, q_options)
            question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score is: {quiz.score}/{len(question_bank)}")
    print(" ")

    play_again = input("Do you want to take another quiz (Y/N): ").lower()
    if play_again == "n":
        break
