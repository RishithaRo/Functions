 # There are 4 models to write a function
'''
1)No sending arguments and no return values
2)Sending arguments and no return values
3)Sending arguments and return values
4)No Sending arguments and return values
'''

# 1) No sending arguments and no return values
# Here, iam not sending any arguments and not returning any values from the function
print("No sending arguments and no return values")
def usa():
    print("iam in usa...")
def singapore():
    print("iam in singapore")
def india():
    print("iam in india..")
def dubai():
    print("iam in dubai")
india()
usa()
dubai()
singapore()

# 2) Sending arguments and no return values
# Here, iam sending arguments but no returning any values from the function
print(" ")
print("Sending arguments and no return values")
def add(a,b):
    print("The sum is:",a+b)
def sub(a,b):
    print("The subtraction is:",a-b)
def mul(a,b):
    print("The multiplication is:",a*b)
def div(a,b):
    print("The division is:",a/b)
add(2,3)
mul(10,8)
sub(8,5)
div(8,2)

# 3)Sending arguments and return values
# Here, iam sending arguments and getting return values
print(" ")
print("Sending arguments and return values")
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print(add(2,3))
print(mul(10,8))
print(sub(8,5))
print(div(8,2))

# 4)No Sending arguments and return values
# Here, iam not sending any arguments but iam getting return values
print(" ")
def text():
    return "Hello"
message=text()
print("The message is:",message)

'''-------------------------------OUTPUT-------------------------------
No sending arguments and no return values
iam in india..
iam in usa...
iam in dubai
iam in singapore
 
Sending arguments and no return values
The sum is: 5
The multiplication is: 80
The subtraction is: 3
The division is: 4.0
 
Sending arguments and return values
5
80
3
4.0
 
The message is: Hello
'''





























