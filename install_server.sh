#!/bin/bash

# Comprobación de permisos
# if [[ $EUID -ne 0 ]]; then
#     echo "Por favor, ejecute este script como usuario root o con sudo."
#     exit 1
# fi

# echo "Updating system..."
# sudo dnf update -y

echo "Installing Python 3.8 and pip..."
sudo dnf install -y python38 python38-pip

# echo "Installing Ansible..."
# dnf install -y ansible

echo "Installing Python dependencies for app..."
python3.8 -m pip install flask flask-socketio ansible-runner gunicorn gevent gevent-websocket --user

# Verificación de instalación
echo "Verifying installed versions:"
echo "Python 3.8: $(python3.8 --version)"
echo "Pip: $(python3.8 -m pip --version)"
echo "Ansible: $(ansible --version | head -n 1)"

echo "Installation completed."
