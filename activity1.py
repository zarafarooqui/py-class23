#take input from user
number= int(input("Enter your number:"))

#store original number for comparison
temp=number
reversed_number = 0

#Reverse the number
while temp > 0:
    digit = temp%10
    reversed_number = reversed_number * 10 + digit
    temp //= 10

if number == reversed_number:
    print(f"{number} is a palindrome")
else:
       print(f"{number} is not a palindrome")