#LAGRS

##Practica 1.1 Directorios de las practicas

Creamos los directorios indicados en el enunciado. 

##Practica 1.2 Uso basico de vi

En este apartado escribimos cuatro titulares con vi con faltas de ortografia.
Posteriormente los corregimos.

##Práctica 1.3. Uso de un editor sin gráficos

El editor que he elegido es nano, debido a su manejo sencillo y a que ya estoy acostumbrado a su uso en otras asignaturas de la carrera

En nano los principales atajos de teclado son:
 
Ctrl + O - Guardar
Ctrl + X - Salir
Ctrl + K - Cortar
Ctrl + U - Pegar
Ctrl + W - Buscar

##Práctica 1.4. Markdown

Creamos el documento indicado en el enunciado de la practica.

Usamos pandoc para limpiar el fichero y luego generamos su version html.

##Practica 1.5 Gestion de contraseñas

En primer lugar he creado un fichero contraseñas.txt con 3 contraseñas.

###1.gpg

He cifrado este fichero usando el comando:

```
gpg -c contraseñas.txt.
```

Luego para descifrar este fichero podremos usar:

```
gpg -d contraseñas.txt.gpg.
```

###2.LibreOffice

Repetimos el caso anterior, pero ahora usaremos LibreOffice.
Para ello creamos un archivo .odt, en mi caso se llamara contraseñas.odt .
A la hora de guardar el documento en la carpeta, elegimos la opcion Añadir Contraseña. Ynos pedira que introduzcamos una clave.
Al activar esta opcion cada vez que queramos abrir este documento deberemos introducir una contraseña.

###3.KeePassx

En este caso usaremos la aplicacion KeePassX.

Para ello abrimos la aplicacion y creamos una nueva base de datos. A continuacion creamos un grupo dentro de esta y añadimos una nueva entrada. En ella establecemos el titulo, nombre y contraseña.

He establecido una contraseña y un archivo llave: archivollave.txt que he guardado en el directorio. Cada vez que se inicie la aplicacion nos pedira la contraseña y el archivo llave.

##Practica 1.6 Secret Sharing

Para realizar este apartado nos pide descomponer una contraseña en 6 trozos y que solo hagan falta 4 de ellos para restaurarlo.

-t: indica el numero de partes que se necesitan para recuperar la contraseña
-n: indica el numero de partes en los que se divide la contraseña.

Para este caso usaremos el siguiente comando:

```
sss-split -t 4 -n 6
```
Y obtenemos los 6 trozos

1-a51b8471567efcc2ce4711bff2ce9f146dedc45dd6e07d27
2-bae7f330a4b4b10c884a7e71b6d2d7846f196c5966458488
3-e88fce3808c4b59e6dc4d3a2d602d9e05590cc96bee882b7
4-a6aa99cd145fd0b0c1be207b7513e97d738afce6a046a574
5-17f7bf7baf6c0cfb7267c13de79d61e2a975800c7ffbc067
6-ce61ff467321f08798c437d8473c24856b6c9042c17eff17

Para recuperar la contraseña debemos usar este comando:

```
sss-combine -t 4 -n 6
```
Nos pedira introducir 4 de los 6 trozos anteriores para recomponerla.

```
Enter 4 shares separated by newlines:
Share [1/4]: 3-e88fce3808c4b59e6dc4d3a2d602d9e05590cc96bee882b7
4-a6aa99cd145fd0b0c1be207b7513e97d738afce6a046a574
5-17f7bf7baf6c0cfb7267c13de79d61e2a975800c7ffbc067
6-ce61ff467321f08798c437d8473c24856b6c9042c17eff17
Share [2/4]: Share [3/4]: Share [4/4]: Resulting secret: Contrase..aSecretSharing
WARNING: binary data detected, use -x mode instead.

```

##Practica 1.7 Vagrant

1. Configuramos VirtualBox para usar /var/tmp/raulsm como carpeta predeterminada de maquinas.

2. Creamos un project directory de Vagrant en el directorio ~/lagrs/vbox01

3. Praparamos la maquina para que sea Ubuntu 22.04 LTS Jammy Jellyfih

4. Usamos vagrant up para descargar e instalar la maquina. Luego usamos vagrant ssh para conectarme a la maquina

