number=int(input())
temp=number
reverse=0
while(number>0):
    remainder=number%10
    reverse=reverse*10 + remainder
    number=number//10
if(reverse==temp):
    print("palindrome")
else:
    print("not a palindrome")