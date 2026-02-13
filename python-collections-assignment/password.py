password="admin123"
entered_password=input("enter password:")

while entered_password != password:
    print("Access denied!")
    entered_password=input("enter password again:")

print("Access granted!")