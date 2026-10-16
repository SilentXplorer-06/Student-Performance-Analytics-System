# Student Performance Analytics System

## About this project

I made this small project to practise using Python with student marks. The program reads a CSV file and works out each student's total, average, grade, and pass/fail result. It also gives a short summary of the class and shows the subjects' average marks.

The names and marks in `students.csv` are fictional examples for practice.

## How to run it in VS Code

1. Extract the ZIP file.
2. Open VS Code and choose **File → Open Folder**. Select the extracted project folder.
3. Choose **Terminal → New Terminal**.
4. Install the libraries (this is usually needed only once):

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Open `main.py` and click **Run Python File** in the top-right corner. You can also type `python main.py` in the terminal.

Keep `students.csv` in the same folder as `main.py`. When the program finishes, it saves the calculated results in `student_results.csv`.

## What the program does

- Uses **Pandas** to read the CSV data and organize it in a DataFrame.
- Calculates each student's total and average marks.
- Uses a function to assign a grade.
- Uses **NumPy** to check whether a student scored at least 35 in every subject.
- Uses NumPy arrays and functions to calculate the class average, highest and lowest averages, pass/fail counts, and subject averages.
- Uses a loop to print subject averages and lists the top three students.
- Saves the final results to a CSV file.

## Grading and pass rules

| Average mark | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80–89.99     | A     |
| 70–79.99     | B     |
| 60–69.99     | C     |
| 50–59.99     | D     |
| Below 50     | F     |

These are the rules chosen for this practice project. A student passes only if they score at least 35 marks in **every** subject.

## Files in this folder

- `main.py` — the main program and calculations.
- `students.csv` — 20 fictional student records.
- `student_results.csv` — output file created by the program.
- `requirements.txt` — lists Pandas and NumPy.
- `PROJECT_DOCUMENTATION.md` — project write-up.
## IMP NOTE ##
- The program should be run in Python 3.13 version.
