# learning-python
Este es un repositorio de scripts en lenguaje de programación Python para el Diplomado en Inteligencia Computacional.

# Proceso staging

Primer comando: Enviar paquete a staging o a cola
$git add . / $git add --all / git add FILE_NAME.ext / git add FOLDER_NAME

Segundo comando: Anexar mensaje - ¿Qué contiene el paquete?
$git commit -m "AQUÍ VA EL MENSAJE"   //-m significa message

Tercer comando: Enviar o desplegar el paquete hacia su destino (RAMA).
$git push origin NOMBRE_RAMA/BRANCH_NAME / $git push

# Comandos para hacer seguimiento del staging:

$git status (Verificar el estado del staging del repositorio)
$git reset FILE_NAME.ext (Saca el archivo de cola de staging)
$git restore --staged FILE_NAME.ext
$git log (Ver la trazabilidad o log de cambios realizados)