5. Salimos de la maquina usando exit.

6. Apagamos la maquina con vagrant halt


## Practica 1.8 Usuarios y grupos

1. Entramos en la maquina virtual como vimos anteriormente.

2. Creamos un nuevo usuario con el comando sudo useradd mi_usuario y establecemos su contraseña sudo passwd mi_usuario.

3. Abro la sesion de mi usuario e introduzco la contraseña, pero a la hora de ejcutar una orden con sudo me salta este error: raulsm is not in the sudoers file. This incident will be reported. 
Para que pueda ejecutar sudo tengo que seguir los siguientes pasos:

* Salgo de la sesion
* Escribo este comando: sudo adduser raulsm sudo
* Ahora entro de nuevo a mi sesion y escribo sudo ls. Me pide contraseña.

4. Creamos dos grupos de la siguiente forma:

* sudo adduser grupo1
* sudo adduser grupo2

A continuacion añadimos nuestro usuario a estos dos grupos.

sudo adduser raulsm grupo1
sudo adduser raulsm grupo2

Ahora comprobamos que nuestro usuario esta en ambos grupos con: 

groups raulsm 

y me dice que :

raulsm : raulsm sudo grupo1 grupo2

Tenemos que probar el comando newgrp. Hacemos newgrp grupo1, por lo que elige grupo1 como primario.

$ id uid=1002(raulsm) gid=1003(grupo1) groups=1003(grupo1),27(sudo),1002(raulsm)

Si ahora hacemos newgrp grupo2

$ id uid=1002(raulsm) gid=1004(grupo2) groups=1004(grupo2),27(sudo),1002(raulsm),1003(grupo1)

## Practica 1.9 ssh sin contraseña (1)

* Genero un par de claves publica-privad con el comando: ssh-keygen -t rsa

* Ahora copio la clave en la maquina que he elegido

 ssh-copy id maquina 

## Practica 1.10 ssh sin contraseña (2)

Configuro la maquina vbox01 para asi poder abrir una sesion.

También usaremos el comando tar para comprimir y descomprimir ficheros.

## Práctica 1.11 scp

1.Copia un fichero cualquiera desde tu puesto del laboratorio al directorio /tmp de un puesto vecino

Escribimos este comando: scp archivo.txt usuario@IP_VECINA:/tmp


2.Entra en un puesto vecino, crea el directorio /tmp/tulogin. (donde tulogin es tu nombre de usuario en el laboratorio). En este directorio, crea unos cuantos ficheros. Copia este directorio al directorio /tmp/ de tu puesto.

Creamos el directorio: raulsm@f-l3109-pc02:/tmp$ mkdir raulsm

Creamos unos cuantos ficheros: touch fichero1 fichero2 fichero3

Ahora en nuestra maquina copiamos el directorio completo: scp -r usuario@IP_VECINA:/tmp/tulogin /tmp


3.Copia un fichero cualquiera desde tu puesto hasta el directorio /tmp de vbox. Recuerda, mediante scp, sin usar el directorio /vagrant de la máquina vbox

Enviamos el fichero ejemplo.md a nuestra maquina vbox: scp ejemplo.md vagrant@127.0.0.1:/tmp
Entramos en nuestra maquina virtual en el directorio /tmp y ahi esta nuestro archivo.

4.Copia un directorio cualquiera desde tu puesto hasta el directorio /tmp de vbox.
Hacmos lo mismo que los apartados anteriores pero esta vez con el directorio con los ficheros anteriores.

scp -r vagrant@127.0.0.1:/tmp/tulogin /tmp

## Práctica 1.12 split

Creo una carpeta con varios archivos en mi maquina.

Busco la hash de cada fichero y la guardo en un archivo de texto.
Comprimo los archivos en un .tgz

A continuacion trozeo el tgz en trozos mas pequeños. Ahora copiamos estos ficheros en /tmp de mi vbox.

Dentro de vbox compuebo que son los mismos ficheros mirando su hash.


## Práctica 1.13 rsync

En esta practica usaremos rsync para acceder desde la local a la remota sin escribir contraseña.

1. En mi primer lugar vamos a clonar un directorio local en uno remoto.

Usamos el siguiente comando clonamos el directorio que hemos elegido en otro directorio donde queramos.

