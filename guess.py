import random
randnum=random.randint(0,100)
unum=int(input("Enter a number between 1-100:"))
if randnum==unum:
    print(f"Congratulation you have succsed to guessed a number in a first try and it was,{unum}")
else:
    while randnum!=unum:
        if unum>100 or unum<0:
            unum=int(input("You have entered a number lesser than 0 or greater than 100 so please enter a num between 1-100::"))
            
        else:
            if unum>randnum:
                unum=int(input("Enter a lesser number"))
            elif unum<randnum:
               unum=int(input("Enter a greater number"))

print("Congratulation you have guessed right and it was ",unum)
                             