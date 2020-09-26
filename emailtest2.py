def check_email():
    count = 4
    while count > 0:
        email = input("Enter your email")
        index = email.index("@")
        email_result = email[index:]
        print(email_result)

        if email_result == "@yahoo.com":
            print("Yahoo mail")
            break
        else:
            print("Not a yahoo mail")
            count = count - 1
            print("You have {} attempts left".format(count))
    print("Try next time")


check_email()

