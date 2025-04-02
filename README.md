# CrediMate

## Description
This Python program allows you to input student credit data in three categories: PASS, DEFER, and FAIL. Based on the input, each student is classified into one of four categories: Progress, Progress (Module Trailer), Exclude, or Do Not Progress (Module Retriever). It also provides a **histogram visualization** of the results and saves the final classification data into a file called note.txt.

### Features
- Valid Input Checking: Ensures the entered credits for each category are valid (0, 20, 40, 60, 80, 100, 120).
- Student Classification: Classifies students into:
   -Progress (120 credits in PASS)
   -Progress (Module Trailer) (100 credits in PASS)
   -Exclude (80 or more credits in FAIL)
   -Do Not Progress (Module Retriever) (Other cases)
- Histogram Display: A graphical representation of the classification results (using graphics.py).
- Results Saving: Saves final results in a note.txt file (creates the file if it doesn't exist).

### Prerequisites
- Python 3.x
- graphics.py library (used for graphical visualization)

### File Structure
- **src/main.py** → The main Python script that runs the program.
- **src/graphics.py** → The external graphics library used to render the histogram.
- **note.txt** → This is an Auto-generated file that stores the classification results.
