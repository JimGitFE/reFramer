#!/usr/bin/env python3

# Python 3 code to rename multiple 
# files in a directory or folder
 
# importing os module
import os
 
imagesCount = 0
offset = 0

# check if output & input folders exist
def folderValidation():
    inputExist = os.path.exists("input")
    if not inputExist: os.makedirs("input")
    outputExist = os.path.exists("output")
    if not outputExist: os.makedirs("output")

# Function to rename multiple files
def main():
    global offset
    global imagesCount

    for count, filename in enumerate(os.listdir("input")):
        newPos = count + int(offset)
        dst = f"render_{str(newPos)}.jpg"
        src =f"input/{filename}"  
        dst =f"output/{dst}"
        imagesCount = count + 1
        
        # rename() function will
        # rename all the files
        os.replace(src, dst)
 


# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    folderValidation()
    print("Offset Count by x amount (default 0):")
    offset = input()
    main()
    print(f"reFramer {imagesCount} images affected")

    # Read input to keep window open
    input("exit...")