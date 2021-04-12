def swapFileData():
    a=input("Enter the file: ")
    b=input("Enter second file: ")
    file=open(a,"r")
    file2=open(b,"r")
    file.write(data_b)
    file2.write(data_a)
    print("First file: "+ file)
    print("Second file: "+ file2)

swapFileData()