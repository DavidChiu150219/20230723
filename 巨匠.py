def play():
    import random 
    try:
        mini=int(input('Please enter the minimum:'))
        maxi=int(input('Please enter the maximum:'))
    except:
        print('Value Error')
    else:
        n=random.randint(mini,maxi)
        t=0

        while True:
            x=int(input(f'Please enter a number between {mini} and {maxi}:'))
            t+=1
            if x<mini or x>maxi:
                print('out of range')
            else:
                if x!=n:
                    if x>n:
                        print('The answer is smaller')
                        maxi=x
                    else:
                        print('The answer is bigger')
                        mini=x
                else:
                    break
    print(f'Congratulations! The answer is {n}')

while True:
    play()

    try:
        a=str(input('Do you want to continue?(y or n)'))
    except:
        print('Enter again!')
    else:
        if a=='n':
            break
print('This is the end of the game')