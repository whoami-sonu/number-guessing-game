import random
import json
import os
import matplotlib.pyplot as plt

DATA_FILE = "scores.json"

# ---------------------------
# Load / Save Scores
# ---------------------------
def load_scores():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_score(name, attempts):
    data = load_scores()
    data.append({"name": name, "attempts": attempts})
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------------------
# Leaderboard
# ---------------------------
def show_leaderboard():
    data = load_scores()
    if not data:
        print("No scores yet.")
        return

    sorted_data = sorted(data, key=lambda x: x["attempts"])
    print("\n🏆 Leaderboard:")
    for i, entry in enumerate(sorted_data[:5]):
        print(f"{i+1}. {entry['name']} - {entry['attempts']} attempts")

# ---------------------------
# Analytics (Graph)
# ---------------------------
def show_graph():
    data = load_scores()
    if not data:
        print("No data to plot.")
        return

    attempts = [d["attempts"] for d in data]

    plt.figure()
    plt.plot(attempts)
    plt.title("Attempts History")
    plt.xlabel("Games")
    plt.ylabel("Attempts")
    plt.show()

# ---------------------------
# Game Logic
# ---------------------------
def play_game():
    print("\n🎮 Advanced Number Guessing Game")

    levels = {"1": 50, "2": 100, "3": 200}

    print("\n1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Choose difficulty: ")
    max_range = levels.get(choice, 100)

    number = random.randint(1, max_range)
    attempts = 0

    print(f"\nGuess number between 1 and {max_range}")

    while True:
        guess = input("Enter guess (or 'exit'): ")

        if guess.lower() == "exit":
            print("Game exited.")
            return

        try:
            guess = int(guess)
            attempts += 1

            diff = abs(guess - number)

            # 🔥 Smart AI hint system
            if guess > number:
                if diff > 20:
                    print("⬇️ Way too high!")
                else:
                    print("⬇️ Slightly high!")
            elif guess < number:
                if diff > 20:
                    print("⬆️ Way too low!")
                else:
                    print("⬆️ Slightly low!")
            else:
                print(f"🎉 Correct in {attempts} attempts!")
                name = input("Enter your name: ")
                save_score(name, attempts)
                break

        except:
            print("❌ Invalid input!")

# ---------------------------
# Main Menu
# ---------------------------
def main():
    while True:
        print("\n🔥 MAIN MENU")
        print("1. Play Game")
        print("2. Leaderboard")
        print("3. Show Analytics Graph")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            show_graph()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
