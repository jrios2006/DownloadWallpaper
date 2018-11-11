# DownloadWallpaper

Descargar del sitio wallpaperswide.com y almacenarlas en una carpeta local.

Programar el entorno de ecritorio cinnamon para que cambie nuestro fono de pantalla con el contenido de estas imágenes.

Además tener un poco controlado las imágenes que vamo a descar de manera automática, para que no crezca demasiado el número de imágenes.

# Instalación

Vamos a hacer uso de tareas automatizadas y antergos, sistema con el que estoy probando, no instala por defecto cron.

Se puede hacer uso de sysmtemd, pero creo que es demasiado complicada para las dos tareas que vamos a automatizar.

Como administrador instalamos crona través del paquete cronie  mediate el comando 
~~~
pacman -S cronie
~~~
Iniciamos el software mediante 
~~~
systemctl start cronie
~~~
Lo habilitamos para que arranque cuando reiniciemos la máquina
~~~
systemctl enable cronie
~~~

Comprobamos que nuestro editor de texto por consola sea el que esperamos que sea.
~~~
env | grep EDITOR
~~~
En mi caso es nano
~~~
EDITOR=/usr/bin/nano
~~~
Si no quiesieras nano como editor y quisieras vi habría que cambiar esta propiedad en tu shell

Editamos y añadimos dos tareas anuestro cron, una para descargar imágenes cada 10 minutos por ejemplo y la otra para mantener la carpeta de imágenes a raya y que no crezca demasiado
~~~
crontab -e
~~~
La ruta /Fotos cambiadla por la vuestra
~~~
# Descargar de imágenes del sitio wallpaperswide
*/10 *  *  *  * /Fotos/descargas.sh > /dev/null 2>&1
~~~
Por defecto en antergos python usa la versión 3. 

Si tuvieras que usar la versión 2 debes cambiar el código del script en python. Al menos las sentencias print, o cambiar python por python3 para ejecutar la versión 3 del intérprete de python.
~~~
# Limpio la carpeta de wallpapers para 500 fotos máximmo
22 22 * * * python /Fotos/wallpaper-limpieza.py > /dev/null 2>&1
~~~

Además debes hacer el script descargas.sh ejecutable con el comando 
~~~
chmod +x /Fotos/descargas.sh
~~~

# Uso de descargas.sh

Se ha usado como base el script que está en la [URL](https://github.com/bijanebrahimi/waffle "Descarga de Wallpaper")

He añadido las categorias que hay actualmente en la web a través de la variable CAT.

Uso curl para descargar las imágenes

# Uso de wallpaper-limpieza.py

Este programa lista los ficheros jpg que hay en la carpeta y si hay más de un tope definido en la variable TotalFicheros borra las más antiguas

La variable Ruta mira donde debe mirar las fotos que es donde almacena el programa descargas.sh las fotos del sitio web

