from random import randint
import os

VIDA_INICIAL_PIKACHU = 100
VIDA_INICIAL_SQUIRTLE = 100

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

#Se desenvuelven los turnos de combate

#Turno pikachu
print("Turno de Pikachu")
if randint(1, 2) == 1:
    print("Pikachu ataca con Onda Trueno")
    vida_squirtle -= 15
else:
    print("Pikachu ataca con Impactrueno")
    vida_squirtle -= 20

if vida_squirtle < 0:
    vida_squirtle = 0

if vida_pikachu < 0:
    vida_pikachu = 0

barra_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
print("Pikachu:          [{}{}][{}/{}]".format("*" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu),
                                               vida_pikachu, VIDA_INICIAL_PIKACHU))

barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
print("Squirtle:          [{}{}][{}/{}]".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle),
                                                    vida_squirtle, VIDA_INICIAL_SQUIRTLE))

input("Enter para continuar...\n\n")
os.system("cls")

#Turno de pikachu
print("Turno de Squirtle")
ataque_squirtle = None

while ataque_squirtle not in ["P", "N", "A", "B"]:
    ataque_squirtle = input("Que ataque deseas realizar: [P]lacaje, Pistola de [A]gua, [B]urbuja: \n"
                            "Prefiero [N]o atacar")
if ataque_squirtle == "N":
       print("Una lastima que no decidas atacar. Fin del juego")
       exit()
if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 13
elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de Agua")
        vida_pikachu -= 15
else:
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 20

if vida_squirtle < 0:
        vida_squirtle = 0

if vida_pikachu < 0:
    vida_pikachu = 0
    barra_vida_pikachu = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:          [{}{}][{}/{}]".format("*" * barra_vida_pikachu, " " * (10 - barra_vida_pikachu),
                                                   vida_pikachu, VIDA_INICIAL_PIKACHU))

barra_vida_squirtle = int(vida_squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
print("Squirtle:          [{}{}][{}/{}]".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle),
                                                vida_squirtle, VIDA_INICIAL_SQUIRTLE))

input("Enter para continuar...\n\n")
os.system("cls")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana!!")
else:
    print("Squirtle gana!!")

