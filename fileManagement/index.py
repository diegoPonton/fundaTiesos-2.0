#FILE MANEGEMENT 

#THE KEY WORD FOR WORKING WITH FILES ON PYTHON IS "OPEN()"

f = open('nombres.txt', mode='r') # OPEN function creates a "file object" that its saved on 'f' variable

#BUILT IN FUNCTION OPEN RECEIVE TWO IMPORTANT PARAMETERS 

        #open('fileName','mode')

'''
    There are 4 important modes when we are working with files:

    "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    "a" - Append - Opens a file for appending, creates the file if it does not exist

    "w" - Write - Opens a file for writing, creates the file if it does not exist
'''

names = f.readlines()

newList = list(map(lambda name: name.strip('\n'), names))

print(newList)