print("enter a number")
number=int(input())
if number > 1:
    for i in range(2,int(number/2)+1):
        if(number%i==0):
            print("number is not prime")
            break
        else:
            print("number is prime")
            break


