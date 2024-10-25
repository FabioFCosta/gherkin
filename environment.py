import os
from openpyxl import Workbook
from steps.steps import students

def before_all(context):
  context.excel_file = os.path.join(os.getcwd(), 'results.xlsx')
  context.workbook = Workbook()
  context.sheet = context.workbook.active
  context.sheet.title = "Test Note Average Results"

  context.sheet.append(["Student", "Discipline", "Note 1", "Note 2", "Average", "Absents", "Situation"])

def after_scenario(context, scenario):
  student_login = context.student_login if hasattr(context, 'student_login') else 'N/A'
  discipline = students[context.student_login]["discipline"] if context.student_login in students else 'N/A'
  av1 = students[context.student_login]["av1_note"] if context.student_login in students else 'N/A'
  av2 = students[context.student_login]["av2_note"] if context.student_login in students else 'N/A'
  absents = students[context.student_login]["absents"] if context.student_login in students else 'N/A'
  average = context.calculated_average if hasattr(context, 'calculated_average') else 'N/A'
  situation = 'N/A'
  if hasattr(context, 'calculated_average'):
        max_absences = students[context.student_login]["schedule_hours"] * 0.25
  if average >= 6 and absents <= max_absences:
      situation = "approved"
  elif absents > max_absences:
      situation = "repproved by frequency"
  else:
      situation = "repproved by note"

  context.sheet.append([student_login, discipline, av1, av2, average, absents, situation])

def after_all(context):
  context.workbook.save(context.excel_file)