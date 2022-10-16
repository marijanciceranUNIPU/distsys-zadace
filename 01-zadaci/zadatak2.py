#probano

def my_function(prvi_par,drugi_par):
  print("Prvi parametar: ", type(prvi_par))
  print("Drugi parametar: ", type(drugi_par))

  if (type(prvi_par)== list) and (type(drugi_par)== dict):
    if len(prvi_par)==len(drugi_par):
        print("Parametri imaju isti broj elemenata")
        if all([isinstance(item, int) for item in prvi_par]):
            print("Svi elementi liste su tipa integer")
        else: print("Nisu svi parametri liste tipa integer")
    else: print("Parametri nemaju isti broj elemenata")
  else: print("Jedni od parametra nisu lista ili dictionary")

my_function([8,7,1], {1:2,2:1,3:2})

"""
# Creating an empty dict
myDict = dict()
  
# Creating a list
valList = ['1', '2', '3']
  
# Iterating the elements in list
for val in valList:
    for ele in range(int(val), int(val) + 2): 
        myDict.setdefault(ele, []).append(val)
  
print(myDict)
"""
