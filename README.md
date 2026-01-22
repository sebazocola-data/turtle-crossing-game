# 🐢 Turtle Crossing Game

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Turtle Graphics](https://img.shields.io/badge/Turtle_Graphics-✅-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Complete-success)

Un juego clásico estilo "Frogger" implementado en Python con Turtle Graphics. Controla una tortuga que debe cruzar una carretera llena de coches en movimiento.


## ✨ Características
- ✅ Sistema de niveles progresivos (dificultad aumenta)
- ✅ Generación aleatoria de coches con colores RGB aleatorios
- ✅ Detección de colisiones entre tortuga y coches
- ✅ Sistema de puntuación y niveles
- ✅ Animación fluida con control de velocidad
- ✅ Arquitectura orientada a objetos limpia

## 🚀 Cómo ejecutar

### Prerrequisitos
- Python 3.8 o superior
- Turtle Graphics (incluido en Python estándar)

### Instalación y ejecución
```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/turtle-crossing-game.git

# 2. Entrar en la carpeta
cd turtle-crossing-game

# 3. Ejecutar el juego
python main.py


##----------------------------------------------------------

🧩 Descripción técnica de las clases
Player (player.py)
Clase que representa a la tortuga jugadora:

Hereda de Turtle para gráficos

Movimiento controlado por teclado

Método level_up() para reiniciar posición

Cars (cars.py)
Clase que maneja los coches enemigos:

Generación aleatoria de posición y color RGB

Movimiento automático de derecha a izquierda

Cada coche tiene velocidad y color únicos

LevelUp (level.py)
Clase que controla la dificultad:

Muestra nivel actual en pantalla

Incrementa nivel cuando la tortuga cruza

Aumenta velocidad de coches por nivel

Maneja estado de "Game Over"

main.py
Bucle principal del juego:

Inicializa pantalla y objetos

Controla la lógica del juego

Maneja colisiones y condiciones de victoria

Controla la velocidad del juego con time.sleep()

🔧 Conceptos técnicos implementados
Programación Orientada a Objetos (POO): 4 clases bien definidas

Herencia: Todas las clases heredan de Turtle

Listas y bucles: Manejo de múltiples coches

Colisiones: Detección con distance() de Turtle

RGB aleatorio: Generación de colores dinámicos

Control de tiempo: Velocidad ajustable por nivel

🚀 Características avanzadas
Sistema de niveles: Cada nivel aumenta la velocidad en 20%

Generación procedural: 500 coches con posiciones aleatorias

Optimización: Uso de screen.tracer(0) para animación fluida

Manejo de eventos: Teclado responsivo para controles

##-------------------------------------------------------

## 🔮 Roadmap (mejoras planeadas)

### Versión 2.0:
- [ ] Sistema de vidas (3 intentos)
- [ ] Diferentes tipos de vehículos
- [ ] Power-ups (invencibilidad temporal)
- [ ] Tabla de records con nombres
- [ ] Efectos de sonido con pygame

### Refactorizaciones técnicas:
- [ ] Mejorar detección de colisiones (bounding boxes)
- [ ] Optimizar generación de coches (pooling)
- [ ] Separar lógica de UI completamente
