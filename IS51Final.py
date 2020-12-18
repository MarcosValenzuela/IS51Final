"""
This program will read be able to find the number of grades, the average grade, and the percentage above
average grade from a text file

It will calll a function called class_avg in which it will
open a file then it will sum the amount of grades in the file
sum the grades then will find the class average
it will print out the amount of grades and the class average
then it will close the file

It then will find the percentage average that is above the class average
to do this it will open a text file
it will then check each grade to comapre to the class average
if the grade is above the class average it will count it 
after it check all the grades it will then find the percentage above class average
then it will display the percentage above class average
then it will close the file
"""

"""
main():
    class_avg(txt_file)
    calculate_percentage_above_average(txt_file, average)

class_avg(txt_file):
    total = 0
    number of grades = 0
    average = 0

    read .txt file

    go by line in .txt file
    total = sum of each grade
    number_of_grades = each time you read a line in txt file
    average = toatl/number_of_grades

    print number_of_grades
    print average

    close file

    return average

calculate_percent_above_average(txt_file, average):
    average_grade = average
    students_above_average = 0
    total_students = 0

    read .txt file

    go line by line in .txt file
        count student
        if student_grade > average_grade
            students_above_average += 1
        percentage_above_average = (students_above_average/total_students)*100

    print percentage_above_average

    close file

    return percentage_above_average

main()
"""