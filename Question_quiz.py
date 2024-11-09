from Question import Question

questions = [
"What is color of apple\n (a)red\n (b)blue\n (c)purple",
"What is color of bananas\n (a)red\n (b)blue\n (c)yellow"
 
]

Questions = [
    Question(questions[0],'a'),
    Question(questions[1],'c')
]

score =0
for q in Questions:
    ans=input(q.prompt+"\n")
    if ans == q.answer:
        score+=1
    
print("Scored "+str(score)+"/"+str(len(questions)))
