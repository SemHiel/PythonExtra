import os
root_path = 'D:\MediaCollege\PythonExtra\mkdir'

folders = ['Enrico', 'Amber', 'Damian', 'Geal', 'Aki', 'Rapael', 'Robin', 'Sem', 'Finn', 'Guido']

for folder in folders:

    os.mkdir(os.path.join(root_path, folder))
