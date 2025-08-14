Python Practice & Mini Project Collection

This repository contains a collection of Python problems and exercises I’ve solved to improve my coding skills, along with a small word game project.  
The problems range from **very basic Python concepts** to **slightly medium-level challenges**, covering a variety of topics.

---

1. Practice Problems
- Covers Python fundamentals:  
  - Variables & Data Types  
  - Strings & String Operations  
  - Lists, Tuples, Sets, Dictionaries  
  - Conditional Statements & Loops  
  - Functions  
  - File Handling  
  - Basic Algorithms  
- Gradually increases in difficulty from beginner to intermediate.

2.Word Games
- **Guess the Word**
  - Guess the letters of a hidden word using its **meaning as a clue**.
  - Limited tries (6) to guess the word correctly.
  - Optional letter clues (max 3) at the cost of points.
- **Jumbled Words**
  - Unscramble shuffled letters to form the correct word.
  - Meaning of the word is provided as a hint.
  - Optional position-revealing clues.

---

**Scoreboard System**
- Stores player names and their highest scores.
- Uses **Python’s pickle module** to save scores between game sessions.
- Displays scores in a sorted leaderboard format.

---

**NLTK Integration**
- Uses `nltk.corpus.words` to generate real dictionary words.
- Fetches word definitions using `nltk.corpus.wordnet` to provide hints.
- Filters words based on difficulty level (Easy / Hard).

---

## Skills Demonstrated
- **Python Programming**: Functions, loops, conditionals, data structures.
- **External Libraries**: NLTK for word handling and definitions.
- **File Handling**: Persistent data storage using pickle.
- **Game Logic**: Score tracking, user input validation, replay loops.
- **Problem-Solving**: Dynamic word selection with error handling.
