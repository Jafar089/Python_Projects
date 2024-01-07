# Description: This code deletes a file from the desired folder into PC.
import os

file_path = 'C:\\Users\hp\Downloads/Phase 2 - Parser.zip'

if os.path.exists(file_path):
    os.remove(file_path)
    print("File Removed!")
else:
    print("File does not exist!")



# # code to delete all files in a folder
# import shutil
# import os

# downloads_path = 'C:\\Users\\hp\\Downloads'

# for item in os.listdir(downloads_path):
#     item_path = os.path.join(downloads_path, item)

#     if os.path.isdir(item_path):
#         shutil.rmtree(item_path)
#         print(f"Folder '{item}' Removed!")

# print("All folders in Downloads directory have been removed.")
