import pygame
import time
import random

# --- 1. Inicialización ---
try:
    pygame.init() # Arranca el motor de pygame
except ImportError:
    print("Error: No se pudo cargar pygame. Asegúrate de haber ejecutado 'pip install pygame'")
    exit()

# --- 2. Definición de Colores (Formato RGB) ---
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 102)
NEGRO = (0, 0, 0)
ROJO = (213, 50, 80)
VERDE = (0, 255, 0)
AZUL = (50, 153, 213)

# --- 3. Configuración de la Pantalla y el Juego ---
ANCHO_PANTALLA = 600
ALTO_PANTALLA = 400

# Usaremos una cuadrícula. Cada bloque de la serpiente o comida mide esto:
TAMANIO_BLOQUE = 10 
# Velocidad del juego (cuántos bloques se mueve por segundo)
VELOCIDAD = 15 

# Creamos la ventana de visualización
dis = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Juego de la Serpiente - Python')

# El reloj controla los fotogramas por segundo (FPS)
reloj = pygame.time.Clock()

# Definimos las fuentes para los textos
fuente_puntuacion = pygame.font.SysFont("comicsansms", 25)
fuente_mensaje = pygame.font.SysFont("bahnschrift", 25)

# --- 4. Funciones Auxiliares ---

def mostrar_puntuacion(score):
    """Dibuja el marcador en la pantalla."""
    valor = fuente_puntuacion.render(f"Puntuación: {score}", True, AMARILLO)
    dis.blit(valor, [0, 0]) # 'blit' copia la imagen (texto) a la pantalla

def dibujar_serpiente(tamanio_bloque, lista_serpiente):
    """Dibuja cada segmento de la serpiente."""
    for x in lista_serpiente:
        # pygame.draw.rect(superficie, color, [x, y, ancho, alto])
        pygame.draw.rect(dis, VERDE, [x[0], x[1], tamanio_bloque, tamanio_bloque])

def mensaje_final(msg, color):
    """Muestra el mensaje de 'Game Over' en el centro."""
    mesg = fuente_mensaje.render(msg, True, color)
    # Centramos el mensaje
    text_rect = mesg.get_rect(center=(ANCHO_PANTALLA/2, ALTO_PANTALLA/2))
    dis.blit(mesg, text_rect)

def spawnear_comida():
    """Genera coordenadas aleatorias para la comida dentro de la cuadrícula."""
    # Aseguramos que las coordenadas sean múltiplos de TAMANIO_BLOQUE
    foodx = round(random.randrange(0, ANCHO_PANTALLA - TAMANIO_BLOQUE) / 10.0) * 10.0
    foody = round(random.randrange(0, ALTO_PANTALLA - TAMANIO_BLOQUE) / 10.0) * 10.0
    return foodx, foody

# --- 5. Bucle Principal del Juego (Game Loop) ---

def loop_juego():
    """Contiene toda la lógica principal del juego."""
    global_game_over = False
    global_game_close = False

    # Posición inicial de la cabeza
    x1 = ANCHO_PANTALLA / 2
    y1 = ALTO_PANTALLA / 2

    # Cambios de posición (movimiento)
    x1_change = 0
    y1_change = 0

    # Lógica de la serpiente
    lista_serpiente = []
    largo_serpiente = 1

    # Spawn de comida inicial
    foodx, foody = spawnear_comida()

    while not global_game_over:

        # --- Sub-bucle de 'Game Over' (Espera para reiniciar o salir) ---
        while global_game_close == True:
            dis.fill(NEGRO)
            mensaje_final("¡Perdiste! Presiona C-Jugar de nuevo o Q-Salir", ROJO)
            mostrar_puntuacion(largo_serpiente - 1)
            pygame.display.update()

            # Captura eventos en la pantalla de Game Over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # Salir definitivamente
                        global_game_over = True
                        global_game_close = False
                    if event.key == pygame.K_c: # Reiniciar el bucle
                        loop_juego()
                if event.type == pygame.QUIT: # Cerrar ventana 'X'
                    global_game_over = True
                    global_game_close = False

        # --- Manejo de Eventos de Entrada (Controles) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Si tocan la 'X' de la ventana
                global_game_over = True
            if event.type == pygame.KEYDOWN: # Si presionan una tecla
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -TAMANIO_BLOQUE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = TAMANIO_BLOQUE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -TAMANIO_BLOQUE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = TAMANIO_BLOQUE
                    x1_change = 0

        # --- Lógica de Movimiento y Colisiones ---

        # 1. Verificar colisión con las paredes (fuera de límites)
        if x1 >= ANCHO_PANTALLA or x1 < 0 or y1 >= ALTO_PANTALLA or y1 < 0:
            global_game_close = True
        
        # 2. Actualizar posición de la cabeza
        x1 += x1_change
        y1 += y1_change
        
        # 3. Dibujar fondo vacío
        dis.fill(NEGRO)
        
        # 4. Dibujar comida
        pygame.draw.rect(dis, ROJO, [foodx, foody, TAMANIO_BLOQUE, TAMANIO_BLOQUE])
        
        # 5. Lógica del cuerpo de la serpiente
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)

        # Si la lista es más larga que el tamaño actual, borramos la cola
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        # 6. Verificar colisión con sí misma (chocar con su propio cuerpo)
        for x in lista_serpiente[:-1]: # Revisamos todo menos la cabeza actual
            if x == cabeza_serpiente:
                global_game_close = True

        # 7. Dibujar serpiente actualizada
        dibujar_serpiente(TAMANIO_BLOQUE, lista_serpiente)
        mostrar_puntuacion(largo_serpiente - 1)

        # 8. Actualizar la pantalla completa
        pygame.display.update()

        # 9. Verificar si comió la comida
        if x1 == foodx and y1 == foody:
            foodx, foody = spawnear_comida() # Nueva comida
            largo_serpiente += 1             # Crecer

        # Controlar la velocidad (pausa el bucle)
        reloj.tick(VELOCIDAD)

    # --- Salida Limpia del Juego ---
    pygame.quit()
    quit()

# --- 6. Ejecución ---
if __name__ == "__main__":
    loop_juego()