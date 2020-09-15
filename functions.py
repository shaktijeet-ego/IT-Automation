def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def div(a,b):
    return a/b

choice_list = ["1.Add", "2.Subtract","3.Div"]

for choices in choice_list:
    print (choices)

a = int(input("First number"))
b = int(input("second number"))

choice = input("enter your choice: ")

if choice == "1":
    print(sum(a,b))
elif choice == "2":
    print(subtract(a,b))
else:
    print(div(a,b))
    




user_name = input("Enter your name: ")

