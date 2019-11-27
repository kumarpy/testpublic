import controller

if __name__ == "__main__":
    print("Welcome to the Pupper Finder:")
    print("SELECT YOUR OPTIONS\nEnter 1 - View Puppies, 2 - Insert Puppy, 3 - Delete Puppy\n")
    oper = int(input("Enter Option Number: "))
    if oper == 1:
        inp = input("Please Enter Either Pupper ID/Name or Enter ALL: ")
        if inp == "ALL":
            opt = "ID = p.ID"
        elif inp.isnumeric():
            opt = "ID = " + inp
        else:
            opt = "NAME = '" + inp + "'"
        output = controller.view_contlr(opt)
        if output:
            print("The Puppy Is Found")
            for x in output:
                print(x)
        else:
            print("The Puppy Is Not Found")
            print(output)
    elif oper == 2:
        print("Insert New Breed details as given below,\n Name,Temperament,Coat ")
        ins_str = input("Enter Values: ")
        mod_inp = "('" + ins_str.replace(",","','") + "')"
        output = controller.ins_contlr(mod_inp)
        print(output," Breed(s) Inserted")
    elif oper == 3:
        print("Enter the Pupper ID to Adopt\n")
        del_str = input("Pupper ID: ")
        output = controller.del_contlr(del_str)
        print(output," Pupper Adopted")
    else:
        print("#### Please Enter Valid Option ####")