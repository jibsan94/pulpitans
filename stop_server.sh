#!/bin/bash

# Buscar el PID del proceso Gunicorn relacionado con la app
PID=$(pgrep -f "gunicorn.*app:app")

# Verificar si se encontró el PID
if [ -n "$PID" ]; then
    echo "Deteniendo el servidor con PID: $PID"
    kill $PID

    # Esperar un momento para verificar si se detuvo
    sleep 2
    if ps -p $PID > /dev/null; then
        echo "No se pudo detener el servidor. Intentando con kill -9..."
        kill -9 $PID
    else
        echo "Servidor detenido correctamente."
    fi
else
    echo "No se encontró un servidor en ejecución."
fi
