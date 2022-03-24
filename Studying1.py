print("Hello World")

while True:
    question=input("Give two numbers separated by a coma:")
    question.split(",")


    for a, b in question:
        if a>b:
            print(f"{question[0]} is greater than {question[1]}")
        else:
            print("The second one is equal or larger")
