import controller

if __name__ == "__main__":
    print("Welcome to the Pupper Finder:")
    inp = input("Please Enter Either Pupper ID/Name or Enter ALL: ")
    if inp == "ALL":
        opt = "ID = p.ID"
    elif inp.isnumeric():
        opt = "ID = " + inp
    else:
        opt = "NAME = '" + inp + "'"
    output = controller.sort_out(opt)
    if output:
        print("The Puppy Is Found")
        for x in output:
            print(x)
    else:
        print("The Puppy Is Not Found")
        print(output)