grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
a_grade = sum(grades[0])/len(grades[0])
b_grade = sum(grades[1])/len(grades[1])
j_grade = sum(grades[2])/len(grades[2])
k_grade = sum(grades[3])/len(grades[3])
s_grade = sum(grades[4])/len(grades[4])
average_grades = {students[0]: a_grade,
                  students[1]: b_grade,
                  students[2]: j_grade,
                  students[3]: k_grade,
                  students[4]: s_grade}
print(average_grades)