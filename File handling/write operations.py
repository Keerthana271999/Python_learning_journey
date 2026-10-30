'''with open("file handling.txt", "w") as f:
    f.write("File handling\n")
    f.write("------------------------------------------------------------\n\n")

    data = ["Need - used to store small amount of data permanently\n\n", "Types of files - Text (.txt), Binary (Images / audio / video / csv / zip)\n\n", "3 basic operations - open a file, perform operations, close the file\n\n", "open the file using in-built function open\n\n",
            "f=open(filename,mode) f - filepointer / cursor\n\n", "in filename if the file is in other location soecify with path i.e. absolute path\n\n", "close the file using close method\n\n", "f.close()\n\n", "Here opening and closing a file is done programatically not physically\n"]

    f.writelines(data)'''

# USER INPUT TO WRITE DATA

'''file = input("Enter file name: ")
with open(f"D:\\AI Engineer\\Python\\Navin reddy\\File handling\\{file}", "w") as f1:
    data = input("Enter some data: ")
    f1.write(data)

    # Your issue is that after f1.write(data), the file cursor is at the end of the file. So f1.read() finds no more data to read. - if you write read below code as nested
with open(f"D:\\AI Engineer\\Python\\Navin reddy\\File handling\\{file}", "r") as f2:
    print(f"Data present: {f2.read()}")'''
