def trivia_fetch(num):
    # Diccionario con varios datos curiosos
    trivia = {
        "number": num,
        "facts": [
            f"El número {num} es divisible por 2" if num % 2 == 0 else f"El número {num} es impar",
            f"El número {num} al cuadrado es {num**2}",
            f"El doble de {num} es {num*2}"
        ]
    }
    return trivia


def main():
    print("Hello learners!")  # 👈 Manteniendo la línea del inicio
    print("🎯 Bienvenido al Quiz de Cultura General 🎯\n")
    print("Instrucciones: Responde las preguntas escribiendo la letra o el número correspondiente y presiona Enter.\n")

    score = 0

    # Pregunta 1
    ans1 = input("1) ¿Cuál es la capital de Francia?\n a) Roma\n b) París\n c) Madrid\n👉 ")
    if ans1.lower() == "b" or ans1.lower() == "parís":
        print("✅ Correcto!\n")
        score += 1
    else:
        print("❌ Incorrecto. La respuesta era París.\n")

    # Pregunta 2
    ans2 = input("2) ¿Cuántos planetas tiene el sistema solar?\n a) 8\n b) 9\n c) 7\n👉 ")
    if ans2 == "a" or ans2 == "8":
        print("✅ Correcto!\n")
        score += 1
    else:
        print("❌ Incorrecto. Son 8 planetas.\n")

    # Pregunta 3
    num = int(input("3) Escribe tu número favorito: "))
    info = trivia_fetch(num)
    print("\nDatos curiosos sobre tu número:")
    for dato in info["facts"]:
        print(f"- {dato}")
    score += 1  # siempre suma porque interactuó

    # Resultado final
    print(f"\n🎉 Tu puntaje final es {score}/3")


if __name__ == "__main__":
    main()