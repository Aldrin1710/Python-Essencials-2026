# Crear un programa que simule la reproducción de un Album en Spotify. Se podrá añadir cualquier canción a la cola 
#  y tambíen poder activar el modo aleatorio (opcional)

# Analisis
# Necesitamos una lista canciones[] que tenga las canciones originales del album
# otra lista cola[] que sea el encargado de gestionar la cola de reproducción
# necesitamos simular la reproducción del album (pausar continuar skipear)

import time 
import random
canciones = ["NUEVAYoL", "VOY A LLeVARTE PA PR", "BAILE INoLVIDABLE", "PERFuMITO NUEVO", "WELTiTA", "VeLDA", "EL CLuB", "KETU TeCRE"]
cola = []

def imprimirMenu():
    print("Bienvenido a la reproducción de 'DeBI TiRAR MaS FOTos'")
    cancionesEnFila(canciones)
    print("Reproducir canciones (1 = normal, 2 = aleatorio)")

def validarOpcion():
    while True:
        opcion = int(input())
        if (opcion== 1) or (opcion==2):
            return opcion
        else:
            print("Valor invalido, ingrese nuevamente: ")

def cancionesEnFila(canciones):
    i = 0
    print("Canciones en fila:")
    for cancion in canciones:
        if(i == 0):
            print("Siguiente cancion: " + cancion)
            i= i + 1 
            continue

        print(str(i) + "." + cancion)
        i = i + 1
    
def reproducirAlbum(modo):
    if(modo == 1):
        cola = canciones     
        while len(cola): #mientras haya elementos en la cola de reproducción
            cancion = cola[0]
            print("REPRODUCIENDO:" + cancion)
            time.sleep(2)
            print("La canción esta por terminar, continuar reproduccion habitual (1), agregar canción a la cola (2), activar modo aleatorio(3)")
            opcion = int(input())
            del cola[0]
            while True:
                if(opcion < 1) or (opcion > 3):
                    print("Opcion invalida intente de nuevo: ")
                    opcion = int(input())
                elif opcion == 1:
                    break
                elif opcion == 2:
                    cancionesEnFila(cola)
                    cancionEscogida = int(input("Ingrese la canción que desea agregar a la fila: "))
                    while True:
                        if (cancionEscogida < 1) or (cancionEscogida > (len(cola) + 1)):
                            print("Opcion invalida, intente de nuevo: ")
                            cancionEscogida = int(input())
                        else:
                            #agregamos la canción a la sig canción después de la actual
                            aux = cola[cancionEscogida]
                            del cola[cancionEscogida]
                            cola.insert(0, aux)
                            break
                    break    
                else:
                    for i in range(len(cola)):
                        numRandom = random.randint(0,len(cola))
                        song = cola[i]
                        del cola[i]
                        cola.insert(numRandom, song)
                    break


def main():
    imprimirMenu()
    modo = validarOpcion()
    reproducirAlbum(modo)

main()


# to do: implementar el modo aleatorio (cuando sepamos usar random)
