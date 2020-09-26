x = 0
while x < 5:
    print("Not there yet" + str(x))
    x = x + 1
print("Final value: " + str(x))


username = "m"

x=0
while x < 5:
    if username == "me":
        print("welcome")
        break
    else:
        print(x)
        x = x + 1
        #print(x)


print("=============================")

def count_down(current):
    while (current > 0):
        print("Counting down to " + str(current))
        current = current - 1
    print("Zero")

count_down(20)



