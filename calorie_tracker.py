# Project Title : Daily Calorie Tracker CLI
# Name : Anupam Chaudhary
# Department : B.Tech. C.S.E ( AI/ML ) section-A
# Roll no. 2501730151


global meals , cal , cal_total , cal_avg , cal_limit , length 


def longest_word_len(lst):     # To return the length of the longest meal name
    word=""
    for a in lst:
        if len(word)<len(a):
            word=a
        else:
            continue
    return len(word)


def space(len1,word):          # To create appropriate space to be applied between key and value outputs while printing and writing into the file
    count = len1-len(word)
    space1=chr(32)
    gap = space1*count
    return gap


def print_entry(key,value):    # To print the given key-value pairs on the user interface
    gap = space(length,key)
    entry = key+gap+':'+value
    print(entry)
    return gap

    
def write_entry(key,value):    # To write the given key-value pairs to calorie_log.txt file
    gap = space(length,key)
    entry = '\n'+key+gap+':'+value
    f1.write(entry)

    
def save_record(date):         # To write date and other given/derived data to calorie_log.txt file
    global f1
    f1=open("Calorie_log.txt","a")
    f1.write("\nDate : "+date)
    f1.write("\n----------------")
    
    write_entry("Meal Name","Calories")
    f1.write("\n--------------------------------")
    
    for i in range(len(meals)):
        write_entry(meals[i],str(cal[i]))

    f1.write("\n--------------------------------")
    write_entry("Average",str(cal_avg))
    write_entry("Total Calories",str(cal_total))
    write_entry("Daily Limit",str(cal_limit))

    f1.write("\n_________________________________________\n               END OF DATA             \n_________________________________________")
    f1.close()


    
print("Welcome to the command line interface of our Daily Calorie Tracker.")
print("This interface is a quick and simple way to monitor your daily calorie intake.")
print("------------------------------------------------------------------------------")


meals = []
cal = []

# -------------------------------------------------------------------
# Taking meal_name and calorie inputs and adding them to their respective lists.
# -------------------------------------------------------------------

num_meals = int(input("Enter the no. of meals you want to enter for today : "))
print()
for i in range(num_meals): 
    meal_name = input("Enter meal designation ( ex: breakfast, lunch etc.) : ")
    cal_intake = float(input("Enter calorie intake : "))
    print("------------")
    meals.append(meal_name)
    cal.append(cal_intake)


cal_total = sum(cal)
cal_avg = cal_total/num_meals

# -------------------------------------------------------------------
# To create output message for user based to total calorie intake compared to daily calorie limit.
# -------------------------------------------------------------------

cal_limit = float(input("Enter your daily calorie limit : "))

if (cal_total > cal_limit): 
    cal_excess = cal_total-cal_limit
    print(f"WARNING!!! Your calorie intake excedded your daily calorie limit by {cal_excess} calories.")

elif (cal_total == cal_limit):
    print(f"GOOD JOB. You consumed exactly your daily calorie limit.")

else:
    cal_save = cal_limit-cal_total
    print(f"CONGRATULATIONS , You consumed {cal_save} less calories than your daily calorie limit.")


# -------------------------------------------------------------------
# Printing out all the given and derived data in a systematic order
# -------------------------------------------------------------------

length = longest_word_len(meals) + 4
gap = print_entry("Meal_name","Calories")
c = len(gap)+20
print("-"*c)


for i in range(num_meals):
    print_entry(meals[i],str(cal[i]))


print("-"*c)
print_entry("Average",str(cal_avg))
print("-"*c)
ask=input("Do you wish to save the report ( y/n ) : ")


# -------------------------------------------------------------------
# Asking whether to write the given and derived data in calorie_log.txt file
# -------------------------------------------------------------------

if ask.lower() == 'y':
    date = input("Enter Date ( DD-MM-YYYY ) : ")
    save_record(date)

print()
print("Thank you for using our calorie tracker module!!!")
