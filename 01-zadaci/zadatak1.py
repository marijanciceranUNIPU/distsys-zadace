def stringovi():
    #podaci
    listastringova = ["Pas", "Macka", "Stol"]
    print(listastringova)
    
    #rješenje
    newlist = [x for x in listastringova if len(x)>4]
    print(newlist)

stringovi()