try:
    num = float(input("enter value : "))
    print(f"model accuracy is {num}")
except ValueError:
    print("entered num is not numeric")
