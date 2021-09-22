# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero1 = int(input("Coloque aqui el primer numero: "))

numero2 = int(input("Coloque aqui el segundo numero: "))

numero3 = int(input("Coloque aqui el tercer numero: "))

resultado1 = (numero1 % 2)
resultado2 = (numero2 % 2)
resultado3 = (numero3 % 2)

if (resultado1 == 0):
    print("El numero", numero1, "es par.")
else:
    print("El numero", numero1, "es impar.")

if (resultado2 == 0):
    print("El numero", numero2, "es par.")
else:
    print("El numero", numero2, "es impar.")

if (resultado3 == 0):
    print("El numero", numero3, "es par.")
else:
    print("El numero", numero3, "es impar.")