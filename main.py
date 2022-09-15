import time

iniciar_trivia = True
intentos = 0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
VERDE = '\033[1;32m'

print(MAGENTA+"BIENVENIDOS A MI TRIVIA SOBRE FUTBOL\n"+RESET)
time.sleep(2)
print("Hablaremos de uno de los torneos mas importantes del futbol:UEFA Champions League\n")
time.sleep(1)
nombre = input("Ingresa tu nombre: ")
#Puntos
puntaje = 0
print("\nTienes", puntaje , "puntos")
time.sleep(1)
#Siguiente
print("\nBuenas",nombre,",pondremos a prueba tu conocimiento.")

print("Responde las preguntas escribiendo la letra de la alternativa y presionando ENTER para enviar tu respuesta:\n")
time.sleep(2)

while iniciar_trivia == True: 
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar\n")

  print(YELLOW+"1)¿Cual es el grupo considerado el grupo de la muerte?\n"+RESET)
  print("A)Shakhtar Donetsk,Real Madrid,RB Leipzig,Celtic")
  print("B)Atlético De Madrid,Bayer Leverkusen,Club Brugge,Porto")
  print("C)Barcelona,Bayern Munich,Inter,Viktoria Plzen")
  print("D)Dinamo Zagreb,Milan,Red Bull Salzburg,Chelsea\n")

  respuesta_1 = input(BLUE+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_1 not in ("A", "B", "C", "D","M"):
     respuesta_1 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")

  if respuesta_1 == "M":
        puntaje +=8
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_1 == "C":
        puntaje += 5
        print(GREEN+"Muy bien"+RESET , nombre , GREEN+"Sigue asi"+RESET)
  else:
   puntaje -= 5
   print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
   time.sleep(1)
    
  print("Tienes",puntaje,"puntos.\n")
  
  #SEGUNDA PREGUNTA
  time.sleep(2)
  print(YELLOW+"2) El Barcelona se enfrenta en primera ronda a:\n"+RESET)
  print("A)Real Madrid")
  print("B)Inter")
  print("C)Liverpool ")
  print("D)Viktoria Plzen\n")

  respuesta_2 = input(BLUE+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_2 not in ("A", "B", "C", "D","T"):
     respuesta_2 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "T":
        puntaje += 4
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_2 == "A":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  elif respuesta_2 == "B":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  elif respuesta_2 == "C":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  else :
   puntaje += 5
   print(GREEN+"Muy bien"+RESET , nombre , GREEN+"Sigue asi"+RESET)
   time.sleep(1)
    
  print("Tienes",puntaje,"puntos.\n")

  #TERCERA PREGUNTA

  time.sleep(2)
  print(YELLOW+"3)¿Cuál es el club con más Champions de la historia?\n"+RESET)
  print("A)Inter")
  print("B)Sevilla")
  print("C)Niza")
  print("D)Real Madrid\n")
  
  respuesta_3 = input(BLUE+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_3 not in ("A", "B", "C", "D","P"):
     respuesta_3 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "P":
        puntaje += 4
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_3 == "A":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  elif respuesta_3 == "B":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  else :
    puntaje += 5
    print(GREEN+"Muy bien"+RESET , nombre , GREEN+"Sigue asi"+RESET)
    time.sleep(1)
    
  print("Tienes",puntaje,"puntos.\n")

  time.sleep(2)
  print(YELLOW+"4)¿Quién ha perdido más finales de Champions?\n"+RESET)
  print("A)Manchester City")
  print("B)Napoli")
  print("C)Milan")
  print("D)Real Sociedad\n")

  respuesta_4 = input(BLUE+"Tu respuesta:"+RESET)
  time.sleep(3)
  while respuesta_4 not in ("A", "B", "C", "D","E"):
     respuesta_4 = input("Debes responder A, B, C o D. Ingresa nuevamente tu respuesta: ")
    
  if respuesta_4 == "E":
        puntaje += 4
        print("Ojito", nombre ,"Este es un mensaje secreto")
  elif respuesta_4 == "A":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  elif respuesta_4 == "B":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  elif respuesta_4 == "D":
        puntaje -= 5
        print(RED+"A fallado"+RESET, nombre , RED+"Lamentable"+RESET)
  else :
   puntaje += 5
   print(GREEN+"Muy bien"+RESET , nombre , GREEN+"Sigue asi"+RESET)
   time.sleep(1)
  
  print("Tienes",puntaje,"puntos.\n")

  time.sleep(2)

  if puntaje >= 0:
      print(VERDE+"\nGracias", nombre ,"!" ,"Espero que la trivia haya sido de tu agrado.","Alcanzaste", puntaje ,"puntos"+RESET)
  else :
      print(VERDE+"\nGracias", nombre ,"!" ,"Que desafortunado.","Alcanzaste", puntaje ,"puntos,intentalo para la proxima"+RESET)


  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":
    print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
    
    iniciar_trivia = False







  




              
















































  
























        







  







  












      








  