rsync -e ssh -va <directorio_maestro> <directorio_donde_escribir_esclavo>

-e especifica como acceder a los ficheros en la máquina remota

-v verbose (prolijo en detalles)

-a modo archive: incluye subdirectorios, copia enlaces como
enlaces, conserva permisos, fechas y grupo. Si lo ejecuta el root, también conserva el dueño

--delete indica que si se borra un fichero en el maestro, también se borrar´a en el esclavo

2. Ahora clonaremos un directorio remoto en uno local.


3. Consultamos la pagina del manual

Escribimos: man rsync


## Práctica 1.14 FreeFileSync

Creo las carpetas que se mencionan en mi ordenador personal.
He creado el fichero prueba.txt. 
Tras editarlo en el laboratorio intento sincronizarlo. Aparece un mensaje de conflicto.

##Practica 1.15 Conflictos FreeFileSync

Para resolverlo hay que hacerlo a mano y luego elegir con que lado te quieres quedar.

## Practica 1.16 Sincronizacion real de tu cuenta

He instalado FreeFileSync para poder tener un backup de mis practicas en mi ordenador personal.


## Práctica 1.17 Localización de procesos

En primer lugar guardamos los resultados de realizar una captura de los procesos que se estan ejecutando.
Usamos la orden ps -ef > /tmp/procesos_ahora.txt

Luego abrimos un programa, por ejemplo la calculadora.

Y a continuación volvemos a realizar otra captura con el mismo comando pero con diferente nombre de archivo.

Luego usamos el comando diff /tmp/procesos_ahora.txt  /tmp/procesos_despues.txt
Podremos observar entre algunas de las nuevas lineas el proceso CALCULATOR.

## Practica 1.18 Invocacion de la Shell

Los ficheros de inicio de la Shell los obtenemos con el comando “echo $SHELL”. Obtendremos “/bin/bash/” Ejecutamos .bashrc cuando el usuario ejecuta el bash. 

La shell de login es en la que el usuario introdicdo usuario y contraseña. 
En la shell interactiva no hace falta contraseña y login sino que está redirigida desde la consola del usuario. Bashrc es un scrpt de Shell que Bash ejecuta siempre que se inicia de forma interactiva.

Ejecutamos “echo prueba blabla” lo que nos da como resultado: “prueba blabla” 

El archivo .bashrc ya existe y además ejecuta bien.

4.Comprueba qué sucede cuando, desde la shell, cambiamos de usuario mediante la orden su. ¿Qué ficheos se ejecutan? ¿Pasamos a tener una shell de login o no? 

Solo nos deja ejecutar ficheros del usuario que estamos utilizando. Tendremos una Shell de login en la que se nos pedirá tanto el login como la contraseña. 

## Practica 1.19 Docker

1. Primero entramos en vbox01 con vagrant. Para instalar el Docker.io tenemos que meter los siguientes comandos: “sudo apt update” , “sudo apt upgrade -y” , “sudo apt install Docker.io”

Después, tenemos que añadir nuestro usuario al grupo Docker, esto lo hacemos con las sentencias “sudo addgroup Docker” para crear el grupo Docker aunque debe estar creado ya y “sudo adduser raulsm Docker” para añadir nuestro usuario al grupo Docker.

2. Comprobamos que funciona correctamente con este comando: “sudo Docker run debian echo “hola mundo”

3. Ahora hacemos una prueba de tipo holamundo basada en ubuntu.

El comando es "sudo Docker run ubuntu echo “hola mundo”

## Practica 1.20 Uso basico de imagenes

1.Crea un contenedor interactivo. No le pongas nombre. Ejecuta alguna orden básica de la shell. Indica alguna orden básica que esté disponible y alguna otra que no.

El comando necesario es “sudo docker run -it Ubuntu” . Entramos en root y comprobamos que las sentencias que funcionan son ls, ls -l y cd y que por el contrario, la sentencia sudo no funciona.

2. El comando necesario es “sudo Docker run -it -–name raulc01 ubuntu”

3. Los comandos necesarios son "sudo docker images", “sudo docker ps -a” y  “sudo docker ps”

Aparece el docker con el nombre raulc01, un ID, una imagen en Ubuntu ...
Nos sale el docker sin nombre, un ID una imagen Ubuntu...

