#3. Python vasitəsi ilə bir şəkli bir qovluqdan başqa qovluğa kopyalayan app yazaraq linkini qeyd edin
import os
import shutil

path_to_your_files = 'Python_final/Images'
copy_to_path = 'Python_final/Uploads'

files_list = sorted(os.listdir(path_to_your_files))
orders = range(1, len(files_list) , 4)

for order in orders:
    files = files_list[order] #3 Sekilden 1ini goturur
    shutil.copyfile(os.path.join(path_to_your_files, files), os.path.join(copy_to_path, files))  # kopyalayir diger qovluga