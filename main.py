"""
Assignment program using Dynamic Programming bitmasking technique
"""

# Input file name
# Data seperated by '/'
# First item in the row is the student number and further are the topics selected for the students
input_file_name = 'inputPS4.txt'

# output file to be written to
output_file = 'outputPS4.txt'

# Number of students
n = 11

# List of subjects adding in alphabetical ascending order
subjects = ['AI', 'BD', 'CC', 'DM', 'EC',
            'GM', 'IP', 'ML', 'NLP', 'SDA', 'WMC']

# 2d matrix for preferences of topics
course_matrix = []

preferences = [[0 for j in range(n)] for i in range(n)]

# Maximum value - all the bits to one
ones = (1 << n) - 1


def insert_into_matrix(student_options, student):
    """
    Insert the student record and the topics into course_matrix
    """
    # Split the given row with '/'
    student_details = student_options.split('/')
    # Trim the spaces from both sides for the strings
    # and exclude the student id
    courses_opted = [item.strip() for item in student_details[1:]]
    # Sort the courses for easier computation
    courses_opted.sort()
    course_bit_matrix = []
    # Insert the subjects into the list
    for subject in subjects:
        if subject in courses_opted:
            course_bit_matrix.append(1)  # Topic choosen by the student
        else:
            course_bit_matrix.append(0)  # Topic not choosen by the student
    # Add each student entries into the matrix
    course_matrix.append(course_bit_matrix)


def assignments(matrix, bitmask, assignment):
    """
    Method for assignment with bitmasking technique
    """

    # Base condition for ones
    if bitmask == ones:
        return 1

    # Base condition for value of n
    if assignment > n:
        return 0

    # Return if the value already computed by checking with -1
    if matrix[bitmask][assignment] != -1:
        return matrix[bitmask][assignment]

    # Get the computations of the next iteration
    combinations = assignments(matrix, bitmask, assignment+1)

    for student in range(n):
        if preferences[assignment-1][student] == 0:
            continue

        if bitmask & (1 << student):
            continue

        # Call the topic check with the next student and increasing the assignment count
        combinations += assignments(matrix, bitmask |
                                    (1 << student), assignment + 1)

    # Update the combinations to the matrix
    matrix[bitmask][assignment] = combinations

    return matrix[bitmask][assignment]


def main():
    with open(input_file_name, 'r') as input_file:
        student = 0
        for option in input_file:
            # Sample format: S1 / DM / SDA / WMC / CC
            insert_into_matrix(option, student)
        # print(course_matrix)

    for i in range(n):
        for j in range(n):
            preferences[j][i] = course_matrix[i][j]

    recursiveMatrix = [[-1 for j in range(n+1)] for i in range(2 ** n)]

    value = assignments(recursiveMatrix, 0, 1)

    # print("The total number of allocations possible is: %d" % value)
    with open(output_file, 'w') as of:
        of.write("The total number of allocations possible is: %d" % value)


if __name__ == "__main__":
    main()
