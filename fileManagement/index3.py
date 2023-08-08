# FILEMANEGEMENT: WRITTING

#           WRITE() FUNCTION

'''

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content


'''



f = open("nombres.txt", "a")

f.write("Now the file has more content!" + '\n')     # WRITE FUNCTION LET US TO WRITE TEXT ON THE FILE
                                                     # IF THE FILE IS ON MODE:
                                                            # w: the file its overwritten
                                                            # a: the info its added to the file

f.close()