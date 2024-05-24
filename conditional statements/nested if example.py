age = int(input("enter the age: "))

if age>=18:
    score = int(input("enter the score: "))
    if score>=40:
        print("you're age and score qualified")
    else:
        print("you're age is qualified but score is not qualified")
else:
    print("you're age is not qualified")