4.

Comando para terminar la ejecución: “sudo docker stop id_contenedor”

Comando para borrar las imágenes no utilizadas: “docker rmi $(docker images -a -q)”

Comando para borrar todos los contenedores detenidos: “docker rm $(docker ps -a -f status=exited -q)”

Comando para borrar todos los contenedores creados y nunca ejecutados: “docker rm $(docker ps -a -f status=created -q)”

Ahora los dos contenedores creados tienen el status "exited"


5. Comprueba que el sistema de ficheros dentro del contenedor no es persistente. Esto es: escribe algún fichero, apaga el contenedor, vuelva a entrar y observa que ha desaparecido.

Efectivamente han desaparecido.


## Practica 1.21 Creación de una imagen de un contenedor

Me creo una cuenta en docker hub.

Creo el directorio de contexto y creo el archivo entrypoint.sh.

 				#!/bin/bash
        banner bienvenido
        banner a
        banner $HOSTNAME

Y también creamos el fichero Dockerfile dentro del directorio contexto:

        FROM ubuntu:22.04
        RUN apt-get update && apt-get upgrade -y && apt-get install -y sysvbanner
        COPY entrypoint.sh /
        ENTRYPOINT ["/entrypoint.sh"]
        
Una vez hemos creados los dos fichero hacemos cd para volver a la maquina principal y construimos la imagen con el siguiente comando: “sudo docker build -t raulsm1/banner contexto”

Lo hago con la sentencia: “sudo docker run -h c01 –name c01 raulsm1/banner

4.Modifica la imagen para que una vez lanzada, no solo muestre el banner sino que abra una Shell

Esto se hace poniendo “/bin/bash” justo después de los banners en el entrypoint.sh

5.Lanza un contenedor con la imagen para comprobar que puedes ejecutar la shell.

Hacemos “docker run -it -h c01 –name c01 raulsm1/banner”

Imagen 1.21 del resultado en la carpeta images.

## Practica 1.22 Creacion de una imagen personalizada

En primer lugar instalaremos el paquete bsdmainutils, el cual contiene el paquete cal.

En la maquina virtual de vagrant. Hacemos un cd /vagrant para entrar a dicho repositorio (donde crearemos todos los directorios y ficheros necesarios dentro de el directorio vbox01 directamente).

Creamos el directorio cal con “mkdir cal”, hacemos cd cal y aquí creamos el directorio context con el comando “mkdir context”, entramos también en context con un cd.
Dentro de cd cal/context creamos el fichero entrypoint.sh que llevará dentro lo siguiente:
        #!/bin/bash
        cal

Le damos permisos +x a entrypoint.sh con el comando “chmod +x entrypoint.sh” y lo ejecutamos con la sentencia “./entrypoint.sh” lo cuál nos mostrara el calendario.

Después, dentro de /lagrs/cal/context creamos el archivo Dockerfile que llevará dentro lo siguiente:
        FROM ubuntu:22.04
        RUN apt-get update && apt-get upgrade -y && apt-get install -y bsdmainutils
        COPY entrypoint.sh /
        ENTRYPOINT ["/entrypoint.sh"]

Después de esto entramos en /vagrant/cal y creamos el archivo construye.sh con el comando “nano construye.sh” el cuál contiene lo siguiente:
        #!/bin/bash
        docker build -t raulsm/cal /vagrant/cal/context

Le damos permisos +x con el comando “chmod +x construye.sh” y lo ejecutamos con el comando “./construye.sh”. Nos muestra que se construyo con exito.

2.Prepara el script lanza_jpercal01.sh y lánzalo.

Creamos el archivo lanza_raulcal01.sh que contiene lo siguiente:
        #!/bin/bash
        docker run -it --name raulcal01 raulsm/cal

Le damos permisos +x con el comando “chmod +x lanza_raulcal01.sh” y lo ejecutamos con el comando “./lanza_raulcal01.sh”. Nos sale el calendario.

3.Prepara el script lanza_jpercal02.sh y lánzalo.

Ahora creamos el archivo lanza_raulcal02.sh que llevará lo siguiente:
        #!/bin/bash
        docker run -it --name raulcal02 raulsm/cal

