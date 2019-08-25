input_file_name = 'inputPS4.txt'

n = 11

subjects = ['AI', 'BD', 'CC', 'DM','EC', 'GM', 'IP', 'ML', 'NLP', 'SDA', 'WMC']

course_matrix = []

preferences = [[0 for j in range(n)] for i in range(n)]

ones = (1 << n) - 1  

 

def insert_into_matrix(student_options, student):
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
    course_matrix.append(course_bit_matrix)
    
    
    

   
def assignments(matrix, bitmask, assignment):
    if bitmask == ones:
        return 1
    
    if assignment > n:
        return 0
    
    if matrix[bitmask][assignment] != -1:
        return matrix[bitmask][assignment]
    
    combinations = assignments(matrix,bitmask,assignment+1)
    
    for student in range(n):
        if preferences[assignment-1][student] == 0:
            continue
        
        if bitmask & (1 << student):
            continue
        
        combinations += assignments(matrix,bitmask | (1<< student),assignment + 1)
        
    matrix[bitmask][assignment] = combinations
    
    return matrix[bitmask][assignment]


        
    

def main():
    with open(input_file_name, 'r') as input_file:
        student = 0;
        for option in input_file:
            insert_into_matrix(option,student)
        print(course_matrix)
        

    for i in range(n):
        for j in range(n):
            preferences[j][i] = course_matrix[i][j]

    recursiveMatrix = [[-1 for j in range(n+1)] for i in range(2 ** n)]
            
    value = assignments(recursiveMatrix, 0, 1)
    
    print(value)
        
if __name__ == "__main__":
    main()

