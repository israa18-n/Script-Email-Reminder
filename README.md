
This is a simple Python script that sends automated email reminders based on data provided in a `.csv` file. It's ideal for managing daily tasks, follow-ups, or reminders using Gmail and Python.

- Sends personalized email reminders via Gmail
- Reads reminders from a CSV file
- Matches reminders to the current date
- Simple, customizable, and beginner-friendly
- No need for external libraries like `pandas`

The script reads data from a `reminders` file with the following format:

```csv
email,subject,body,date
example1@gmail.com,Meeting,"Don't forget the 10AM meeting",2025-06-29
example2@gmail.com,Report,"Please submit the final report",2025-06-30
