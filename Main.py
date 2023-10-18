import random


myAccount = 0
Prize = ["Congratulations! You've found a chest!", "Unfortunately, you found nothing."]


Chest1 = {'Color':'Green', 'Points': 1000}
Chest2 = {'Color':'Orange', 'Points': 4000}
Chest3 = {'Color':'Purple' ,'Points': 9000}
Chest4 = {'Color':'Gold', 'Points': 16000}
Chests = [Chest1,Chest2,Chest3,Chest4]

print("Welcome in my game")
print("You have only 5 moves left. Let's see how much treasure you can uncover!")


gamerChoice = 1

while gamerChoice <= 5:
    print(f"Move {gamerChoice}:")
    step = input("Do you wish to move forward? (Type 'yes' or 'no'):  \n")
    gamerChoice += 1

    #Main option 'yes'
    if step == 'yes':
        print("Alright, let's see what destiny has in store for you...")
        percentageStep = random.choices(Prize,[60,40],k = 100)
        stepYesOrNo = random.choice(percentageStep)
        print(stepYesOrNo)

        if stepYesOrNo == Prize[0]:
            percentageOfTheBox = random.choices(Chests,[75,20,4,1],k = 100 )
            kindOfTheBox = random.choice(percentageOfTheBox)
            print("You've discovered :", kindOfTheBox['Color'])
            myAccount += kindOfTheBox['Points']
            print("Added points to my account!!!")
            if gamerChoice > 5:
                print("My points scored:", myAccount)

    #Finish the program
    elif step == 'no':
        print("Goodbye! Thanks for playing.")
        break

    #What if we use the other options
    else:
        print("Sorry, you've selected an invalid option. Please try again:\n")
        gamerChoice -= 1
        continue