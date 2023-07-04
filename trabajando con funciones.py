'''1 - Crear una funcion o procedimiento que pida como parametro un nombre y que muestre
en pantalla un saludo con el nombre pasado como argumento.'''
# Definimos la función para saludar con un nombre
def saludar(nombre):
    # Imprimimos un saludo con el nombre pasado como argumento
    print("¡Hola, " + nombre + "! Bienvenido.")

# Pedimos al usuario que ingrese un nombre
nombre = input("Ingrese su nombre: ")

# Llamamos a la función de saludo pasando el nombre como argumento
saludar(nombre)

'''2 - Crear una funcion o procedimiento que pida una lista de numeros por parametro y que
muestre en pantalla, la suma de todos los numeros, el promedio, el numero mas alto y el
mas bajo.'''
# Definimos la función para procesar una lista de números
def procesar_numeros(numeros):
    # Calculamos la suma de los números
    suma = sum(numeros)
    
    # Calculamos el promedio dividiendo la suma entre la cantidad de números
    promedio = suma / len(numeros)
    
    # Buscamos el número máximo en la lista
    maximo = max(numeros)
    
    # Buscamos el número mínimo en la lista
    minimo = min(numeros)
    
    # Mostramos los resultados en pantalla
    print("Suma: ", suma)
    print("Promedio: ", promedio)
    print("Máximo: ", maximo)
    print("Mínimo: ", minimo)

# Pedimos al usuario que ingrese una lista de números separados por comas
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertimos la cadena de números en una lista de enteros
numeros = [int(num) for num in numeros.split(',')]

# Llamamos a la función para procesar la lista de números
procesar_numeros(numeros)
