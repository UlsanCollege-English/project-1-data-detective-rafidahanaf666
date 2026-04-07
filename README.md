[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cDnlIYNC)
# P1: Data Detective

## Summary
This project analyzes a text file, counts word frequencies, shows the top N most common words, and provides an additional insight. The program converts raw text into structured data, making it easier to understand patterns in word usage.

## Dataset
- File: The Crime Code by William Le Queux
- Why I chose it: I chose this dataset because it is a mystery/crime novel with rich vocabulary and varied sentence structures. This makes it ideal for testing text processing, especially word frequency analysis and normalization.

## How to run
```bash
pytest -q
python -m src.project
```

## Approach
- Load text from a file
- Normalize the text (convert to lowercase, remove punctuation, clean extra spaces)
- Tokenize the text into individual words
- Count word frequencies using a dictionary
- Sort and display the top N most frequent words
- Provide an extra insight (words that appear only once)

## Complexity
### `count_words`
- Time: O(n)
- Space: O(n)
- Why: The function iterates through all words once and stores counts in a dictionary.

### `top_n_words`
- Time: O(n log n)
- Space: O(n)
- Why: Sorting the dictionary items takes O(n log n), and a new list is created.

## Edge-case checklist
- [x] empty file
- [x] punctuation-heavy input
- [x] repeated words
- [x] uppercase/lowercase differences
- [x] `n <= 0`

## Assistance & sources
- AI used? (Y)
- What it helped with: Understanding implementation structure, debugging logic, and improving test coverage.
- Other sources: Python official documentation

## Design note (150–250 words)
For this project, I selected *The Crime Code* by William Le Queux as my dataset because it is a classic crime novel with diverse vocabulary and natural language patterns. This makes it suitable for analyzing word frequencies and testing how well the program handles real-world text data.

In terms of design, I followed a pipeline-based approach: loading the text, normalizing it, tokenizing into words, counting frequencies, and finally extracting insights. I used Python's built-in data structures such as lists and dictionaries because they are efficient and easy to implement. The normalization step was important to ensure consistency by converting all text to lowercase and removing punctuation.

The easiest part of the project was implementing the word counting logic, as dictionaries provide a simple way to track frequencies. The more challenging part was handling edge cases such as empty inputs and punctuation-heavy text.

If I were to improve this project in the future, I would add more advanced features such as detecting common phrases (n-grams) or visualizing word frequency using graphs.