# Write a program capable of displaying questions to the users like KBC

# Requirements
#Make a list of questions 
# Store questions and answers 
# Take input(answer) from user
# compare it to your answer 
# if yes give amount and add one by one and if uncorrect do not give prize  

KBC=[("When Pakistan came into being:","1947")
     ,("Which countries comes under sub-continent:","India and Pakistan"),
     ("Who is the founder of pakistan:","Quaid e azam")]


# because we have to make answer store and answer that we are providing in same case so it can match successfully
prizePerCorrectAnswer=0

for questions,correct_answers in KBC:
    
    answer=input(f"{questions}?")
    
    # now both are in same case 
    UserAnswer=answer.lower()
    Listanswer=correct_answers.lower()
    
    if UserAnswer==Listanswer:
        print("Correct Answer! You won 100")
        prizePerCorrectAnswer=prizePerCorrectAnswer+100
    else:
        print("Uncorrect Answer! Shit")
        
print("Total Amount you won is:", prizePerCorrectAnswer)
        
        
      