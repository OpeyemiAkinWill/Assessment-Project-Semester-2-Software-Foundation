
# Python_Assessment_Semestr 2_Project_May_2025

#try:
import utils_082025

#except ModuleNotFoundError:
       #print("Error : Make sure module file exists")


# import the python built-in csv module
import csv


# initializing the students list
students = []  


try:
        # reading csv file
        with open('Students.csv', 'r') as file:
                # creating a csv reader object
                reader = csv.reader(file)

                # Read the header (first row)
                header = next(reader)
               
                # extracting field names through first row
                for row in reader:
                       
                        #data elements extracted from the row
                        Name,Accounting,BusinessAdministrative,Economics,HealthSocialCare = row
                       
                        #calculate the average score
                        average = utils_082025.calculate_average(
                                [int(Accounting), int(BusinessAdministrative), int(Economics), int(HealthSocialCare)])
                       
                        #assign the grade
                        grade = utils_082025.assign_grade(average)
               
                        #append the data into the list
                        students.append ([Name, Accounting, BusinessAdministrative, HealthSocialCare, average, grade])

except FileNotFoundError:
        # Handle case when the file is not found
        print(f"Error: Students.csv not found.")

#write the data into a new file
with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Accounting', 'BusinessAdministrative', 'Economics','HealthSocialCare', 'Average', 'Grade'])
        writer.writerows(students)

print('Results saved to student_results.csv')

