

from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

# Instatiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Set grades achieved so far
my_grades.quiz_1 = 0.78 # Received 78% in the first quiz

# Print out the grades to console
print(my_grades)

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
    min_avg_points = GradeCalculator.get_min_avg_point_for_A_grade(my_grades, weights)
    if min_avg_points is None:
        print("Can't get A in class")
    else:
        print("He has to get {} of min_points from all yet ungraded assignments to get A in class".
              format(min_avg_points))
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

# Calculate the grade assuming that all assignmets not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}')

