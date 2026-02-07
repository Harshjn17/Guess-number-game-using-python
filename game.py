secret_num = 10
attempt = 0

while True:
    guess = int(input("Enter the num for guess: "))
    attempt += 1
    
    if guess > secret_num:
        print("Too high")
        
    elif guess < secret_num:
        print("Too low")
        
    else:
        print("Correct")
        print("Attempts",attempt)
        break
