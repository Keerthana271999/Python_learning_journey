from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED

# zipping
'''zip = ZipFile("File handling.zip", "w", ZIP_DEFLATED)
zip.write("binary files.py")
zip.write("binary files.py")
zip.write("csv files.py")
zip.write("data copying.py")
zip.write("lord Ganesha.jpg")
zip.write("lord Ganesha copy.jpg")
zip.write("os module.py")
zip.close()'''

'''unzip = ZipFile("File handling.zip", "r", ZIP_STORED)
# print(unzip.namelist())'''

'''files = unzip.namelist()
for file in files:
    if file.endswith(".py"):
        with open(file) as f:
            print(f.read())
    else:
        print("Not a readable file")'''

'''unzip.extractall()'''
