# for i in range(1,10):
#     print(i)

# for a in range(2,20,2):
#     print(a)

# number = int(input('Enter your number : '))
# for a in range(1,11):
#     print(f"{number}  x {a} = {number*a} ")

# start = int(input('Ente the starting point of numbers : '))
# end = int(input('Enter the ending point of numbers : '))
# if start<end :
#     for number in range(start,end):
#         print(number )
# else:
#     print('Your number flow is wrong ')
    

# Exercise 1 
# fizzbuzz = []
# fizz = []
# buzz = []
# for num in range(1,50):
#     if num %3 ==0 and num % 5 == 0:   
#         fizzbuzz.append(num)
#         for a in fizzbuzz:
#             print(f"Fizzbuzz {a}")
#     elif num % 3 ==0 :
#         fizz.append(num)
#         for b in fizz:
#             print(f"Fizz : {b}")
#     elif num%5==0 :
#         buzz.append(num)
#         for c in buzz:
#             print(f"Buzz : {c}")
#     else:
#         print(num)

# Exercise 2 
# start = int(input('Enter the starting number : '))
# end = int(input('Enter the ending number : '))
# even  = 0
# odd = 0
# for num in range(start,end):
#     if num%2 ==0:
#         even+=num
#     else:
#         odd+=num 
# print(f"Sum Even : {even}") 
# print(f"Sum Odd : {odd}") 
   
# Exercise 3 
# num = int(input("Enter a number greater than 1 : "))

# if num < 2:
#   print("Invalid Number! Must be greater than 1.")
# else:
#   is_prime = True

#   for i in range(2, num):
#     if num % i == 0:
#       is_prime = False
#       break  # Found a divisor! Stop checking immediately.

#   if is_prime:
#     print(f"{num} is a Prime Number! ")
#   else:
#     print(f"{num} is a Composite Number (not prime).")

# Exercise 1 reversed 
# fizzbuzz = []
# fizz = []
# buzz = []

# for num in range(1, 51):
#   if num % 3 == 0 and num % 5 == 0:
#     fizzbuzz.append(num)
#   elif num % 3 == 0:
#     fizz.append(num)
#   elif num % 5 == 0:
#     buzz.append(num)

# # Print everything cleanly AFTER the loop finishes
# print("--- RESULTS ---")
# print(f"FizzBuzz numbers: {fizzbuzz}")
# print(f"Fizz numbers: {fizz}")
# print(f"Buzz numbers: {buzz}")

# Exercise 3 reversed 
# num = int(input("Enter a number greater than 1 : "))
# divisors = []

# if num < 2:
#   print("Invalid Number ")
# else:
#   # Find all divisors and put them in the list
#   for i in range(2, num):
#     if num % i == 0:
#       divisors.append(i)

#   # Check the list at the end
#   if len(divisors) > 0:
#     print(f"Divisors of {num}: {divisors}")
#     print(f"{num} is a Composite Number (not prime).")
#   else:
#     print(f"{num} has no divisors. It is a Prime Number! ")



# Mashq 2
# son = int(input('Son kiriting : '))
# boluvchilar = []
# if son<=1 :
#     print('Invalid Number!')
# else:
#     for i in range(1,son+1):
#         if son%i == 0:
#             boluvchilar.append(i)
#     print(boluvchilar)    

# Mashq 3
# import random 
# numbers = [random.randint(1,100) for _ in range(10)]
# high = numbers[0]
# for num in numbers:
#     if num > high :
#         high = num 
# print(numbers)
# print(high )        
  
# Mashq 1 
# text = input('Enter a sentence or word : ')
# vowels = 0 
# consonants = 0 
# others = 0
# for char in text :
#     if char.lower() in 'aeiou':
#         vowels +=1 
#     elif char.isdigit():
#         consonants+=1 
#     else:   
#         others+=1
# print(f"Vowels : {vowels}")        
# print(f"Consonants : {consonants}")
# print(f"Others : {others}")


# Mashq 1 
# son = int(input('Son kirit : '))
# while son>=1 : 
#     print(son)
#     son-=1
# print('Vaqt Tugadi ')

# Mashq 2 
# password = 'python123' 
# attempt = input('Enter the password: ')
# while True :
#    if password != attempt :
#     print('You entered a wrong password try again ')
#     continue 
#    else:
#      print('You entered the right password')
#      break 

parol = ''
password = 'python123'
while parol != password : 
    if parol != password  :
        print(f"Notogri parol, qayatadan urinib koring!")
print('Xush Kelibsiz ')        
         



