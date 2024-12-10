import os

def shut():
  os.system('shutdown /s')
def questions():
  '''Please enter 'y' for yes and 'n' for no'''
  user=input('Are you sure you want to shutdown your computer?  ')
  user=input('Have you saved all your important things?  ') 
  if user=='y':
    print('SHUTDOWN IN PROCESS!')
    shut()
  else:
    print('ABORTING SHUTDOWN!')
print(questions.__doc__)
questions()