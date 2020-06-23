import os

path = "/home/daniel/Downloads"
files = os.listdir(path)

def sorter ():
    for file in files:
        original_file_name, file_ext = (os.path.splitext(file))
        #print(file_ext)
        if file_ext == "":
            pass
        elif file_ext == ".jpeg" or file_ext == ".png" or file_ext == ".webp":
            os.rename("/home/daniel/Downloads/"+file,"/home/daniel/Pictures/" + file)
        elif file_ext == ".whl":
            os.rename("/home/daniel/Downloads/"+file,"/home/daniel/Documents/" + file)
        elif file_ext == ".pdf":
            os.rename("/home/daniel/Downloads/"+file,"/home/daniel/Documents/PDF/" + file)
        elif file_ext == ".py":
            os.rename("/home/daniel/Downloads/"+file,"/home/daniel/Documents/Projects/" + file)
        else:
            print("{} is not in my database, please add it to my code and assign a folder to sort it into".format(file_ext))
        

sorter()

