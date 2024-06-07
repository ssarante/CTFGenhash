import requests
import schedule
import time

def consultar_hash_validado_y_modificar(url_de_la_api, archivo_de_hash):
    try:
        response = requests.get(url_de_la_api + '/hash/validado')
        if response.status_code == 200:
            data = response.json()
            if "hash" in data:
                hash_validado = data["hash"]
                with open(archivo_de_hash, 'r') as file:
                    hash_en_archivo = file.read().strip()
                if hash_validado == hash_en_archivo:
                    nuevo_hash_response = requests.get(url_de_la_api + '/hash/generado')
                    if nuevo_hash_response.status_code == 200:
                        nuevo_hash = nuevo_hash_response.json()["hash"]
                        with open(archivo_de_hash, 'w') as file:
                            file.write(nuevo_hash)
                        print("Se ha modificado el archivo con el nuevo hash:", nuevo_hash)
                    else:
                        print("Error al obtener el nuevo hash:", nuevo_hash_response.status_code)
                else:
                    print("El archivo de hash no coincide con el hash validado en la URL.")
            else:
                print("La respuesta no contiene la clave 'hash'.")
        else:
            print("Error al hacer la solicitud:", response.status_code)
    except Exception as e:
        print("Se produjo un error:", str(e))

# Aquí establecemos la tarea de verificación cada 30 segundos
schedule.every(30).seconds.do(consultar_hash_validado_y_modificar, url_de_la_api='http://127.0.0.1:5000', archivo_de_hash='flaglab.txt')

# Bucle para ejecutar las tareas continuamente
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print("Se ha detenido la ejecución.")
        break
