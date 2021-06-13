from questionClass import Questions
prompt_questions = [
    "\n qual é a cor da banana? \n a) azul \n b) amarelo \n c) vermelho, \n ",
    "\n qual é a cor do céu? \n a) preto \n b) amarelo \n c) azul \n ",
    "\n qual é a cor do abacate \n a) verde \n b) azul \n c) amarelo \n"
]

questions = [
    Questions(prompt_questions[0], "b"),
    Questions(prompt_questions[1], "c"),
    Questions(prompt_questions[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.pergunta)
        if answer == question.resposta:
            score += 1
    print("Voce arcetou " + str(score) + "/" + str(len(questions)))

run_test(questions)
