from machine import Pin
import time
from minikame import MiniKame
from sensoreyes import SensorEyes
from webconnector import WebConnector
from commandexecutor import CommandExecutor

robot = MiniKame()
eyes = SensorEyes()
connector = WebConnector()
executor = CommandExecutor(robot)

def setup():
    # Configurar pines
    # ...

    connector.init()
    robot.init()
    eyes.init()
    executor.init(robot)
    print("Robot is starting.")

def loop():
    # Procesar la conexión si hay alguna
    connector.handleConnection()
    # Obtener el comando activo
    activeCommand = connector.getActiveCommand()

    print("Executing command:", activeCommand)

    if executor.isAutonomous():
        # Algo de lógica para el modo autónomo
        eyes.measureDistance()
        if eyes.getDistance() == 0 or eyes.getDistance() > 20:
            # Solo correr si no hay valores o si la distancia es mayor que 20
            executor.parseCommand("01")
        else:
            # Algo está en el camino, intentar ir a la derecha
            executor.parseCommand("04")

    # Ejecutar el comando activo, que llama al robot
    executor.parseCommand(activeCommand)

# Configurar y ejecutar el programa
setup()
while True:
    loop()
    time.sleep(0.1)  # Añadir un pequeño retraso para evitar que el bucle se ejecute demasiado rápido
```
