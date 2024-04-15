# NTP-Sync
## Description
Script en Python para dispositivos y routers Mikrotik, cambiar configuracion de NTP/Clock para cientos o miles de routers. 

## Como ejecutar
Paso #1

- ```pip3 install -r requirements.txt```

- Coloca tus IPS en el archivo hosts.txt (una ip por linea)

Paso #2

- Abre el archivo template.json de la carpeta './templates' y reemplaza X.X.X.X por las ip de tu servidor NTP (coloca dos IPs distintas)
- Abre el archivo .env (sino lo ves en tu carpeta pulsa CTRL + H para ver el archivo oculto) alli modifica el usuario y contraseña por las de tus routers.


Paso #3
- ``` ✨ Ejecuta ✨ ``` 
- ```Python3 main.py```
 

### Pruebalo 

| Caracteristicas |
| ------ |
| Soporte Tecnico | 
| Detecta V7 y V6 en Mikrotik | 
| Comandos Personalizados | 
| Agrega Features comodamente |