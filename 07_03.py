import os.path
import shutil
root_dir = 'my_project'
templates_dir = '/templates'
if not os.path.exists(root_dir+templates_dir):
    os.mkdir(root_dir+templates_dir)
for root, _, files in os.walk(root_dir):
    for f in files:
        if f.find(".html") > 0:
            way_file = os.path.split(root)[1]
            st_ad = f"{root}/{f}"
            if not os.path.exists(f"{root_dir+templates_dir}/{way_file}"):
                os.mkdir(f"{root_dir+templates_dir}/{way_file}")
            new_ad = f"{root_dir + templates_dir}/{way_file}/{f}"
            if os.path.realpath(st_ad) != os.path.realpath(new_ad):
                shutil.copy2(st_ad, new_ad)

