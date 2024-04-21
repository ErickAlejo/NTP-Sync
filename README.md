# NTP-Sync
![Logo NTP-Sync](https://i.imgur.com/DeQY0Cx.png)
## Descripción
Script en Python para dispositivos y routers Mikrotik, cambiar configuracion de NTP/Clock para cientos o miles de routers. 

## ¿Como ejecutar?

**Paso #1**
- ```pip3 install -r requirements.txt```
- ```Coloca tus IPS en el archivo hosts.txt (una ip por linea)```

**Paso #2**
- ```Abre el archivo template.json y reemplaza X.X.X.X por dos IPs de servidores NTP```
- ```Abre el archivo .env y modifica el usuario y contraseña por las de tus routers```

**Paso #3**
- ```✨ Python3 main.py ✨```
 

### Features

| Caracteristicas |
| ------ |
| Flexible y ajustable a nuevos comandos | 
| Detecta V7 y V6 en Mikrotik | 
| Comandos Personalizados | 
| Escalable via template JSON |
