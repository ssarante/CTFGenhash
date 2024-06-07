# CTFGenhash
este es un generador de hash para las maquinas vulnerables

# Hash Vuln Machine

Este proyecto consiste en una aplicación web que genera un hash SHA-256 aleatorio y permite a los usuarios validar ese hash. La aplicación está dividida en dos partes: el servidor (`app.py`) y el cliente (`app.py`). El servidor está escrito en Python utilizando Flask, mientras que el cliente es un script Python que hace solicitudes a la API del servidor.

## Servidor (app.py)

![image](https://github.com/ssarante/CTFGenhash/assets/39504876/d9b7e586-7db3-4f3e-b8c2-8d3f219c57e5)
![image](https://github.com/ssarante/CTFGenhash/assets/39504876/7f14f03b-9fcc-4ccc-9a23-9a5a351007ad)



El servidor está escrito en Python utilizando el framework Flask. Aquí hay un resumen de las principales funciones del servidor:

- **Generación de Hash:** Genera un hash aleatorio y lo guarda en un archivo.
- **Validación de Hash:** Permite a los usuarios validar un hash enviado a través de un formulario. Si el hash es válido, se actualiza el hash validado y se genera un nuevo hash aleatorio.
- **Obtención de Hash Generado y Validado:** Provee endpoints para obtener el hash generado y el hash validado.

Para ejecutar el servidor, simplemente ejecuta el archivo `app.py` y accede a `http://localhost:5000` en tu navegador web.

## Cliente (app.py)
![image](https://github.com/ssarante/CTFGenhash/assets/39504876/9d25ffe7-1eb6-4903-8b3e-045a1375c17d)


El cliente es un script Python que consulta la API del servidor para verificar si hay un hash válido y actualizar el hash en un archivo local en caso necesario. Aquí está una visión general de lo que hace el cliente:

- **Consulta de Hash Validado:** Consulta la API del servidor para obtener el hash validado.
- **Consulta de Hash Generado:** Consulta la API del servidor para obtener el hash generado.
- **Actualización de Hash:** Si el hash validado coincide con el hash local, actualiza el hash local con el nuevo hash generado por el servidor.

Para ejecutar el cliente, simplemente ejecuta el archivo `app.py`.

## Requisitos

- Python 3.x
- Flask
- Requests

## Instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. Instala Flask y Requests si aún no lo tienes instalado. Puedes hacerlo ejecutando `pip install Flask requests` en tu terminal.

## Uso

1. Ejecuta el servidor ejecutando el archivo `app.py` en tu terminal: `python app.py`.
2. Ejecuta el cliente ejecutando el archivo `app.py` en tu terminal: `python app.py`.
3. Observa cómo el cliente consulta la API del servidor y actualiza el hash local si es necesario.
lo ejecutando pip install Flask requests en tu terminal.
Uso
Ejecuta el servidor ejecutando el archivo app.py en tu terminal: python app.py.
Ejecuta el cliente ejecutando el archivo app.py en tu terminal: python app.py.
Observa cómo el cliente consulta la API del servidor y actualiza el hash local si es necesario.

# Uso en Batallas de Hacking

Esta aplicación puede ser utilizada en competiciones o batallas de hacking donde los participantes intentan obtener acceso a una "máquina vulnerable". La dinámica es la siguiente:

1. **Acceso a la Máquina Vulnerable:** Los participantes intentan obtener acceso a una máquina vulnerable donde se encuentra un hash aleatorio generado por la aplicación.

2. **Validación del Hash:** Una vez que un participante ha obtenido acceso a la máquina vulnerable, puede utilizar el formulario proporcionado por la aplicación para enviar el hash que ha encontrado.

3. **Validación y Generación de Nuevo Hash:** La aplicación valida el hash proporcionado por el participante. Si el hash es válido, la aplicación genera otro hash aleatorio y lo reemplaza en la máquina vulnerable.

4. **Continuación de la Competición:** Con el nuevo hash generado y cambiado en la máquina vulnerable, el próximo participante tendrá que buscar este nuevo hash .

## Características Clave

- **Evita Compartir de Hash:** Dado que el hash en la máquina vulnerable se cambia cada vez que se valida correctamente, los participantes no tienen la oportunidad de compartir el hash encontrado, lo que mantiene la competición justa y desafiante para todos.

- **Dinamismo y Desafío:** La generación dinámica de hash y la validación aseguran que cada participante se enfrente a un desafío único, lo que añade emoción y complejidad a la competición.

- **Seguimiento de Participación:** La aplicación registra los nombres de los participantes junto con la fecha y hora en que accedieron a la máquina vulnerable, lo que permite llevar un registro de la participación y el progreso de la competición.

---

Este sistema proporciona una plataforma emocionante y equitativa para competiciones de hacking, donde la habilidad y la astucia de los participantes se ponen a prueba en un entorno desafiante y dinámico.
