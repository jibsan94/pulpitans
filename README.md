# Welcome to the `PulpitAns` web UI for running `Ansible` playbooks on RedHat 8.6.
In order to leave the app running on a server, you must follow the next steps:

## Step 1
Execute the `install_server.sh` script.
This will install all the required packages and dependencies for the app.

> [!TIP]
> Run the script with the following commands:
> * cd /route/to/the/pulpitans/app
> * ./install_server.sh
_________________________________________________________________________

## Step 2
Execute the `start_server.sh` script.
This will start the app listening on the port `8080`.

> [!TIP]
> Run the script with the following commands:
> * cd /route/to/the/pulpitans/app
> * ./start_server.sh
_________________________________________________________________________

## Step 3
Execute the `stop_server.sh` script.
This will stop the app by killing all the opened processes.

> [!TIP]
> Run the script with the following commands:
> * cd /route/to/the/pulpitans/app
> * ./stop_server.sh
_________________________________________________________________________

# To change the listening port of the app you must edit the following line:

![Screenshot 2024-11-25 114905](https://github.com/user-attachments/assets/63d92b7c-c0fa-4785-a477-ffc016593369)

There you must change the port for the desired one. Once you done, you must also change the `start_server.sh` with the same port you also configured.

![Screenshot 2024-11-25 115237](https://github.com/user-attachments/assets/90a226a3-f2d6-4e28-bb21-1216fd902f31)

# Notes:

> [!CAUTION]
> In order to runn correctly the app, you must change the `PATH` variable with the user who will be running the server on the `start_server.sh`.
>![Screenshot 2024-11-25 115237](https://github.com/user-attachments/assets/a7c19860-4acb-44f8-b2ee-115fc325a76d)
> ![Screenshot 2024-11-25 115244](https://github.com/user-attachments/assets/30929047-c8e9-4bbd-adb7-379f4a3a5031)