Y le damos permisos +x con la sentencia “chmod +x lanza_raulcal02.sh” y lo ejecutamos con el comando “./lanza_raulcal02.sh”. Nos  sale el calendario.

4.Ejecuta docker ps -a y docker images, y observa que, naturalmente, se puede comprobar que ambos contenedores están basados en la misma imagen.

Por último, ejecutamos “docker ps -a” para observar que salgan las imágenes creadas:

Vemos que sí aparecen las imágenes y contenedor creadas.

## Practica 1.23 Montaje bind

Lo primero que vamos a hacer es crear la imagen y el contenedor, para ello el directorio /bind/context tendrá lo siguiente:

-Dockerfile:

FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y sysvbanner
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
RUN useradd -rm -d /home/raulsm -s /bin/bash -u 1000 raulsm
USER raulsm
WORKDIR /home/raulsm

-entrypoint.sh:

"#!/bin/bash
/bin/bash


Y el directorio /bind tendrá lo siguiente:

-construye.sh:

"#!/bin/bash
docker build -t raulsm/bind  /vagrant/bind/context
"

-lanza_raulsmbind01.sh:

"#!/bin/bash
docker run -it -h raulbind01 --name raulbind01 --rm -v /vagrant/bind:/home/raulsm raulsm/bind
"

Cabe destacar que se le dan permisos +x a los ficheros entrypoint.sh, construye.sh y lanza_raulbind01.sh con el comando "chmod +x nombre_archivo"

1.Lanza el contenedor y escribe en el directorio montado un fichero con nombre hola_raulsm

Lanzo el contenedor con las sentencias "sudo ./construye.sh"
Luego "sudo ./lanza_raulbind01.sh" .

Una vez dentro podemos ver el contenido copiado del directorio host con ls
Luego creo un archivo llamado hola_raulsm, lo hago con touch"hola_raulsm"

Cierro el contenedor y cuando lo vuelvo a lanzar, comprobamos que el archivo hola_raulsm es persistente.

Me meto en vbox01 y edito el fichero hola_raulsm con un texto.
Me meto en el contenedor y hago un cat de hola_raulsm para comprobar que tiene los cambios y asi es. TIene el mensaje que escribi fuera.



## Practica 1.24 Conectividad entre contenedores

Primero vamos a preparar la images y los contenedores.
Para ello entramos en la maquina virtual de vagrant y hacemos un "cd /vagrant/ para acceder al directorio de vbox01 donde guardaremos los directorios necesarios para crear la imagen y contenedores. Una vez ahí dentro hacemos "mkdir remoto" y "cd remoto" una vez dentro de remoto creamos el directorio context con "mkdir context" nos metemos en context con "cd context" y creamos el entrypoint.sh el cual llevará lo siguiente: 

"#!/bin/bash
/usr/sbin/sshd &
/bin/bash 
"

el /bin/bash para crear la shell y el /usr/sbin/sshd para tener instalado el sshd.
También crearemos el Dockerfile que llevará lo siguiente:

FROM ubuntu:22.04
RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y net-tools && \
apt-get install -y iputils-ping && \
apt-get install -y openssh-server && \
apt-get install -y locales && \
localedef -i es_ES -c -f UTF-8 -A /usr/share/locale/locale.alias es_ES.UTF-8
RUN mkdir /var/run/sshd
ENV LANG es_ES.UTF-8
COPY entrypoint.sh /
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]

lleva los comandos para instalar el ifconfig y ping, instalar el idioma español, tambien para poder hacer sshd...

Una vez creados el Dockerfile y entrypoint.sh volvemos a /remoto y crearemos el construye.sh que llevará lo siguiente:

"#!/bin/bash
docker build -t raulsm/remoto /vagrant/remoto/context
"

y creamos los dos lanza que llevarán lo siguiente, el lanza_raulremoto01.sh:

"#!/bin/bash
docker run -it -h raulremoto01 --name raulremoto01 raulsm/remoto
"

y el lanza_raulremoto02.sh:

"#!/bin/bash
docker run -it -h raulremoto02 --name raulremoto02 raulsm/remoto
"

cabe decir que le tenemos que dar permisos +x con la sentencia "chmod +x nombre_fichero" tanto al entrypoint.sh como al construye.sh como al lanza_raulremoto01.sh como al lanza_raulremoto02.sh .

