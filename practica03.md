##Práctica 3.1. FHS

2014.01. Ejercicio 2 Cuando se crea un usuario nuevo se copia en su home el directorio /etc/skel. Si lo borras, seguirá existiendo en los usuarios ya creados pero al crear un usuario nuevo tendrás un problema.

2014.01. Ejercicio 3: El SUID en un ejecutable hará que cuando lo ejecute cualquier usuario, los permisos del proceso sean los del dueño del fichero en vez de los de quien ejecuta. Para un script no tiene sentido ya que un script no se ejecuta, lo interpreta un intérprete (el cual si es ejecutable). Que un intérprete tenga el bit SUID activado si que tiene consecuencias y muy peligrosas. Su dueño es root, por lo que si tiene SUID, sea quien sea quien ejecute el intérprete, tendrá siempre permisos de root.

2014.01. Ejercicio 4: Por convenio, lo renombramos para que acabe en d. Para la configuración de puesta en marcha y parada habrá que crear el script /etc/init.d/ups Para que se ejecute y deje de ejecutar cuando deseemos, tenemos que crear los ficheros que servirán de enlace simbólico al script en sus correspondientes niveles. Iniciarlo: /etc/rc2.d y terminarlo: /etc/rc0.d y /etc/rc6.d

2014.06. Ejercicio 1: Los ficheros pueden estar referenciados por distintos enlaces, con distintos nombres. Estas "flechas" van en el sentido del nombre al fichero, y no a la inversa, por lo que desde un fichero no podemos llegar a sus nombres, solo podemos saber el número de referencias que existen al fichero porque se almacena en el inodo.

2014.06. Ejercicio 2: El journal permite reparar inconsistencias causadas por ejemplo un apagón durante la copia de un fichero. Básicamente, primero apunta lo que se va a hacer y luego lo hace, de forma que si el trabajo se queda a medias, se puede arreglar de cierta forma y no estropearse el sistema de ficheros.

2014.06. Ejercicio 3: El formato .tgz es general para Linux y el .deb es específico para Debian. Si tenemos Debian o derivado de Debian deberíamos usar el .deb, aunque el .tgz también funcionará pero tendremos que resolver a mano las dependencias e incompatibilidades. Si tenemos otro Linux deberemos usar el .tgz ya que el .deb no funcionará.

2015.01. Ejercicio 4: La secuencia #! indica que a continuación se indica el path del ejecutable que sabe interpretar ese texto. Si no aparece esa línea, se ejecutará el intérprete por omisión. Quizá tengamos suerte y lo entienda o quizá no. Si el script no tiene permiso de ejecución dará error al intentar ejecutarlo. Como opción alternativa se le puede pasar al intérprete por stdin (esquivando la ejecución del fichero).

2015.06. Ejercicio 2: /dev/sda1 es una de las particiones de sda (SCSI disk a) Si se deniega el acceso es probablemente porque no está montado.

2017.12. Ejercicio 1: VT-x es una tecnología propia del procesador Intel que permite la virtualización nativa.

2017.12. Ejercicio 2: La shell consulta los directorios indicados en PATH por lo tanto encontrará el fichero y lo podrá ejecutar. Sin embargo, la variable PATH es local a la shell, y cuando iniciemos un terminal nuevo no estará "actualizada". Para que se actualice siempre, debemos incluir el comando correspondiente en el script .bashrc que se ejecuta al iniciar un terminal (export...).

2017.12. Ejercicio 3: /lib contiene librerías esenciales para los ejecutables del sistema. /usr/lib contiene librerías para ejecutables de menor importancia. /usr/local/lib contiene librerías de programas no estándar de la distribución.

2018.12. Ejercicio 3: Al salir y entrar se ejecuta un proceso nuevo y se vuelven a leer esos ficheros. Utilizando la orden source obtenemos ese resultado sin tener que salir y entrar y así mantenemos el contexto de la shell.


##Práctica 3.2 Recode

He creado tres ficheros y he copiado información de páginas web. Compruebo su codificación usando file :
raulsm@f-l3103-pc11:~/lagrs$ mkdir practica03/recode
raulsm@f-l3103-pc11:~/lagrs$ cd practica03
raulsm@f-l3103-pc11:~/lagrs/practica03$ ls
recode
raulsm@f-l3103-pc11:~/lagrs/practica03$ cd recode
raulsm@f-l3103-pc11:~/lagrs/practica03/recode$ nano fichero1.txt
raulsm@f-l3103-pc11:~/lagrs/practica03/recode$ nano fichero2.txt
raulsm@f-l3103-pc11:~/lagrs/practica03/recode$ nano fichero3.txt
raulsm@f-l3103-pc11:~/lagrs/practica03/recode$ file fichero1.txt
fichero1.txt: ASCII text

Todos los ficheros tienen el mismo formato.

Para comprobar la codificación de mi máquina uso echo $LANG:

raulsm@f-l3103-pc11:~/lagrs/practica03/recode$ echo $LANG
es_ES.UTF-8

Ahora cambio la codificación de estos ficheros:

raulsm@f-l3109-pc38:~/lagrs/practica03/recode$ recode ASCII..utf-16 <fichero1.txt> fichero1.utf-16.txt
raulsm@f-l3109-pc38:~/lagrs/practica03/recode$ recode ASCII..utf-16 <fichero2.txt> fichero2.utf-16.txt
raulsm@f-l3109-pc38:~/lagrs/practica03/recode$ recode ASCII..utf-16 <fichero3.txt> fichero3.utf-16.txt


##Práctica 3.3 Cron

1. Utilizamos el comando “crontab -e” e introducimos lo siguiente:

        # m h  dom mon dow   command
        * *   *   *   *    touch/tmp/test_cron_rauls

Entramos en el directorio con un cd /tmp y utilizamos el comando “grep test_cron_rauls” el cual nos devuelve lo siguiente:

rauls> ls -l | grep test_cron_rauls
-rw-rw-r-- 1 raul raul    0 dic 23 01:24 test_cron_rauls
rauls> ls -l | grep test_cron_rauls
-rw-rw-r-- 1 raul raul    0 dic 23 01:26 test_cron_rauls

2. Creamos el archivo escribe_log en el directorio /lagrs/practica03 con el comando “nano escribe_log” el cuál llevará lo siguiente:

        #!/bin/bash
        echo -n "prueba cron " >> ~/lagrs/log.txt
        date >> ~/lagrs/log.txt

Y le damos permisos +x con el comando “chmod +x escribe_log”


3. Primero editamos el fichero contab con el comando “crontab -e” en el que meteremos lo siguiente:

        # m h  dom mon dow   command
        * *   *   *   * ./lagrs/practica03/escribe_log

Para que se ejecute de lunes a viernes a las 9 de la mañana editamos el fichero crontab con el comando “crontab -e” en el que metemos:

        # m h  dom mon dow   command
        0 9  *   *   1-5./lagrs/practica03/escribe_log
        echo -n "probando cron " >> ~/lagrs/log.txt
        date >> ~/lagrs/log.txt

Y le damos permisos +x con el comando “chmod +x escribe_log”


