input_file_name = 'inputPS4.txt'

subjects = ['AI', 'BD', 'CC', 'DM',
 'EC', 'GM', 'IP', 'ML', 'NLP', 'SDA', 'WMC']

course_matrix = []

def insert_into_matrix(student_options):
    # print('student_options ', student_options)
    student_details = student_options.split('/') # Split by /
    # Trim the spaces from both sides for the strings 
    # and exclude the student id
    courses_opted = [item.strip() for item in student_details[1:]]
    # Sort the courses
    courses_opted.sort()
    # print('cousers ', courses_opted)
    course_bit_matrix = []
    # exclude the student name from the list 
    for subject in subjects:
        if subject in courses_opted:
            course_bit_matrix.append(1)
        else:
            course_bit_matrix.append(0)
    print('cpirser matrix ', course_bit_matrix)
    course_matrix.append(course_bit_matrix)

    

def main():
    with open(input_file_name, 'r') as input_file:
        for option in input_file:
            insert_into_matrix(option)
        print(course_matrix)
        
if __name__ == "__main__":
    main()

