def my_function(prva_lista,druga_lista):
  #ispis podataka
  print("Prvi parametar: ", type(prva_lista))
  print("Drugi parametar: ", type(druga_lista))

  #rješenje
  novalista = [x if x == y else -1 for x,y in zip(prva_lista,druga_lista)]
  print(novalista)

my_function([1,2,3,4,5],[2,2,4,4,5,])
