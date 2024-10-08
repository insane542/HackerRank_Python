"""
Task:
Given the names and grades for each student in a class of N students, store them in a nested list.
Print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example:
records = [["chi",20.0],["beta",50.0],["alpha","50.0"]]
The ordered list of scores is [[20.0,50.0]], so the second lowest score is 50. 
There are two students with that score: ["beta","alpha"]. Ordered alphabetically, the names are printed as: 

alpha
beta

Input Format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints:
* 2<=N<=5
* There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0:
Berry
Harry

Explanation 0:
There are 5 students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina. 
The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        records.append([name, grade])

    unique_grades = sorted(set([record[1] for record in records]))

    second_lowest_grade = unique_grades[1]

    second_lowest_students = []
    for record in records:
        if record[1] == second_lowest_grade:
            second_lowest_students.append(record[0])

    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)