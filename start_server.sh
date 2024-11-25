#!/bin/bash

# Configure correct PATH
export PATH=$PATH:/home/jjrosat/.local/bin:/usr/bin

# Start the server on background
nohup /home/jjrosat/.local/bin/gunicorn -w 4 -b 0.0.0.0:8080 --worker-class geventwebsocket.gunicorn.workers.GeventWebSocketWorker app:app > server.log 2>&1 &
echo "
###################################################################

Server is running on background. 
Logs can be found at server.log file.
To enter the server open the following URL: http://127.0.0.1:8080/

###################################################################
"
