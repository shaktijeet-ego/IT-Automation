a = 1
sum = 0

while a<=10:
    sum+=a #sum = sum + 1
    a = a + 1
    print(str(sum) + "<=")
    print("a = " + str(a))

b=1
product = 0
while b < 5:
    product *= b
    b = b + 1
    print("product = " + str(product))
    print("b = " + str(b))

c = 5
division = 0
while c<10:
    division = division/c
    print(c)
    c = c + 1
    print("division = " + str(division))
    print("The value of c incremented = " + str(c))



# count down
print("===============")
start_time = 10
while start_time > 0:
    print("Tik tok !!! = " + str(start_time))
    start_time = start_time - 1


#with function

def count_down(start_number):
    current = start_number
    while current>0:
        current-=1
        print("Tik tok  = " + str(current))
    print("Zero!!!!!")
count_down(2)

#another
def count_down(start_number):
    while start_number>0:
        start_number-=1
        print("Tik tok  = " + str(start_number))
    print("Zero!!!!!")
count_down(5)
