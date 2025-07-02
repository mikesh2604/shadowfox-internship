import random

# Words with hints
words = {
    "python": "A popular programming language 🐍",
    "guitar": "A musical instrument 🎸",
    "elephant": "The largest land animal 🐘",
    "pizza": "A popular Italian dish 🍕",
    "india": "A country in South Asia 🇮🇳",
    "oxygen": "Gas essential for breathing 🫁",
    "chess": "A two-player strategy board game ♟️"
}

# Hangman drawings for each stage
hangman_pics = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# Pick a word and its hint
word, hint = random.choice(list(words.items()))
guessed = ['_'] * len(word)
wrong_attempts = 0
max_attempts = len(hangman_pics) - 1
guessed_letters = []

# Game start
print("🎯 Welcome to Hangman with Hints!")
print(f"💡 Hint: {hint}")

while wrong_attempts < max_attempts and ''.join(guessed) != word:
    print(hangman_pics[wrong_attempts])
    print("Word: ", ' '.join(guessed))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⛔ You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong guess!")
        wrong_attempts += 1

# Game result
if ''.join(guessed) == word:
    print("\n🎉 You won! The word was:", word)
else:
    print(hangman_pics[wrong_attempts])
    print("\n💀 Game Over! The word was:", word)
