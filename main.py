# Variable Declaration
quizzes = [0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
quiz_score = 0
midterms = [0, 0, 0, 0]
midterm_score = 0
final_score = 0
count1 = 0
count2 = 0

# goes through until the user enters a zero and adds all assignment scores to list
for i in range(len(quizzes)):
  print(f'Quiz #{count1+1}:', end = " ")
  score = int(input())
  if score != 1 and score != 2 and score != 3:
    break
  else:
    quizzes[count1] = score
    count1 += 1
# adds all the assignment scores together and then checks if its over 40
for i in range(len(quizzes)):
  quiz_score += quizzes[i]
if(quiz_score > 40):
  quiz_score = 20
else:
  quiz_score /= 2
  
# goes through until the user enters a zero and adds all midterm scores to list
for i in range(len(midterms)):
  print(f'Midterm #{count2+1}:', end = " ")
  score = int(input())
  if score <= 0:
    break
  else:
    midterms[count2] = score
    count2 += 1
# sorts midterm scores from highest to lowest and then adds top two  
# and halves bottom two
midterms.sort(reverse=True)
midterm_score = midterms[0] + midterms [1] + 0.5*(midterms[2] + midterms[3])

# gets final score and then totals grade
final_score = int(input("Final: "))
grade = quiz_score + midterm_score + final_score

print(f'\nYour total grade in the class is {grade}%\n')
print(f'Your assignment point total is {quiz_score} out of 20')
print(f'Your midterms point total is {midterm_score} out of 60')
print(f'Your finals point total is {final_score} out of 20')
