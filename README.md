# 🥗 Daily Calorie Tracker (CLI)

**Author:** Anupam Chaudhary  
**Department:** B.Tech. C.S.E (AI/ML) Section-A  
**Roll No:** 2501730151  

---

## 📘 Overview

The **Daily Calorie Tracker CLI** is a Python-based command-line interface that helps users record and monitor their daily calorie intake.  
It allows you to:
- Log multiple meals with their respective calorie counts  
- Calculate total and average calorie consumption  
- Compare your intake against a self-defined daily calorie limit  
- Save the results to a text file (`Calorie_log.txt`) for record-keeping  

---

## ⚙️ Features

✅ Accepts user input for any number of meals  
✅ Displays a neatly formatted summary table  
✅ Calculates and reports whether you exceeded or stayed within your calorie limit  
✅ Option to save your data into a log file with date and summary details  
✅ Automatically aligns text output for better readability  

---

## 🧩 Functions Used

| Function Name | Purpose |
|----------------|----------|
| `longest_word_len(lst)` | Finds the length of the longest meal name (for spacing and alignment). |
| `space(len1, word)` | Generates spacing for neat output formatting. |
| `print_entry(key, value)` | Prints key–value pairs in a formatted way. |
| `write_entry(key, value)` | Writes formatted key–value pairs into the file. |
| `save_record(date)` | Saves all the entered and calculated data into `Calorie_log.txt`. |

---

## 🧮 Variables Used

| Variable | Description |
|-----------|-------------|
| `meals` | Stores the list of meal names entered by the user. |
| `cal` | Stores corresponding calorie values for each meal. |
| `cal_total` | Sum of all calorie intakes. |
| `cal_avg` | Average calorie intake per meal. |
| `cal_limit` | User-defined daily calorie limit. |
| `length` | Used for formatting and alignment in printed output. |

---

## 💻 How to Run

1. Make sure you have **Python 3.x** installed.  
2. Save the file as `daily_calorie_tracker.py`.  
3. Open the terminal or command prompt in the same directory.  
4. Run the program using:

   ```bash
   python daily_calorie_tracker.py
   ```

5. Follow the on-screen prompts to:
   - Enter the number of meals  
   - Provide each meal’s name and calorie count  
   - Set your daily calorie limit  
   - Choose whether to save the report  

---

## 🗂️ Output Example

**Sample Console Output:**
```
Welcome to the command line interface of our Daily Calorie Tracker.
Enter the no. of meals you want to enter for today : 3

Enter meal designation ( ex: breakfast, lunch etc.) : breakfast
Enter calorie intake : 400
------------
Enter meal designation ( ex: breakfast, lunch etc.) : lunch
Enter calorie intake : 600
------------
Enter meal designation ( ex: breakfast, lunch etc.) : dinner
Enter calorie intake : 500
------------

Enter your daily calorie limit : 1600
CONGRATULATIONS , You consumed 100.0 less calories than your daily calorie limit.

Meal_name   :Calories
----------------------------------------
breakfast   :400.0
lunch       :600.0
dinner      :500.0
----------------------------------------
Average     :500.0
----------------------------------------
Do you wish to save the report ( y/n ) : y
Enter Date ( DD-MM-YYYY ) : 12-11-2025

Thank you for using our calorie tracker module!!!
```

---

## 🧾 Sample Log File (`Calorie_log.txt`)

```
Date : 12-11-2025
----------------
Meal Name :Calories
--------------------------------
breakfast :400.0
lunch     :600.0
dinner    :500.0
--------------------------------
Average :500.0
Total Calories :1500.0
Daily Limit :1600.0
_________________________________________
               END OF DATA             
_________________________________________
```

---

## 🚀 Future Enhancements

- Add automatic date and time logging  
- Include BMI-based calorie suggestions  
- Enable deletion or editing of past records  
- Add colorized CLI output for better user experience  

---

## 🧑‍💻 Author Info

**Name:** Anupam Chaudhary  
