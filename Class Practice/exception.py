# Exception handling in Files
'''
try:
    print(b)
except:
    print("its an Example of Exception")
    '''

try:
    with open("Not_file.txt","r") as f:
        content =f.read()
        print(content)
except FileNotFoundError:
    print("Error : file does not exits")
except IOError:
    print("error :- File io error")

finally:
    print("file operations attemped")



