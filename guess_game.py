import random
import json
import os

FILE = "score.json"

# ---------- LOAD BEST SCORE ----------
def load_score():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {"best": None}

def save_score(score):
    with open(FILE, "w") as f:
        json.dump({"best": score}, f)

# ---------- GAME ----------
def play():
    print("\n🎮 Number Guessing Game")

    print("\nSelect Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Choose: ")

    if choice == "1":
        max_num = 50
    elif choice == "2":
        max_num = 100
    else:
        max_num = 200

    number = random.randint(1, max_num)
    attempts = 0

    print(f"\nGuess number between 1 and {max_num}")

    while True:
        try:
            guess = int(input("Enter guess: "))
            attempts += 1

            if guess < number:
                print("⬆️ Too low!")
            elif guess > number:
                print("⬇️ Too high!")
            else:
                print(f"🎉 Correct! Attempts: {attempts}")
                return attempts
        except:
            print("Enter valid number!")

# ---------- MAIN ----------
def main():
    score_data = load_score()

    while True:
        attempts = play()

        # Best score update
        if score_data["best"] is None or attempts < score_data["best"]:
            score_data["best"] = attempts
            save_score(attempts)
            print("🏆 New Best Score!")

        print(f"⭐ Best Score: {score_data['best']}")

        again = input("\nPlay again? (y/n): ")
        if again.lower() != "y":
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
