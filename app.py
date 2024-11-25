from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import threading
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)
playbook_running = False
playbook_process = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_playbook')
def start_playbook(data):
    global playbook_running, playbook_process

    playbook_path = data.get('playbook_path')

    if not playbook_path:
        emit('status', {'message': 'Por favor, proporcione una ruta para el playbook'})
        return

    if playbook_running:
        emit('status', {'message': 'Playbook ya está ejecutándose'})
        return

    playbook_running = True
    emit('status', {'message': f'Iniciando playbook: {playbook_path}...'})

    def run_playbook():
        global playbook_running, playbook_process
        try:
            # Ejecutamos el playbook en un subproceso
            playbook_process = subprocess.Popen(
                ['ansible-playbook', playbook_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            # Leer la salida estándar y de error en tiempo real
            for line in iter(playbook_process.stdout.readline, ''):
                socketio.emit('status', {'message': line.strip()})
            for line in iter(playbook_process.stderr.readline, ''):
                socketio.emit('status', {'message': line.strip()})

            # Esperar a que termine el proceso
            playbook_process.stdout.close()
            playbook_process.stderr.close()
            playbook_process.wait()

            # Cuando termine, se marca como no ejecutándose
            socketio.emit('status', {'message': 'Playbook terminado'})
        except Exception as e:
            socketio.emit('status', {'message': f'Error: {str(e)}'})
        finally:
            playbook_running = False
            playbook_process = None

    # Ejecutar el playbook en un hilo separado para no bloquear el servidor
    threading.Thread(target=run_playbook).start()

@socketio.on('cancel_playbook')
def cancel_playbook():
    global playbook_running, playbook_process

    if playbook_running and playbook_process:
        playbook_process.terminate()  # Detener el playbook
        playbook_running = False
        emit('status', {'message': 'Playbook cancelado'})
    else:
        emit('status', {'message': 'No hay playbook en ejecución'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080)
