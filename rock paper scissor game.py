import random
signs = ["rock","paper","scissor"]
print('select signs from the list ',signs,"0,1,2 respectively")
n=int(input())
user=signs[n]
comp=random.choice(signs)
print("user selected ",user)
print("computer selected",comp)
if (comp == 'rock' and user == 'paper' ):
    print("user wins")
elif (comp == 'paper' and user == 'scissor' ):
    print("user wins")
elif (comp == 'scissor' and user == 'rock' ):
    print("user wins")    
elif(comp == user):
    print("tie! try again") 
else:
    print("computer wins!!")   