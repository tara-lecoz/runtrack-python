def hauteurparcourue(nb, h) :  
    print(f"Pour {nb} marches de {h} cm, il parcourt {nb*h*2*5*7/100.0:.2f}m par semaine") 
   
nb_marches = int(input("Nombre de marches : "))  
h_marche = int(input("Hauteur d'une marche(cm) : "))  
  
hauteurparcourue(nb_marches, h_marche)