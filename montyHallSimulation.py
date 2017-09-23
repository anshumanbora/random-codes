#
# PROBLEM
# Someone shows you three hats and tells you that the there is a
# prize in one of them. He asks you to choose one of the hats. You
# choose one hat and tell him which one you chose. He then lifts one
# of the hats you didn’t choose and there is nothing under that hat. 
# He then tells you that you can either stay with the hat you have 
# originally chosen or switch to the other remaining hat
#
#  IMPLEMENTATION
# This implementation will simulate the code over a range
# and show the overall results in the end.


import random
choices = [1,2,3]

#number of times user won after he stuck to his oirginal choice
winWithOriginal = 0

#number of times user won after he changed his choice
winAfterChanging = 0

yourRange = input('\nHow many time do you want to run this simulation? ')

for i in range(int(yourRange)):

    print ('\nCurrent iteration:', i+1)
    hatContainingPrize = random.randint(1,3)
    hatChosen  = random.randint(1,3)
    print ('You chose hat ', hatChosen)

    for x in choices:
        if x != hatChosen and x != hatContainingPrize:
            print('Hat ', x ,' doesn\'t contain your prize.')
            break


    # 1 denotes user kept original choice. 2 denotes he changed his choice
    choice = random.randint(1,2)

    if choice == 1:
        print('You stuck to the original choice and it is a...')
        if int(hatChosen) == hatContainingPrize:
            print('Hit')
            winWithOriginal+=1
        else:
            print('Miss')
    elif choice ==2 :
        print('You changed your choice and it is a...')
        if int(hatChosen) != hatContainingPrize:
            print ('Hit')
            winAfterChanging+=1
        else:
            print ('Miss')



winYes= (100*(winWithOriginal/(winWithOriginal+winAfterChanging)))
winNo = (100*(winAfterChanging/(winWithOriginal+winAfterChanging)))

print('\n\nOut of total wins\nWin % with original choice: ',winYes,'\nWin % after changing hat: ',winNo)
