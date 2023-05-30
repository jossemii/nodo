import os
import time

import docker
from tabulate import tabulate

def containers():
    # Crear una instancia del cliente de Docker
    client = docker.from_env()

    while True:
        # Borrar la consola
        os.system('clear')

        # Obtener la lista de contenedores en ejecución
        contenedores = client.containers.list()

        # Crear una lista para almacenar los datos de cada contenedor
        datos_contenedores = []

        # Recorrer los contenedores y obtener los datos relevantes
        for contenedor in contenedores:
            servicio = contenedor.image.tags[0]
            creado = contenedor.attrs['Created']
            puertos = contenedor.attrs['HostConfig']['PortBindings']
            nombre = contenedor.name

            # Agregar los datos a la lista
            datos_contenedores.append([servicio, creado, puertos, nombre])

        # Mostrar la tabla de datos
        headers = ['SERVICE', 'CREATED', 'PORTS', 'NAMES']
        print(tabulate(datos_contenedores, headers=headers, tablefmt="plain"))

        # Esperar dos segundos antes de refrescar
        time.sleep(2)
