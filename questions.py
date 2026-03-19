import string
import random
puntos=0 # dependiendo la palabra que ingrese el usuario se le restaran o sumaran puntos 

menu={
    "lenguajes":["python"],
    "conceptos_basicos":['bucle','variable','programa','funcion'],
    "tipos_datos":['entero','lista','cadena']
} #cree el diccionario solicitado 

print('categorias: ')
for categoria in menu:
           print(categoria, '-')

cat=input('ingresa la categoria elegida: ')

if cat in menu:
    print('la categoria es:',cat)
    for pal in menu[cat]:
        print(pal)
else: print('categoria no valida')


word = random.sample(menu[cat],1)[0] #usando random.sample debo mandarle la coleccion, cuantos elem quiero de esa coleccion y agregar [0] para sacar a ese elem de la lista, ya que esta funcion devuelve una lista y no un string como necesitamos 
guessed = []
attempts = 6

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += " _ "
    print(progress)
# Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
      print("¡Ganaste!")
      puntos+= 6
      break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")


    cadena=string.ascii_lowercase
    letter = input("Ingresá una letra: ")

    if (letter not in cadena or len(letter)!=1): # modificacion por si ingresa un char invalido o mas de uno 
        print('entrada no valida')
        continue
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntos -= 1
        print("Esa letra no está en la palabra.")

    print()

else:
    puntos=0
    print(f"¡Perdiste! La palabra era: {word}")

print('puntos ganados: ',(puntos)) 