print("Hola este es un analizador de texto")
print("------------------------------------")
texto = input("Porfavor, Ingresa un texto a tu gusto (Ya sea un poema o una frase):\n").lower() #Se le solicita al usuario que ingrese un texto para poder analizarlo
lista_texto = texto.split()
print(f"Tu texto tiene en total:\n {len(lista_texto)} palabras")

print("Muy bien, continua...")
lista_letras = ['','','']
lista_letras[0] = input("Porfavor ingrese la primera(1era) letra para analizar el texto:\n").lower() #   *  Peticion al usuario que sirven para analizar y conteo de
lista_letras[1] = input("Porfavor ingrese la segunda(2da) letra para analizar el texto:\n").lower()  #   *  cuantas letras seleccionadas existen en el texto
lista_letras[2] = input("Porfavor ingrese la tercera(3era) letra para analizar el texto:\n").lower() #   *  que ingreso el usuario
print(lista_letras)
print(f" Se analizo un total de {texto.count(lista_letras[0])} letras {lista_letras[0].upper()} en el texto") # Realiza el conteo almacenado
print(f" Se analizo un total de {texto.count(lista_letras[1])} letras {lista_letras[1].upper()} en el texto") # en la lista de letras que se le
print(f" Se analizo un total de {texto.count(lista_letras[2])} letras {lista_letras[2].upper()} en el texto") # solicito al usuario.


