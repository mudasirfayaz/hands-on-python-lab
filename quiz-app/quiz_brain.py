import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Display question and choices
        q_text = html.unescape(current_question.text)
        print(f"Q.{self.question_number}: {q_text}")
        option_letters = ["A", "B", "C", "D"]
        self.option_map = {}

        for i, option in enumerate(current_question.options):
            print(f"{option_letters[i]}. {html.unescape(option)}")
            self.option_map[option_letters[i]] = option

        while True:
            user_input = input("Your answer (A/B/C/D): ").strip().upper()
            if user_input in self.option_map:
                selected_option = self.option_map[user_input]
                self.check_answer(selected_option, current_question.answer)
                break
            else:
                print("Invalid input. Please select A, B, C, or D.")

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅ Correct answer")
        else:
            for key, value in self.option_map.items():
                if value == correct_answer:
                    print(f"❌ Wrong answer! The correct option is: {key}. '{value}'.")
                    break
        print(" ")
