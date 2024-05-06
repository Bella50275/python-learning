grade = int(input("what is your grade level?:"))
if grade >= 10 and grade <= 12:
    print("you can join science club, or drama club")
else:
    print("you cannot join science club, however you can join drama club.")

activity = (input("what activity do you want to join?:"))
grade = int(input("what is your grade level?:"))
if grade >= 10 and grade <= 12:
    print("you are eligible for chosen activity")

notifications = input("Do you want notifications on SMS or email?:")
if notifications == SMS:
    print("you will receive updates on SMS.")
else:
    print("you will receive notifications on email.")

leadership = input("do you want leadership role within activity?:")
if leadership == yes:
    print("You'll be considered for leadership position.")
else:
    print("no problem, no need to want leadership position.")