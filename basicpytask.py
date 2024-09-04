# question 10
'''a=[10,20,25,30,35]
b=[40,45,60,75,90]

odd_num=[num for num in a if num%2!=0]
even_num=[num for num in b if num%2==0]

result= odd_num + even_num
print(result)'''

#question 9
'''def palindrome(num):
    str_num = str(num)
    
    if str_num == str_num[::-1]:
        return "Yes. given number is palindrome number"
    else:
        return "No. given number is not a palindrome number"
number = input("enter a number:")
print(f"entered number: {number}")
print(palindrome(number))'''

#8
'''a=5
for i in range(1,a+1):
    print(str(i)*i)'''

#question 7
'''a = "Emma is good developer. Emma is a writer"
b = "Emma"

count = a.count(b)
print(" '{b}' appears {count} times in the given string.")'''

#question 6
'''numbers = [10, 20, 33, 46, 55]

print("Given list is", numbers)
print("Divisible by 5:")

for number in numbers:
    if number % 5 == 0:
        print(number) '''

# question 5
'''x = [10, 20, 30, 40, 10]
y = [75, 65, 35, 75, 30]
def check(self):
    if x[0] == x[-1]:
        return True
    else:
        return False
def Check(self):
    if y[0] == y[-1]:
        return True
    else:
        return False

print(f"Given List: {x}, result is {check(x)}")
print(f"Given List: {y}, result is {Check(y)}")'''

#question 4:

def remove_chars(s, n):
    if n < len(s):
      return s[n:]
    else:
      return ""

print(remove_chars("PYnative", 4)) 
print(remove_chars("PYnative", 2)) 


# question 3

'''a ="PYnative"
print("Original String is", a)
print("Printing only even index chars:")

for i in range(0, len(a), 2):
    print(a[i])'''

# question 2
'''print("Printing current and previous number sum in a range(10)")

previous_num = 0

for current_num in range(10):
    sum_num = current_num + previous_num
    print(f"Current Number {current_num} Previous Number {previous_num} Sum: {sum_num}")
    previous_num = current_num'''

#question 1
'''def calculate_result(number1, number2):
    product = number1 * number2
    
    if product <= 1000:
        return product
    else:
        return number1 + number2
number1 = 20
number2 = 30
result = calculate_result(number1, number2)
print(f"The result is {result}")

number1 = 40
number2 = 30
result = calculate_result(number1, number2)
print(f"The result is {result}")'''
