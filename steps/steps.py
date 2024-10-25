from behave import given, when, then

students = {}

@given("the student {student_login}")
def set_student(context, student_login):
  context.student_login = student_login
  if student_login not in students:
    students[student_login] = {"login": student_login}
  print(f"Student set: {student_login}")

@given("the discipline {discipline_cod}")
def set_discipline(context, discipline_cod):
  students[context.student_login]["discipline"] = discipline_cod
  print(f"Discipline set: {discipline_cod}")

@given("discipline schedule with {ds} hours")
def set_schedule(context, ds):
  students[context.student_login]["schedule_hours"] = int(ds)
  print(f"Schedule hours set: {ds}")

@when("the user informs the avaliation 1 note equals to {av1_note}")
def set_av1(context, av1_note):
  students[context.student_login]["av1_note"] = float(av1_note)
  print(f"Avaliation 1 set: {av1_note}")

@when("the avaliation 2 note equals to {av2_note}")
def set_av2(context, av2_note):
  students[context.student_login]["av2_note"] = float(av2_note)
  print(f"Avaliation 2 set: {av2_note}")

@when("the student has {absents} classes absents")
def set_absents(context, absents):
  students[context.student_login]["absents"] = int(absents)
  print(f"Absents set: {absents}")

@then("the system calculates the student's average")
def calculate_average(context):
  student = students[context.student_login]
  average = (student["av1_note"] + student["av2_note"]) / 2
  print(f"Student average calculated: {average}")
  context.calculated_average = average

@then("determines the student situation: {expected_situation}")
def check_situation(context, expected_situation):
  student = students[context.student_login]
  average = context.calculated_average
  max_absences = int(student["schedule_hours"] * 0.25)
  
  if average >=6 and student["absents"]<=max_absences:
    situation = 'approved'
  elif student["absents"] > max_absences:
    situation = "repproved by frequency"
  else:
    situation = "repproved by note"

  assert situation == expected_situation, f"Expected {expected_situation}, got {situation}"

  print(f"Student situation: {situation}")