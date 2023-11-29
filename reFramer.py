# Python 3 code to rename multiple 
# files in a directory or folder
 
# importing os module
import os
 
imagesCount = 0

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
    main()
    print(f"reFramer {imagesCount} images affected")