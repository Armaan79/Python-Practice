import random
secret_number=random.randint(1, 100)
attempts=0
print("----Number Guessing Game----\n")
print("""Choose difficulty level: 
      
1. Easy
2. Medium
3. Hard""")
while True:
  diff=int(input("\nEnter  your difficulty:"))
  if diff==1:
     total_attempts=10
     break
  elif diff==2:
     total_attempts=7
     break
  elif diff==3:
     total_attempts=5
     break
  else:
     print("\nInvalid input")
while True:
    if attempts>=total_attempts:
        print("\nGame over!")
        print(f"The correct number was {secret_number}")
        break
    guess=int(input("\nEnter your guess: "))
    attempts+=1
    if guess>secret_number:
        print("Too high!!")   
    elif guess<secret_number:
        print("Too low!!")
    else:
        print("\nCongratulations!!!!")
        print(f"You guessed it in {attempts} attempts")
        break
    