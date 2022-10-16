def my_function(prvi_par,drugi_par):
  print("Prvi parametar: ", type(prvi_par))
  print("Drugi parametar: ", type(drugi_par))

  try:
    if type(prvi_par) == type(drugi_par):
        print ("Parametri su istog tipa")
        if type(prvi_par and drugi_par)is list:
            print("Oba parametra su liste")
            novalista=prvi_par + drugi_par
            print("Spojena lista:  ", novalista)
        elif type(prvi_par and drugi_par)is dict:
            print("Oba parametra su dictionary")
            novidict=prvi_par.copy()
            novidict.update(drugi_par)
            print(novidict)
        else: print("Parametri nisu liste ili dictionary")
  except:
    print("Parametri nisu isti tipovi")

my_function({1:2, 3:2}, {5:2, 4:1})
