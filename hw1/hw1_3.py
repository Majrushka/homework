# Задание 3

# вывести имена и фамилии студентов с посещаемостью ниже 75%

students = [
    ("Иван", "Петров", [4,5,5,4], [3,4,5,3], 0.9),
    ("Мария", "Иванова", [5,5,5,5], [5,5,4,5], 0.95),
    ("Алексей", "Сидоров", [3,4,3,3], [4,3,4,4], 0.7),
    ("Елена", "Козлова", [5,4,5,5], [4,5,5,5], 0.85),
    ("Дмитрий", "Смирнов", [2,3,2,3], [3,2,2,3], 0.5)
]

# "Name", "Surname", "Python_marks", "Math_marks", "addendance"

print("Студент(ы) с посещаемостью ниже 0.75:")
for name, surname, python_marks, math_marks, attendance in students:
 if attendance < 0.75:
  print(f'{name} {surname}')


# вывести имя и фамилию студента с самым высоким средним баллом по обоим предметам

max_average = 0
best_student = None

for name, surname, python_marks, math_marks, attendance in students:
 average = float(sum(python_marks + math_marks) / len(python_marks + math_marks))
 # print(average)
 if average > max_average:
   max_average = average
   full_name = f"{name} {surname}"
   best_student = full_name

print(f"Студент с самым высоким средним баллом по обоим предметам: {best_student}") 


# вывести сообщение студенту, если его средний балл по Пайтон ниже, чем по математике


for name, surname, python_marks, math_marks, attendance in students:
 py_average = float(sum(python_marks) / len(python_marks))
 math_average = float(sum(math_marks) / len(math_marks))
 # print(float(py_average))
 # print(float(math_average))
 
 if py_average < math_average:
  print(f"{name} {surname}, нужно уделить больше внимания Python!")
