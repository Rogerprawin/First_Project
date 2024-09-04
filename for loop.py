#question 1 
'''Print Numbers 1 to 10
Write a program that prints the numbers from 1 to 10, each on a new line. '''

'''for i in range (1,11):
    print(i)'''

#question 2
'''Sum of a List
Given a list of numbers, write a program that calculates and prints the sum of all the numbers in the list.'''

'''a = [1, 2, 3, 4, 5]
sum = 0
for i in a:
    sum += i
print(sum)'''

#question 3
'''Count Vowels in a String:'''

'''string="to customize run and debug"
vowels="a,e,i,o,u"
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)'''

#question 4

'''Print a Multiplication Table
Write a program that prints the multiplication table for a given number n up to 10.
 For example, if n is 3, print:

3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30'''

'''n = int(input("enter a number:"))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")'''

#question 5
'''Find Even Numbers
Write a program that prints all even numbers from 1 to 20.'''
'''for i in range(1,21):
    if i%2==0:
        print(i)'''

#question 6
'''Generate Fibonacci Sequence:'''
'''n = 10
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
    print(a, end=' ')'''

#question 7
'''Print a Pyramid Pattern
Write a program that prints a pyramid pattern of stars. For example, for n = 5:'''

'''for a in range (5):
    for b in range(a+1):
        print("*",end="")
    print()'''

#question 8
'''Count Occurrences of a Character
Write a program that counts and prints the number 
of times a specific character appears in a given string'''

'''string = " times a specific character appears in a given string"
char = 'a'
count = 0
for c in string:
    if c == char:
        count += 1
print(count)'''

#question 9
'''Find Prime Numbers
Write a program that prints all prime numbers between 1 and 50.'''
'''for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)'''

#question 10
'''print z pattern'''

'''for a in range(5):
    for b in range(5):
        if (a==0 or a==4) or (b==3 and a==1) or (b==2 and a==2) or (b==1 and a==3):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()'''








