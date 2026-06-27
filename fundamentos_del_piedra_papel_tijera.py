import random

print("====================================")
print("¡Bienvenido a Piedra, Papel o Tijera!")
print("====================================")

# 1. El usuario elige su opción
usuario = input("Elige una opción (piedra, papel, tijera): ").lower()

# 2. La computadora elige su opción al azar
opciones = ["piedra", "papel", "tijera"]
computadora = random.choice(opciones)

print(s"Tú elegiste: {usuario}")
print(f"La computadora eligió: {computadora}")
print("------------------------------------")

# 3. Determinar el ganador usando condicionales
if usuario == computadora:
    print("¡Es un empate! 🤝")

elif usuario == "piedra":
    if computadora == "tijera":
        print("¡Ganaste! La piedra rompe la tijera. 🎉")
    else:
        print("Perdiste. El papel envuelve a la piedra. 😢")

elif usuario == "papel":
    if computadora == "piedra":
        print("¡Ganaste! El papel envuelve a la piedra. 🎉")
    else:
        print("Perdiste. La tijera corta el papel. 😢")

elif usuario == "tijera":
    if computadora == "papel":
        print("¡Ganaste! La tijera corta el papel. 🎉")
    else:
        print("Perdiste. La piedra rompe la tijera. 😢")

else:
    print("Opción no válida. Por favor, escribe piedra, papel o tijera.")