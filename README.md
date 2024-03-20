# Para que funciona este script?

Es un script al cual le pasas a través del archivo "hosts.txt" las IPs de los routers a los cuales quieres que se conecte
Y este les colocara la configuracion correcta para el apartado NTP y CLOCK

# Que comandos ejecuta sobre mis routers?

Para V6 ejecutará los siguientes comandos :
- "/system ntp client set primary-ntp=10.0.2.9 secondary-ntp=172.16.1.122"
- "/system clock set time-zone-name=America/Bogota" 

Para V7 ejecutará los siguientes comandos :
- "/system/ntp/client/servers remove [find]"
- "/system clock set time-zone-name=America/Bogota"
- "/system ntp client set enabled=yes",
- "/system ntp client servers add address=10.0.2.9",
- "/system ntp client servers add address=172.16.1.122"

# Como lo uso?

Coloca tus IPs en el archivo "hosts.txt" debe haber una IP por linea y si el archivo no existe crealo con ese mismo nombre.
Por ultimo ejecuta python main.py y el resto lo  hará el script