Una vez que estén listas las imágenes, lanzo ambos contenedores.

1.Averigua su dirección IP.

Primero lanzamos el construye.sh y después el lanza_raulremoto01.sh y el lanza_raulremoto02.sh . Una vez dentro de ambos contenedores podemos mirar su IP a través del comando ifcofig: 

Podemos ver que la dirección IP del contenedor 1 es 172.17.0.2 y la del contenedor 2 es 172.17.0.2


2.Haz ping a tu propio contenedor.

Realizo un ping desde el contenedor 1 hasta el mismo con la sentencia "ping 172.17.0.2". Funciona.

3.Usando netstat, comprueba que el servidor sshd está funcionando. Pero no instales netstat en la imagen, instálalo solo en este contenedor en particular para esta prueba concreta (esto es, de forma interactiva).

Podemos ver si sshd esta funcionando a través de netstat lanzando la sentencia "netstat -tupan" en los contenedores.
Comprobamos que el sshd sí está funcionando.

4.Entra por ssh en tu contenedor.

Entramos por ssh al contenedor 1 utilizando el comando "ssh raulsm@172.17.0.2"

5.Comprueba que puedes hacer ping al otro contenedor.

Hacemos ping al contenedor 2 con la sentancia "ping 172.17.0.2"

6.Abre una sesión en el otro contendor.

Podemos abrir una sesión en el otro contenedor perfectamente, simplemente lanzandolo.

##Práctica 1.25 sshfs

He realizado una prueba llevándome una copia del directorio /home/alumnos/raulsm/lagrs/vbox01 a mi directorio ∼/Escritorio de mi ordenador personal. Lo he podido hacer con la ayuda de la sentencia: "sshfs -C raulsm@f-l3207-pc19/lagrs/vbox01:/∼/Escritorio /Escritorio/vbox01" a través de la conexión sshfs. 

Obviamente descargué previamente sshfs en mi maquina de casa con la sentencia sudo apt-get install sshfs, si no no se podría realizar la conexión sshfs. Ya podríamos trabajar en casa como en el laboratorio, con le directorio vbox01.


## Práctica 1.26 Contenedor con sshfs

1.Prepara la imagen con los paquetes necesarios, la configuración en español y un usuario.

Preparo la imagen con los paquetes necesarios que serán los siguientes:

Dentro del directorio /cssh/context tendremos:

-Dockerfile:

FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y locales && \
localedef -i es_ES -c -f UTF-8 \
-A /usr/share/locale/locale.alias es_ES.UTF-8
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y sudo && \
apt-get install -y openssh-server && \
apt-get install -y openssh-client && \
sudo apt-get install -y sshfs
RUN useradd -rm -d /home/raulsm -s /bin/bash -u 1001 raulsm
RUN service ssh start
ENV LANG es_ES.UTF-8
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

-entrypoint.sh:
"#!/bin/bash
 /bin/bash
"

Después crearemos dentro del directorio /cssh  los ficheros construye.sh y lanza_raulcssh01.sh con lo siguiente:

-construye.sh:
"#!/bin/bash
docker build -t raulsm/cssh context
"
-lanza_raulcssh01.sh:
"#!/bin/bash
docker run --cap-add SYS_ADMIN --device /dev/fuse --security-opt apparmor:unconfined -it -h raulcssh01 --name raulcssh01 --rm raulsm/cssh
"
Cabe destacar que a los ficheros entrypoint.sh, construye.sh y lanza_raulcssh.sh le hemos dado permisos +x con la sentencia "chmos +x nombre_archivo"

2.Lanza el contenedor con las opciones necesarias para usar sshfs.

Como siempre lanzamos primero el construye.sh con la sentencia "./construye.sh" y luego el lanza con la sentencia "./lanza_mraulcssh02.sh"

3.Empieza probando sshfs desde el usuario root del contenedor:

-Monta el directorios /tmp de una máquina cualquiera de las que estén disponibles en el laboratorio (consulta el parte de guerra). Por ejemplo f-l2108-pc05 en el directorios /tmp/pc05 del contenedor. (Esto es, el directorio local será /tmp/pcNN, siendo NN el número del puesto)

-Comprueba que el resultado es el esperado: entra por ssh en esa máquina, edita algún fichero en el directorio /tmp/, comprueba que puedes editar el mismo fichero en el directorio montado en tu máquina local.

