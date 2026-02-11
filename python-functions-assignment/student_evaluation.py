def greet(name):
    return "Hello, " + name

def calculate(scores):
    subjects = len(scores)
    average = sum(scores) / subjects
    return subjects, round(average, 2)

def result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    name = input("Enter name: ")
    n = int(input("Enter number of subjects: "))
    
    scores = []
    for i in range(n):
        marks = float(input("Enter marks: "))
        scores.append(marks)

    subjects, average = calculate(scores)
    final = result(average)

    print(greet(name))
    print("Subjects:", subjects)
    print("Average Score:", average)
    print("Result:", final)

main()
