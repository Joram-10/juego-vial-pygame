import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Educación Vial México")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
AMARILLO = (255, 204, 0)
AZUL = (50, 150, 255)  # Color Ana
VERDE = (50, 200, 50)  # Color Luis
GRIS = (100, 100, 100)

# Fuentes
fuente_titulo = pygame.font.SysFont("Arial", 40, bold=True)
fuente_texto = pygame.font.SysFont("Arial", 24)

# Variables de estado
estado_juego = "MENU"  # Puede ser: MENU, NIVEL_1, NIVEL_2, FIN
personaje_elegido = ""
color_personaje = NEGRO


def dibujar_texto(texto, fuente, color, x, y):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))


def dibujar_senal_alto(x, y):
    # Dibuja un octágono rojo
    puntos = [(x + 30, y), (x + 70, y), (x + 100, y + 30), (x + 100, y + 70),
              (x + 70, y + 100), (x + 30, y + 100), (x, y + 70), (x, y + 30)]
    pygame.draw.polygon(pantalla, ROJO, puntos)
    dibujar_texto("ALTO", fuente_texto, BLANCO, x + 20, y + 35)
    # Poste
    pygame.draw.rect(pantalla, GRIS, (x + 45, y + 100, 10, 80))


def dibujar_senal_ceda(x, y):
    # Dibuja un triángulo invertido
    puntos = [(x, y), (x + 100, y), (x + 50, y + 100)]
    pygame.draw.polygon(pantalla, AMARILLO, puntos)
    pygame.draw.polygon(pantalla, NEGRO, puntos, 3)  # Borde
    dibujar_texto("CEDA", pygame.font.SysFont("Arial", 18, bold=True), NEGRO, x + 25, y + 20)
    # Poste
    pygame.draw.rect(pantalla, GRIS, (x + 45, y + 100, 10, 80))


# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    pantalla.fill(BLANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if estado_juego == "MENU":
                if evento.key == pygame.K_1:
                    personaje_elegido = "Ana (Peatón)"
                    color_personaje = AZUL
                    estado_juego = "NIVEL_1"
                elif evento.key == pygame.K_2:
                    personaje_elegido = "Luis (Conductor)"
                    color_personaje = VERDE
                    estado_juego = "NIVEL_1"

            elif estado_juego == "NIVEL_1":
                # La respuesta correcta es la A (Detenerse)
                if evento.key == pygame.K_a:
                    estado_juego = "NIVEL_2"
                elif evento.key == pygame.K_b:
                    estado_juego = "FIN_MAL"

            elif estado_juego == "NIVEL_2":
                # La respuesta correcta es la B (Dejar pasar)
                if evento.key == pygame.K_a:
                    estado_juego = "FIN_MAL"
                elif evento.key == pygame.K_b:
                    estado_juego = "FIN_BIEN"

    # Lógica de dibujo según el estado
    if estado_juego == "MENU":
        dibujar_texto("Juego de Señales Viales - México", fuente_titulo, NEGRO, 100, 100)
        dibujar_texto("Elige tu personaje:", fuente_texto, NEGRO, 100, 200)
        dibujar_texto("Presiona 1 para Ana (Peatón)", fuente_texto, AZUL, 150, 250)
        dibujar_texto("Presiona 2 para Luis (Conductor)", fuente_texto, VERDE, 150, 300)

    elif estado_juego == "NIVEL_1":
        dibujar_texto(f"Nivel 1 - Jugando como: {personaje_elegido}", fuente_titulo, color_personaje, 50, 50)
        dibujar_senal_alto(350, 150)

        dibujar_texto("Llegas a una intersección y ves esta señal.", fuente_texto, NEGRO, 50, 380)
        dibujar_texto("¿Qué debes hacer?", fuente_titulo, NEGRO, 50, 420)
        dibujar_texto("A) Detenerme por completo y mirar a los lados.", fuente_texto, NEGRO, 80, 480)
        dibujar_texto("B) Acelerar para pasar rápido.", fuente_texto, NEGRO, 80, 520)

    elif estado_juego == "NIVEL_2":
        dibujar_texto(f"Nivel 2 - Jugando como: {personaje_elegido}", fuente_titulo, color_personaje, 50, 50)
        dibujar_senal_ceda(350, 150)

        dibujar_texto("Te acercas a una avenida principal y ves esta señal.", fuente_texto, NEGRO, 50, 380)
        dibujar_texto("¿Qué significa?", fuente_titulo, NEGRO, 50, 420)
        dibujar_texto("A) Que tengo preferencia y debo tocar el claxon.", fuente_texto, NEGRO, 80, 480)
        dibujar_texto("B) Que debo reducir la velocidad y dejar pasar a otros.", fuente_texto, NEGRO, 80, 520)

    elif estado_juego == "FIN_BIEN":
        dibujar_texto("¡FELICIDADES!", fuente_titulo, VERDE, 250, 200)
        dibujar_texto("Conoces muy bien las señales de tránsito de México.", fuente_texto, NEGRO, 150, 280)
        dibujar_texto("Cierra la ventana para salir.", fuente_texto, GRIS, 250, 350)

    elif estado_juego == "FIN_MAL":
        dibujar_texto("¡CUIDADO!", fuente_titulo, ROJO, 300, 200)
        dibujar_texto("Esa no era la respuesta correcta. Podrías causar un accidente.", fuente_texto, NEGRO, 100, 280)
        dibujar_texto("Cierra la ventana e intenta de nuevo.", fuente_texto, GRIS, 200, 350)

    pygame.display.flip()
    reloj.tick(30)

pygame.quit()
sys.exit()
