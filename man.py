DataType = input("Enter a number/word (string) >> ") #Write your datatype (Integer,Float-point,Boolean(True or False),String)
                

if DataType.isdigit:
    print("The DataType you wrote is", DataType) #Tell the user what is the DataType
print("The DataType is", type(DataType), "Remember int means integer, str means string, bool means boolean (True, False)")
