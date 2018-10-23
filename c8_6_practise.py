import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento'}
states = list(capitals.keys())
print('capital.values() is : ', capitals.values())
#print(capitals.keys())
print('states is : ', states)
for questionNum in range(0, 2):
    correctAnswer = capitals[states[questionNum]]
    print('correctAnswer is : ', correctAnswer)
    wrongAnswers = list(capitals.values())
    #print('wrongAnswers are : ', wrongAnswers)
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    #print('wrongAnswers are : ', wrongAnswers)
    wrongAnswers = random.sample(wrongAnswers, 3)
    #print('wrongAnswers are : ', wrongAnswers)
    answerOptions = wrongAnswers + [correctAnswer]
    #print('answerOptions are : ', answerOptions)
    random.shuffle(answerOptions)
    print('answerOptions are : ', answerOptions)
