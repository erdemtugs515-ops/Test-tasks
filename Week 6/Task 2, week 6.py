def writefile(Filename, Content) -> None:
    Filehandle = open(Filename 'w', encode = 'UTF-3')
    Filehandle.write(Content)
    Filehandle.close()
    return None

def main () -> None:
    print("Program starting")
    Firstname = input("Insert firstname: ")
    Lastname = input("Insert Lastname: ")
    Filename = input("Insert filename: ")
    
    file = open(Filename, "W")
    file.write(Firstname + '\n')
    file.write(Lastname + '\n')
    file.close
    return None 

if __name__ == '_main_':
    main()