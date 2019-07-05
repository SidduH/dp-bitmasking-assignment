"""
ASSUMPTIONS:
1. from promptsPS4.txt file, the data for course to offer is --> courseOffer: 3.5 : 4:0
but considered it as --> courseOffer: 3.5 : 4.0
2. New Course List considering the Current year as 2014
"""



hash_array =None
input_file_name = 'inputPS4.txt'
prompts_file_name = 'promptsPS4.txt'
output_file = 'outputPS4.txt'
current_year = 2014

def initializeHash():
    """
    Initialize the hash
    """
    global hash_array
    hash_array = {}

def insertStudentRec(StudentHashRecords, studentId, CGPA):
    StudentHashRecords[studentId]=float(CGPA)

def hallOfFame(StudentHashRecords, CGPA): 
    # print(StudentHashRecords)

    hof_students = [data for data in StudentHashRecords.items() if data[1]>=CGPA]
    # print('hof students', hof_students)
    with open(output_file, 'w+') as of:
        of.write('---------- hall of fame ----------\n')
        of.write('Input: %s\n'% str(CGPA) )
        of.write('Total eligible students: %d\n'% len(hof_students) )
        of.write('Qualified students:\n')
        for each_hof_student in hof_students:
            hof_student_id = each_hof_student[0]
            hof_cgpa = each_hof_student[1]
            of.write('%s / %s\n'% (hof_student_id, str(hof_cgpa)))
        of.write('\n')

def newCourseList(StudentHashRecords, CGPAFrom, CPGATo): 
    # print('current year', current_year)
    eligible_students = [data for data in StudentHashRecords.items() \
        if (int(data[0][:4])+4)>=(current_year-5)]
    
    qualified_students = [data for data in eligible_students \
        if (data[1]>=CGPAFrom and data[1]<=CPGATo)]
    # print('eligible canditates ', eligible_students, qualified_students)
    with open(output_file, 'a+') as of:
        of.write('---------- new course candidates ----------\n')
        of.write('Input: %s to %s'% (str(CGPAFrom), str(CPGATo)) )
        of.write('Total eligible students: %d\n'% len(qualified_students) )
        of.write('Qualified students:\n')
        for qualified_student in qualified_students:
            qual_student_id = qualified_student[0]
            qual_cgpa = qualified_student[1]
            of.write('%s / %s\n'% (qual_student_id, str(qual_cgpa)))
        of.write('\n')

def depAvg(StudentHashRecords): 
    pass# TODO:

def main():
    print('Hash before initialize ::', hash_array)
    initializeHash()
    print('After inititalizing the array',hash_array)

    # Insert students records
    with open(input_file_name, 'r') as input_file:
        records = input_file.readlines()
        for each_record in records:
            # print('each_record record', each_record)
            student_id = each_record.split('/')[0].strip() # Getting student ID
            cgpa = each_record.split('/')[1].strip()  # Getting student CGPA
            # print(student_id, cgpa)
            insertStudentRec(hash_array, student_id, cgpa)
            # print(hash_array)

    with open(prompts_file_name, 'r') as input_file:
        records = input_file.readlines()
        for each_record in records:
            header = each_record.split(':')[0].strip()
            # Insert Hall Of Fame records
            if header=='hallOfFame':
                cutoff_cgpa = each_record.split(':')[1].strip()
                cutoff_cgpa = float(cutoff_cgpa)
                # print('cutoff ', cutoff_cgpa, type(cutoff_cgpa))
                hallOfFame(hash_array, cutoff_cgpa)
            # Insert Course Offer records
            elif header=='courseOffer':
                cgpa_ranges = each_record.split(':')[1:]
                cgpa_from =float(cgpa_ranges[0].strip())
                cgpa_to =float(cgpa_ranges[1].strip())
                # print('cgpa ranges ', cgpa_from, cgpa_to)
                newCourseList(hash_array, cgpa_from, cgpa_to)
    
    depAvg(hash_array)

if __name__ == "__main__":
    main()