Primero voy a comprobar que puedo hacer ssh desde el contenedor a mi maquina del laboratorio:

Mi maquina del laboratorio es la @f-l3103-pc09 por tanto voy a crear un directorio /tmp/pc09 dentro del contenedor:

root@raulbcssh01:/# mkdir /tmp/pc09
root@raulcssh01:/# sshfs -C raulsm@f-l3103-pc09:/tmp /tmp/pc09
raulsm@f-l3103-pc09's password: 
root@raulcssh01:/# cd /tmp/pc09

Despues de esto, creo un fichero desde la maquina del laboratorio en ese directorio llamado prueba.txt y compruebo en le contenedor que le aparece dicho fichero que acabo de crear:

root@raulcssh01:/tmp/pc09# ls
prueba.txt

Voy a probar a editarlo desde el contenedor para comprobar si se actualiza en la maquina del laboratorio:

root@raulcssh01:/tmp/pc09# echo "Retocando el fichero prueba.txt desde el contenedor" >> /tmp/pc09/prueba.txt

Compruebo que puedo ver los cambios desde la maquina del laboratorio:

Efectivamente se han incorporado los cambios.

4.Ahora repite el paso anterior pero con tu usuario del contenedor, no con el usuario root.

Vmos a repetir el mismo procedimiento pero a la inversa, voy a retocar el archibo prueba.txt desde la maquina del laboratorio y voy a comprobar si dichos cambios le llegan al contenedor:

Escribo en el archivo desde la maquina del laboratorio lo siguiente: "Retocando el fichero prueba.txt desde la maquina del laboratorio"

Comprobamos desde el contenedor que si son visibles los cambios.

## Práctica 1.27 Contenedor con fichero hosts

Primero vamos a crear el fichero delta_hosts dentro del context del contenedor, este estará en ~/lagrs/vbox01/chosts/context. Dentro de delta_hosts copiaremos el contenido de /etc/hosts, se puede hacer de varias maneras por ejemplo "cat /etc/hosts > delta_hosts".

Ahora empezamos a preparar los contenedores, dentro del directorio /chosts/context tendremos:

-Dockefile: queremos que tenga las especificaciones del enunciado (que se pueda hacer ssh, ifconfig, que esté delta_hosts en /tmp...)
FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y && \
apt-get install -y iputils-ping && \
apt-get install -y net-tools && \
apt-get install -y openssh-server && \
apt-get install -y openssh-client
RUN service ssh start
COPY entrypoint.sh /
COPY delta_hosts /tmp
ENTRYPOINT ["/entrypoint.sh"]

-entrypoint.sh:
"#!/bin/bash
cat /tmp/delta_hosts >> /etc/hosts
/bin/bash
"
A parte del ya mencionado delta_hosts.

Por otro lado en el directorio /chosts tendremos:

-construye.sh:
"#!/bin/bash
docker build -t raulsm/chosts context
"

-lanza_raulchosts01.sh:
"#!/bin/bash
docker run -it -h raulchosts01 --name raulchosts01 --rm raulsm/chosts
"

-lanza_raulchosts02.sh:

"#!/bin/bash
docker run -it -h raulchosts02 --name raulchosts02 --rm raulsm/chosts
"

Daremos permisos +x como siempre a los ficheros entrypoint.sh, construye.sh, lanza_raulchosts01.sh y lanza_raulchosts01.sh 

lanzamos el contenedor y comprobamos que se ha copiado el fichero delta_hosts en el directorio /tmp del contenedor:


Efectivamente el fichero delta_hosts está en el directorio /tmp del contenedor.

Vemos si se ha copiado lo correspondiente en /etc/hosts hciendo un cat /etc/hosts:


Efectivamente se ha añadido la información correctamente a /etc/hosts

Comprobamos que funcione el ifconfig:


Y también comprobamos que funcione un ping a cualquier máquina del laboratorio:


Por último voy a acceder a cualquier máquina del laboratorio por ssh para comprobar que funciona:

Vemos que funciona perfectamente.
Cabe destacar que todo esto ha sido comprobado tanto en el contenedor raulchosts01 como en el raulchosts02 y funciona perfectamente en ambos.



