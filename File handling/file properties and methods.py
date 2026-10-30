'''
File handling
----------------------------------------------------------------------------
Need - used to store small amount of data permanently
----------------------------------------------------------------------------
Types of files - Text (.txt), Binary (Images / audio / video / csv / zip)
----------------------------------------------------------------------------
3 basic operations - open a file, perform operations, close the file

open the file using in-built function open
f=open(filename,mode) f - filepointer / cursor

in filename if the file is in other location soecify with path i.e. absolute path

close the file using close method
f.close()

Here opening and closing a file is done programatically not physically
----------------------------------------------------------------------------
7 modes

r - read
default mode
if the file is there opens and reads
if the file is not there gives FileNotFoundError

IF YOU DONT SPECIFY MODE IT IS BY DEFAULT READ MODE

w - write
if the file is the there and if there is some content as soon as you specify mode it clears the content and whatever you write later will be inserted i.e. overwrite
if the file is not there it creates and then writes

IF YOU EXECUTE WRITE OPERATION MUTIPLE TIMES ALSO DATA WILL BE PRESENT ONLY ONCE SINCE IT OVERWRITES

a - append
if the file is there id adds the content ant the end
if the file is not there it creates and then appends since main intension is to write

IF YOU EXECUTE WRITE OPERATION MUTIPLE TIMES ALSO DATA WILL BE PRESENT MULTIPLE TIMES i.e. NUMBER OF TIME YOU EXECUTE = NUMBER OF TIME DATA IS INSERTED

r+ - read and write
here 1st operation is read
hence if the file is not there it throws error
and if there is a content it does not overwrite since 1st operation is read

w+ - write and read
here 1st operation is write
hence as soon as you specify mode it clears the content and whatever you write later will be inserted i.e. overwrite later reads the content. hence if the file is not there does not throw wrror since 1st operation is write

a+ - append and read
here 1st operation is append
if the file is there id adds the content ant the end
if the file is not there it creates and then appends since main intension is to write later reads the content. hence if the file is not there does not throw wrror since 1st operation is append

TO APPEND AT A PARTICULAR POSITION USE SEEK FUNCTION

x - xclusive = dangerous

THESE ARE FOR TEXT FILES

FOR BINARY FILE JUST ADD b
rb, wb, ab, r+b, w+b, a+b, xb
-----------------------------------------------------------------------------
Properties (variable) and behaviour (methods)

name, mode, closed - variables
readable, writable - methods

f.name - return name of the file
f.mode - returns mode of the file
f.closed - returns boolean value if the file is closed or not programatically
f.readable - returns boolean value if the file is readable
f.writable - returns boolean value if the file is writable
------------------------------------------------------------------------------
writing data to file

f.write() - writes a single string of data
f.writelines() - writes a list of lines [line1, line2, line3....]

ALWAYS USE \n ELSE DATA APPEARS ON A SAME LINE
------------------------------------------------------------------------------
reading data

f.read() - read entire content
f.read(n) - reads specified number of chracters (start's from 0)

EVEN SPACES \n . EVERYTHING IS COUNTED

f.readline() - reads single line at a time
f.readlines() - reads data into a list [line1,line2,line3........]

USE end="" AS print - adds a new line AND TO HAVE NEAT DATA YOU SPECIFIED \n EXPLICITLY
-----------------------------------------------------------------------------
with statement

Automatically closes the file (programatically not physcally)
you need not write f.close() explicitly
-------------------------------------------------------------------------------
tell and seek

tell() - return current position of the filepointer (cursor) i.e. at which character position

BY DEFAULT FOR

r - filepointer is at begining
w - filepointer is at begining
a - filepointer is at end

seek() - moves the filepointer to specified character position
-----------------------------------------------------------------------------
os module 

os.path.isfile(filename) - tells if the file is present or not
----------------------------------------------------------------------------
csv module 
to work with excel data

for reading - reader
for writing - writer
for writing each row - writerow [col1,col2..........]

SIMILAR TO END USE NEWLINE=""
---------------------------------------------------------------------------
zip and unzip

saves memory
save transportation time from 1 machine to other
improve performance

zip = since you want to have some file use w mode
since you want to tell you are zipping use constant ZIP_DEFLATED
use write method to specify files to be zipped

unzip = since you to unzip use r mode
since you want to tell you want to unzip use ZIP_STORED constant

steps
1. create object of class ZipFile of zipfile module
2. zip / unzip

TO KNOW THE FILES PRESENT USE namelist

------------------------------------------------------------------------------
------------------------------------------------------------------------------
'''

'''with open("file handling.txt") as f:
    print(f"File name: {f.name}")
    print(f"File mode: {f.mode}")
    print(f"Is the file closed: {f.closed}")
    print(f"Is this a readable file?: {f.readable()}")
    print(f"Is this a writeable file?: {f.writable()}")'''

'''with open("file handling.txt", "w") as f:
    print(f"File name: {f.name}")
    print(f"File mode: {f.mode}")
    print(f"Is the file closed: {f.closed}")
    print(f"Is this a readable file?: {f.readable()}")
    print(f"Is this a writeable file?: {f.writable()}")'''

'''with open("file handling.txtx", "a") as f:
    print(f"File name: {f.name}")
    print(f"File mode: {f.mode}")
    print(f"Is the file closed: {f.closed}")
    print(f"Is this a readable file?: {f.readable()}")
    print(f"Is this a writeable file?: {f.writable()}")'''

'''with open("file handling.txt", "r+") as f:
    print(f"File name: {f.name}")
    print(f"File mode: {f.mode}")
    print(f"Is the file closed: {f.closed}")
    print(f"Is this a readable file?: {f.readable()}")
    print(f"Is this a writeable file?: {f.writable()}")'''

'''with open("file handling.txt", "w+") as f:
    print(f"File name: {f.name}")
    print(f"File mode: {f.mode}")
    print(f"Is the file closed: {f.closed}")
    print(f"Is this a readable file?: {f.readable()}")
    print(f"Is this a writeable file?: {f.writable()}")'''

'''with open("file handling.txt", "a+") as f:
    print(f"File name: {f.name}")
    print(f"File mode: {f.mode}")
    print(f"Is the file closed: {f.closed}")
    print(f"Is this a readable file?: {f.readable()}")
    print(f"Is this a writeable file?: {f.writable()}")'''
