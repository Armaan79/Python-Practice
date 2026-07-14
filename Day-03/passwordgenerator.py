import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password=""
while True:
    a = int(input("Enter the length of password: "))
    if a >= 6:
        break
    print("Password length should be at least 6!")
for i in range(a):
    b=random.choice(characters)
    password+=b
print(f"Your password: {password}")