#El tablero debe ser un arreglo de 3x3
#Funcion imprimirTablaActual para imprimir la tabla en el estado actual
#Funcion validarJuego que nos retorne si ya ha ganado alguien, hay empate, etc. 
#Funcion ingresarMovimiento para verificar si un movimiento es valido en la tabla actual
#Necesitamos un control sobre los turnos
# Despues de cada movimiento, necesitamos verificar si ya se ha producido un juego ganador
# o en todo caso, si existe un empate. 
import random, time

tablero = [""] * 9

turnos = {
     "X": 'x',
     "O": 'o'
}

combosGanadores = [
  [0,1,2],
  [3,4,5],
  [6,7,8],
  [0,4,8],
  [2,4,6],
  [0,3,6],
  [1,4,7],
  [2,5,8]
]

# Estados del juego
ganador = None
turnoActual = turnos["X"]

def display_board(tablero):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    time.sleep(1.5)
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for column in range(3):
            indice = row * 3 + column
            valor = tablero[indice] if tablero[indice] != "" else indice + 1
            print("|    ",valor, "", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------+-------+-------+")

def verificarGanador():
    global tablero
    for combo in combosGanadores:
        [a,b,c] = combo
        if(tablero[a] and tablero[a] == tablero[b] and tablero[a] == tablero[c]):
            return tablero[a]
    return None
  
def verificarEmpate():
    global tablero

    for i in range(len(tablero)):
        if(tablero[i] == ""):
            return False
    return True

def actualizarTablero(index):
    global tablero, turnoActual, ganador

    tablero[index] = turnoActual
    
    turnoActual = turnos["O"] if (turnoActual == turnos["X"]) else turnos["X"]

    hayGanador = verificarGanador()
    if(hayGanador):
        ganador = hayGanador # se escribe el valor del ganador x u o
        
    elif verificarEmpate():
        ganador = False

def validarEntrada(turnoActual):
    global tablero
    while True:
        if(turnoActual == turnos['O']):
            movimiento= int(input("Ingresa una casilla (1-9): ")) - 1
        else: 
            movimiento = random.randrange(0,9)

        if( 0 <= movimiento <= 8 and not(tablero[movimiento])):
            return movimiento
        elif (turnoActual == turnos['O']):
            print("Ingresa un número valido! ")

def realizarTurno():
    global turnoActual, tablero
    print("Turno de: ", turnoActual)
    movimiento = validarEntrada(turnoActual)    
    actualizarTablero(movimiento) 
    display_board(tablero)    

def main():
    global tablero
    global ganador
    movimientoCPU = 4

    # Primer movimiento CPU 
    actualizarTablero(movimientoCPU) # X en el centro
    display_board(tablero)

    while ganador == None:
        realizarTurno()

    if(ganador):
        print("Felicidades el ganador ha sido: ", ganador)  
    else: 
        print("Ha sido un empate")
main()

        

    




