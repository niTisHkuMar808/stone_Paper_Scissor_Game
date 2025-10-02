import random
print("Enter Stone,Paper,Scissor to play this Game")
print("Enter Q for quit from this game")
option=["stone","paper","scissor"]
Bot_count=0
user_count=0
while True:
    user=input("Enter your Choice: ").lower()
    if user=="q" :
        print("Thanks for playing !!")
        break
    if user not in option:
        print("Invalid input! please try again")
        continue
    Bot=random.choice(option)
    print(f"Bot choice: {Bot}")
    if(Bot==user):
        print("It's a Draw! ")
    elif(user=="stone" and Bot=="scissor") or (user=="paper" and Bot=="stone") or (user=="scissor"and Bot=="paper"):
        print("You Win!")
        user_count+=1
    else:
        print("You Lose!")
        Bot_count+=1
    print(f"Score= You:{user_count}|Bot={Bot_count}")
print("Final_Score:")
print(f"You score: {user_count}| Bot score: {Bot_count}")
print("Thanks For playing :)")