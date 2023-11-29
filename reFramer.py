#!/usr/bin/env python3

# Python 3 code to rename multiple 
# files in a directory or folder
 
# importing os module
import os
 
imagesCount = 0

# check if output & input folders exist
def folderValidation():
    inputExist = os.path.exists("input")
    if not inputExist: os.makedirs("input")
    outputExist = os.path.exists("output")
    if not outputExist: os.makedirs("output")

# Function to rename multiple files
def main():
    global imagesCount
    
    for count, filename in enumerate(os.listdir("input")):
        dst = f"render_{str(count)}.jpg"
        src =f"input/{filename}"  
        dst =f"output/{dst}"
        imagesCount = count
        
        # rename() function will
        # rename all the files
        os.rename(src, dst)
 


# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    folderValidation()
    main()
    print(f"reFramer {imagesCount} images affected")