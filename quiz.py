from components.quizQuestions import questions
from components import vars, quizTally
import emoji

answer1 = questions["q1"][input(questions["q1"]["question"])]
print(answer1)

vars.quizTotal += answer1
print("/////////////////// Marvel Quiz /////////////////////\n")


answer2 = questions["q2"][input(questions["q2"]["question"])]
print(answer2)

vars.quizTotal += answer2
print("/////////////////// Will it be accurate?/////////////////////\n")

answer3 = questions["q3"][input(questions["q3"]["question"])]
print(answer3)

vars.quizTotal += answer3
print("/////////////////// WE SHALL SEE /////////////////////\n")

answer4 = questions["q4"][input(questions["q4"]["question"])]
print(answer4)

vars.quizTotal += answer4
print("///////////////////VOILA!/////////////////////\n")


print("total so far: " + str(vars.quizTotal) + "\n")
print(emoji.emojize(":sparkles::sparkles::sparkles::sparkles::sparkles::sparkles::sparkles::sparkles::sparkles:"))


quizTally.total(vars.quizTotal)




