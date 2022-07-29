class Question:
    def __init__(self, text, choice, answer):
        self.text = text
        self.choice = choice
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')
        for q in question.choice:
            print('-', q)
        answer = str(input('Your answer: '))
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
            self.displayProgress()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Your Score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print('Quiz is finished!')
        else:
            print(f' Question {questionNumber} of {totalQuestion} '.center(100, '*'))


q1 = Question('Which is the best programming language?', ['Python', 'C#', 'Java', 'JavaScript'], 'Python')
q2 = Question('What is the most popular programming language?', ['Java', 'JavaScript', 'Python', 'C#'],
              'JavaScript')
q3 = Question('Which programming language is the most profitable?', ['Python', 'C#', 'Java', 'JavaScript'], 'Java')
q4 = Question('Which is the easiest programming language?', ['Java', 'JavaScript', 'Python', 'C#'], 'Python')
q5 = Question('What is the most used programming language?', ['Python', 'C#', 'Java', 'JavaScript'], 'JavaScript')
questions = [q1, q2, q3, q4, q5]

quiz = Quiz(questions)
quiz.loadQuestion()
