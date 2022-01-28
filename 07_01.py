import os
dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists('my_project'):
    os.mkdir('my_project')
for name in dirs:
    if not os.path.exists(f'my_project/{name}'):
        os.mkdir(f'my_project/{name}')