#Reading Data from the File.
def main():
    try:
        ReadFile=open("x.txt","r")
        for line in ReadFile:
            print(line)
        ReadFile.close()
    except IOError:
        print("File not found")
    print("app is done")
if __name__ == '__main__':main()
