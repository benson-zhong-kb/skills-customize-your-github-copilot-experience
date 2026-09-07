
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice string manipulation, loops, conditionals, user input, and random selection while tracking the player's progress and remaining attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Use the provided starter code to choose a secret word and initialize the variables needed to track the game state.

#### Requirements

Completed program should:

- Select one word at random from the predefined `words` list using the `random` module.
- Store the player's guessed letters in a collection that can be checked and updated.
- Set a maximum number of incorrect guesses and track the number used during the game.
- Treat guesses without regard to letter case.

### 🛠️ Implement the Guessing Game

#### Description

Create the main game loop so the player can guess letters, reveal the secret word, and receive a result when the game ends.

#### Requirements

Completed program should:

- Display the current progress with unguessed letters hidden, such as `_ _ _ _ _ _`.
- Ask the player for one letter at a time and record each guess.
- Update the displayed progress when a guessed letter appears in the secret word.
- Decrease the remaining attempts after an incorrect guess and show the current count.
- End when the player reveals the entire word or uses all allowed incorrect guesses.
- Display a clear win message with the secret word or a clear lose message that reveals it.

For example, a game in progress could display:

```text
Word: _ _ _ _ _ _
Incorrect guesses remaining: 5
Guess a letter: p
Word: p _ _ _ _ _
```
