import os, os.path
import shutil

base_path = r'ENTER_PATH_HERE'
FOLDER_NAME = "\\data_sources\\"
parent_dir = base_path + FOLDER_NAME

# Loop through all folders in base directory
for folder in os.listdir(base_path):
    if os.path.isdir(os.path.join(base_path, folder)):      
        csv_folder = base_path + folder + "\\"      # backslash is escaped

        # Loop through all files in folders
        for file in os.listdir(csv_folder):
            ### Moving files
            # INFO: Moving files takes significantly less time than copying files
            os.makedirs(os.path.dirname(parent_dir), exist_ok=True)
            shutil.move(csv_folder+file, parent_dir+file)

##            ### Copying files
##            # If file size is greater than ~100MB, skip it
##            MAX_FILE_SIZE = 100000000
##            physical_file = os.path.join(csv_folder, file)
##            statinfo = os.stat(physical_file)
##            print(statinfo)            
##            if statinfo.st_size > MAX_FILE_SIZE:
##                print(file, statinfo.st_size)
##                continue
##            else:
##                shutil.copy2(csv_folder+file, parent_dir+file)
