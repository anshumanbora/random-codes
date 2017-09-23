#
# Anshuman Bora
# 1211247437 | abora3@asu.edu
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
# This implementation will take user input and run for one time.


import random
choices = [1,2,3]


hatContainingPrize = random.randint(1,3)
hatChosen = input('Choose your hat [ 1,2 or 3 ]: ')
print ('You chose hat ', hatChosen)

for x in choices:
    if x != hatChosen and x != hatContainingPrize:
        print('Hat ', x ,' doesn\'t contain your prize.')
        break

choice = input('Press \'y\' to keep your original choice.Press \'n\' to change hat: ')


if choice == 'y':
    if int(hatChosen) == hatContainingPrize:
        print('Hit')

    else:
        print('Miss')
elif choice == 'n' :
    if int(hatChosen) != hatContainingPrize:
        print ('Hit')

    else:
        print ('Miss')



