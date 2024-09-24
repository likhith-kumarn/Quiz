class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer_index):
        # Convert the user's numerical choice to the corresponding answer
        return self.choices[user_answer_index - 1].lower() == self.answer.lower()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_next_question(self):
        current_question = self.questions[self.question_index]
        self.question_index += 1
        return current_question

    def display_question(self, question):
        print(question.text)
        for idx, choice in enumerate(question.choices, start=1):
            print(f"{idx}. {choice}")

    def display_score(self):
        total_questions = len(self.questions)
        print(f"Your score: {self.score}/{total_questions}")
        if self.score == total_questions:
            print("Outstanding!")
        elif self.score == 0:
            print("You lost, better luck next time.")

    def play(self):
        for question in self.questions:
            self.display_question(question)
            try:
                user_answer = int(input("Enter your choice (1, 2, 3, or 4): "))
                if question.check_answer(user_answer):
                    print("Correct!")
                    self.score += 1
                else:
                    print("Incorrect.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 4.")
            print()
        self.display_score()

# Sample questions
q1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris")
q2 = Question("Who wrote 'Romeo and Juliet'?", ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"], "William Shakespeare")
q3 = Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Saturn"], "Jupiter")

questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.play()
