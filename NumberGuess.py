import random
print("Welcome to the number guessing game! the minimum number is 0 and the maximum is 100!")
attempts = 5
wins = 0
loses = 0
randomnumber = random.randint(0, 100)
while True:
    if attempts == 0 and loses > 0 or attempts == 5 and loses == 0:
        console = input(
            "CONSOLE: 1 to view wins, 2 to view loses, 3 to exit console, 4 to exit game ")
        if console.lower() == "1":
            print(wins)
        elif console.lower() == "2":
            print(loses)
        elif console.lower() == "3":
            pass
        elif console.lower() == "4":
            exit()
    guess = int(input("Enter guess: "))
    if guess < randomnumber:
        print("Guess too low")
        attempts -= 1
    elif guess > randomnumber:
        print("Guess too high")
        attempts -= 1
    elif guess == randomnumber: 
        print("You won!")
        randomnumber = random.randint(1, 100)
        attempts = 5
        wins += 1
        console = input(
            "CONSOLE: 1 to view wins, 2 to view loses, 3 to exit console, 4 to exit game ")
        if console.lower() == "1":
            print(wins)
        elif console.lower() == "2":
            print(loses)
        elif console.lower() == "3":
            pass
        elif console.lower() == "4":
            exit()
    if attempts == 0:
        print(f"You lost. The number was {randomnumber}")
        loses += 1
        randomnumber = random.randint(1, 100)
        attempts = 5
        console = input(
            "CONSOLE: 1 to view wins, 2 to view loses, 3 to exit console, 4 to exit game ")
        if console.lower() == "1":
            print(wins)
        elif console.lower() == "2":
            print(loses)
        elif console.lower() == "3":
            pass
        elif console.lower() == "4":
            exit()
        pass
