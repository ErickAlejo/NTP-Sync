# Que hace este script

Le pasas un listado de IPs al archivo hosts.txt y lo ejecutas, este deberá configurar el NTP y el apartado Clock en cada uno de los routers que esten en el archivo hosts.txt. **Principalmente esta pensado para ser usado en routers Mikrotik V7,V6.**

# Que comandos ejecuta en mis Routers Mikrotik

**Comandos V6, que ejecutará**
- "/system ntp client set primary-ntp=10.0.2.9 secondary-ntp=172.16.1.122"
- "/system clock set time-zone-name=America/Bogota" 

**Comandos V7, que ejecutará**
- "/system/ntp/client/servers remove [find]"
- "/system clock set time-zone-name=America/Bogota"
- "/system ntp client set enabled=yes",
- "/system ntp client servers add address=X.X.X.X",
- "/system ntp client servers add address=X.X.X.X"

# Como lo uso

Coloca tus IPs en el archivo "hosts.txt" debe haber una IP por linea y si el archivo no existe crealo con ese mismo nombre. Por ultimo ejecuta python main.py y el resto lo  hará el script

```sh
touch hosts.txt # Coloca tus IPs en este archivo
python3 main.py
# Happy Hacking
```