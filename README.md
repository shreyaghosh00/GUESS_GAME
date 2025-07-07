# GUESS_GAME
# 🎯 Number Guessing Game

This is a simple Python-based number guessing game designed to test your intuition and luck! Built using basic Python concepts such as loops, conditionals, and random number generation, the game challenges you to guess a randomly selected integer within a limited number of tries.

---

## 📌 How It Works

1. You input a lower and upper limit.
2. The program randomly selects an integer `x` within that range.
3. You get a limited number of chances based on the formula:
   total_chances = ceil(log2(upper - lower + 1))
4. With each guess, you're told if your guess is too high or too low.
5. The game continues until you guess the number or run out of chances.

## 🛠️ Technologies Used

1. Python 3+
2. `random` and `math` modules (standard libraries)


## 🚀 Getting Started

Clone the repository and run the script using any Python interpreter:

```bash
python number_guessing_game.py
