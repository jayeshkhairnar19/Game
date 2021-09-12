limit=1
count=0
computer_score=0
human_score=0
print('\t\t\t\tWELCOME TO THE GAME')
print('Important rules for the game are given below')
print('stone=s\nPaper=p\nScissor=c')
print('You have only 21 chances to play the game and if you manage to score more than computer then you will be winner!')
import random
list=['s','p','c']
while(limit<=21):
    x=input('Enter your choice:')
    limit+=1
    
    choice=random.choice(list)
    count+=1
    
    print('The no of attempts are',count,'out of 21.')
   
    
   # print(choice)
    
    if(x==choice):
        #print(x)
        
        print("Computer's choice:",choice)
        print('Answers for both of you is same...so no points will be given')
    elif x=='s' and choice=='p':
       
        print("Computer's choice:",choice)
        print('Computer wins')
        
        
        computer_score+=1
        print('Human score is:',human_score)
        print('computer score is:',computer_score)
        
    elif x=='s' and choice=='c':
        
        print("Computer's choice:",choice)
        
        print('Human wins')
       
        
        human_score+=1
        
        print('Human score is:',human_score)
        print('computer score is:',computer_score)
        
    elif x=='p'and choice=='s':
        
        print("Computer's choice:",choice)
        print('Human wins')
        
        human_score+=1
        
        print('Human score is:',human_score)
        print('computer score is:',computer_score)
        
    elif x=='p' and choice=='c':
        
        print("Computer's choice:",choice)
        print('Computer wins')
        
        
        computer_score+=1
        print('Human score is:',human_score)
        print('computer score is:',computer_score)
        
    elif x=='c' and choice=='s':
       
        print("Computer's choice:",choice)
        print('Computer wins')
        
        
        computer_score+=1
        print('Human score is:',human_score)
        print('computer score is:',computer_score)

    elif x=='c' and choice=='p':
        
        print("Computer's choice:",choice)
        print('Human wins')
        
        human_score+=1
        
        
        print('Human score is:',human_score)
        print('computer score is:',computer_score)
         
   
if human_score>computer_score:
   
    print('\nHUMAN WINS THE GAME AT THE END.And the score of human is',human_score,'and score of computer is',computer_score)
    print('Thanks for giving your time,hope you have enjoyed the game')
elif human_score==computer_score:
    
    print('\nThe game is tied and the the score of human is',human_score,'and score of computer is',computer_score)
    print('Thanks for giving your time,hope you have enjoyed the game')
else:
    
     print('\nCOMPUTER WINS THE GAME AT THE END.And the score of human is',human_score,'and score of computer is',computer_score)
     print('Thanks for giving your time,hope you have enjoyed the game')      
            
        
