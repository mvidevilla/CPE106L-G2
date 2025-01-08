file_name = input("Enter file name: ")

try:
    with open(file_name, "r") as f:
        listFile = f.read().splitlines()
    
    while True:
        print("\nThe file has", len(listFile), "lines.")
        selection = int(input("Enter line number (or 0 to quit): "))
        if selection == 0:
            print("BaiBai:<")
            break
    
        try:
            selection = int(selection) - 1
            if 0 <= selection < len(listFile):
                print("\n", listFile[selection], "\n")
            else:
                print("Invalid line number. Pweasee try again.")
        except ValueError:
            print("Invalid input. Valid # onle.")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")