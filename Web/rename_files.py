import os
def rename_files():
    file_list = os.listdir(r"D:\Github\prank")  # r before the folder directory is for raw string
    print(file_list)
    #saved_path = os.getcwd()
    #print("common working directory is "+saved_path)
    os.chdir(r"D:\Github\prank")
    saved_path = os.getcwd()
    print("new directory is "+saved_path)
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        rename = file_name.translate(table)
        print(rename)
        os.rename(file_name,rename)
    os.chdir(saved_path)

rename_files()