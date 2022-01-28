import os
with open('conf.yaml', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if line[:-1].find('.')<0:
            if not os.path.exists(line[:-1]):
                os.mkdir(line[:-1])
        else:
            with open(line[:-1], 'w', encoding='utf-8') as q:
                pass
