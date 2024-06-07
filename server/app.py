import hashlib
import random
import json
from flask import Flask, request, jsonify, send_file, send_from_directory, redirect, url_for
import datetime

app = Flask(__name__)

# Archivo donde se guarda el hash
DOCKER_FILE_PATH = "dockerlab.txt"
VALIDATED_HASH_PATH = "hash_validado.txt"

def generate_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

def read_hash(file_path):
    with open(file_path, 'r') as file:
        return file.readline().strip()

def write_hash(hash_value, file_path):
    with open(file_path, 'w') as file:
        file.write(hash_value)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/jugadores')
def get_jugadores():
    return send_from_directory('.', 'jugadores.txt')

@app.route('/hash/generado', methods=['GET'])
def get_generated_hash():
    try:
        generated_hash = read_hash(DOCKER_FILE_PATH)
        return jsonify({"hash": generated_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/hash/validado', methods=['GET'])
def get_validated_hash():
    try:
        validated_hash = read_hash(VALIDATED_HASH_PATH)
        return jsonify({"hash": validated_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/validacion/hash', methods=['POST'])
def validar_hash():
    try:
        # Obtener el nombre del jugador y el hash del formulario
        nombre_jugador = request.form.get('nombre')
        hash_value = request.form.get('hash')
        
        
        # Print Content-Type header to debug
        print("Content-Type:", request.headers.get('Content-Type'))
        
        # Check if Content-Type header is set to 'application/json'
        if request.headers.get('Content-Type') == 'application/json' or request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
            # Manejar tanto JSON como form data
            if request.headers.get('Content-Type') == 'application/json':
                data = request.get_json()
                hash_value = data.get('hash')
            elif request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
                hash_value = request.form.get('hash')
            
            # Resto del código para validar el hash

            # Obtener el hash actual
            old_hash = read_hash(DOCKER_FILE_PATH)

            # Validar si el hash enviado coincide con el hash actual
            if hash_value == old_hash:
                # Si coincide, se actualiza el hash validado
                write_hash(hash_value, VALIDATED_HASH_PATH)
                # Se genera un nuevo hash
                new_hash = generate_hash(str(random.random()))
                # Se actualiza el hash en el archivo
                write_hash(new_hash, DOCKER_FILE_PATH)
                
                # Obtener la fecha y hora actual
                now = datetime.datetime.now()
                fecha_hora_actual = now.strftime("%Y-%m-%d %H:%M:%S")
                
                # Guardar el nombre del jugador junto con la fecha y hora en un archivo de texto
                with open('jugadores.txt', 'a') as file:
                    file.write(f"{nombre_jugador} - {fecha_hora_actual}\n")
            
                # Se retorna el nuevo hash para validar
                #return jsonify({"valid": False, "nuevo_hash": new_hash})
                return redirect(url_for('index'))
            else:
                # Si no coincide, se indica que el hash es válido
                #return jsonify({"valid": True})
                return redirect(url_for('index'))
        else:
            # If Content-Type is not 'application/json', return an error response
            return jsonify({"error": "Unsupported Media Type"}), 415
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
