age = int(input("Age: "))
has_id = input("Has ID (True/False): ").strip().lower()

if has_id == "true":
    has_id = True
elif has_id == "false":
    has_id = False
else:
    print("Invalid boolean input")
    exit()

if age >= 20 and has_id:
    print("Entry allowed")
else:
    print("Entry not allowed")
