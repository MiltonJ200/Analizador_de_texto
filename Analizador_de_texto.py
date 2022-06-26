print("Hola este es un analizador de texto")
print("------------------------------------")
texto = input("Porfavor, Ingresa un texto a tu gusto (Ya sea un poema o una frase):\n").lower() #Se le solicita al usuario que ingrese un texto para poder analizarlo
primera_letra = texto[0]  #utilizamos esta forma para identificar la PRIMERA letra del texto
ultima_letra = texto[-1] #utilizamos esta forma para identificar la ULTIMA letra del texto
lista_texto = texto.split()

#print(lista_texto) #usar para visualizar la lista de texto
print("Muy bien, continua...")
lista_letras = ['','','']
lista_letras[0] = input("Porfavor ingrese la primera(1era) letra para analizar el texto:\n").lower() #   *  Peticion al usuario que sirven para analizar y conteo de
lista_letras[1] = input("Porfavor ingrese la segunda(2da) letra para analizar el texto:\n").lower()  #   *  cuantas letras seleccionadas existen en el texto
lista_letras[2] = input("Porfavor ingrese la tercera(3era) letra para analizar el texto:\n").lower() #   *  que ingreso el usuario
#print(lista_letras) usar para visualizar la lista de letras
print(f" Se analizo un total de {texto.count(lista_letras[0])} letras {lista_letras[0].upper()} en el texto") # Realiza el conteo almacenado
print(f" Se analizo un total de {texto.count(lista_letras[1])} letras {lista_letras[1].upper()} en el texto") # en la lista de letras que se le
print(f" Se analizo un total de {texto.count(lista_letras[2])} letras {lista_letras[2].upper()} en el texto") # solicito al usuario.
print(f"Tu texto tiene en total:\n {len(lista_texto)} palabras")
print(f"En el texto la primera letra del texto es \"{primera_letra.upper()}\" y la ultima letra es \"{ultima_letra.upper()}\"")
print("las palabras en orden inverso se ve de la siguiente manera: \n")
lista_texto.reverse()
print(" ".join(lista_texto))



