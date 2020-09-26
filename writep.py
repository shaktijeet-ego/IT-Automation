f = open("demofile.txt", "a")

listing = [1,2,3,4,5]

for lists in listing:
    print (lists)
    f.write(str(lists),)
f.close()


