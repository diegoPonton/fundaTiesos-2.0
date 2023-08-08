# FILEMANEGEMENT: READING


#           READ() FUNCTION

f = open('nombres.txt', mode='r+')

print(f.read())        # read() function let us to obtain all the file


f.close()          # always close file its a good programming practice :D


#           READLINES() FUNCTION

f = open('nombres.txt', mode='r+')

print(f.readlines())

f.close()


#           READLINE() FUNCTION


f = open('nombres.txt', mode='r+')          #You can return one line by using the readline() method:

print(f.readline())

f.close()




