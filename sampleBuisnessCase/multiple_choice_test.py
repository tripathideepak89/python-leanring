from Question import Question

prompt = [
    "What color are apples? \n(a) Red/Green \n(b) Orange \n(c) Blue\n",
    "What color are bananas? \n(a) Orange \n(b) Yellow \n(c) Magenta\n",
    "What color are strawberries? \n(a) White \n(b) Blue \n(c) Red\n"
]

questions = [
    Question(prompt[0], "a"),
    Question(prompt[1], "b"),
    Question(prompt[2], "c")
]


def run_tests(queries):
    score = 0
    for question in queries:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("Your score is " + str(score) + "/" + str(len(queries)))


run_tests(questions)
