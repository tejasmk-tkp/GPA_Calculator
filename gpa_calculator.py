# Prompt user to enter number of subjects and total marks per subject
subjects = int(input("Enter number of subjects: "))
total = int(input("Enter total marks per subject: "))

# Initialize variables
n = 0
lst_c = [] # list to store credits
lst_cm = [] # list to store credit*grade point

# Loop to take input for each subject
for i in range(subjects):
    n += 1
    print("Subject " + str(n) + ":")
    credit = int(input("Credit: "))
    marks = float(input("Marks: "))
    if total != 100:
        marks = (marks / total) * 100
    grade_point = 0
    if 91 <= marks <= 100:
        grade_point = 10
    elif 81 <= marks <= 90:
        grade_point = 9
    elif 71 <= marks <= 80:
        grade_point = 8
    elif 61 <= marks <= 70:
        grade_point = 7
    elif 56 <= marks <= 60:
        grade_point = 6
    elif 50 <= marks <= 55:
        grade_point = 5
    elif 0 <= marks <= 49:
        grade_point = 0
    lst_c.append(credit) # add credit to the list
    lst_cm.append(credit * grade_point) # add credit*grade point to the list

# Calculate GPA by summing up credit*grade point and dividing by total credits
gpa = sum(lst_cm) / sum(lst_c)

# Print the calculated GPA
print(gpa)
