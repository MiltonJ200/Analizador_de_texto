print("Hola este es un analizador de texto")
print("------------------------------------")
texto = input("Porfavor, Ingresa un texto a tu gusto (Ya sea un poema o una frase):\n").lower() #Se le solicita al usuario que ingrese un texto para poder analizarlo
primera_letra = texto[0]  #utilizamos esta forma para identificar la PRIMERA letra del texto
ultima_letra = texto[-1] #utilizamos esta forma para identificar la ULTIMA letra del texto
lista_texto = texto.split() #hacemos lista el texto de cada palabra para poder trabajarlo en el analizador de texto

#print(lista_texto) #usar para visualizar la lista de texto
print("Muy bien, continua...\nA continuacion digitaras 3 letras para hacer funcionar el analizador de texto")

lista_letras = ['','','']
lista_letras[0] = input("Porfavor ingrese la primera (1era) letra para analizar el texto:\n").lower() #   *  Peticion al usuario que sirven para analizar y conteo de
lista_letras[1] = input("Porfavor ingrese la segunda (2da) letra para analizar el texto:\n").lower()  #   *  cuantas letras seleccionadas existen en el texto
print("Uno mas...")
lista_letras[2] = input("Porfavor ingrese la tercera (3era) letra para analizar el texto:\n").lower() #   *  que ingreso el usuario
#print(lista_letras) usar para visualizar la lista de letras

print(f" Se analizo un total de {texto.count(lista_letras[0])} letras {lista_letras[0].upper()} en el texto") # Realiza el conteo almacenado
print(f" Se analizo un total de {texto.count(lista_letras[1])} letras {lista_letras[1].upper()} en el texto") # en la lista de letras que se le
print(f" Se analizo un total de {texto.count(lista_letras[2])} letras {lista_letras[2].upper()} en el texto") # solicito al usuario.
print(f"\nTu texto tiene en total:\n {len(lista_texto)} palabras") #contamos la cantidad de palabras que existen en el texto
print(f"\nEn el texto la primera letra del texto es \"{primera_letra.upper()}\" y la ultima letra es \"{ultima_letra.upper()}\"") #consultamos cual es la primera y ultima letra
                                                                                                                                  #del texto

print("\nLas palabras en orden inverso se ve de la siguiente manera:")
lista_texto.reverse()   #Invertimos el texto que se encuentra en la lista de texto
print(" ".join(lista_texto))    #agregamos los espacios y unimos el texto para poder visualizar ya la cadena de texto junta sobre la lista texto

control_de_texto = "python" in lista_texto #preguntamos o consultamos si existe la palabra "python" en el texto
diccionario_VF = {True:'si', False:'no'}   #Creamos un diccionario donde nos permita decir si o no al momento de recibir el dato booleano True o False
print(f"\nEl resultado si existe o no la palabra \"Python\" en el texto {diccionario_VF[control_de_texto]} existe en el texto") #realizamos un print donde llamaremos al diccionario
                                                                                                                                #y traduciendolo con nuestro diccionario


