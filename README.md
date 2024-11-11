# Proyecto Pokédex: Consumo de la API de Pokémon
Este proyecto consiste en la construcción de una Pokédex utilizando la API pública de Pokémon (PokéAPI). El programa permite al usuario ingresar el nombre de un Pokémon y obtener información detallada sobre él, incluyendo su imagen, estadísticas como peso, tamaño, habilidades, movimientos y tipos. Además, el proyecto guarda los datos en un archivo JSON en una carpeta llamada pokedex.

Funcionalidades
El usuario ingresa el nombre de un Pokémon.
El programa realiza una solicitud a la PokéAPI para obtener información sobre el Pokémon.
Si el Pokémon existe, muestra la imagen del Pokémon y sus estadísticas:
Peso
Tamaño
Habilidades
Tipos
Movimientos
Si el Pokémon no es encontrado, muestra un mensaje de error.
Guarda los datos completos del Pokémon (junto con el enlace de la imagen) en un archivo .json dentro de una carpeta llamada pokedex.
Requisitos
Este proyecto requiere las siguientes librerías de Python:

requests: Para realizar solicitudes HTTP a la API y obtener los datos del Pokémon.
matplotlib: Para mostrar la imagen del Pokémon.
Pillow (PIL): Para abrir y procesar la imagen descargada desde la API.
json: Para guardar los datos del Pokémon en formato JSON.
os: Para crear directorios y manejar archivos locales.
Puedes instalar las librerías necesarias con el siguiente comando:

bash
Copiar código
pip install requests matplotlib Pillow
Uso
Clona este repositorio o descarga los archivos del proyecto.

Ejecuta el script principal pokedex.py desde tu terminal o editor de código.

bash
Copiar código
python pokedex.py
El programa te pedirá que ingreses el nombre de un Pokémon. Por ejemplo, puedes probar con pikachu o charizard.

Si el Pokémon existe, el programa te mostrará su imagen y detalles como:

Tipo
Peso
Tamaño
Habilidades
Movimientos
La información del Pokémon se guardará en un archivo JSON dentro de la carpeta pokedex.

Ejemplo de salida:
makefile
Copiar código
******POKEDEX******
Dime el nombre del Pokémon: pikachu
Pokémon:    pikachu
Tipo:       electric
Peso:       13.2 lbs
Tamaño:     4.0 cm
Habilidades: ['static', 'lightning-rod']
Movimientos:
    quick-attack
    tackle
    electro-ball
    ...
La imagen del Pokémon también se mostrará utilizando matplotlib.

Estructura del Proyecto
El proyecto tiene la siguiente estructura de directorios:

bash
Copiar código
pokedex/
│
├── pokedex.py                # Script principal que consume la API y muestra los datos.
├── pokedex/                  # Carpeta donde se guardarán los archivos .json de los Pokémon.
│   └── pokemon.json          # Ejemplo de archivo JSON con los datos del Pokémon.
└── README.md                 # Este archivo.
Explicación del Código
Paso 1: Solicitud a la API
El programa realiza una solicitud GET a la API de Pokémon utilizando la librería requests. La URL de la API se construye a partir del nombre del Pokémon proporcionado por el usuario.

Paso 2: Procesamiento de los Datos
Los datos recibidos en formato JSON se procesan para extraer la siguiente información:

Nombre
Tipo(s)
Peso
Tamaño
Habilidades
Movimientos
Imagen
Paso 3: Visualización
La imagen del Pokémon se descarga y muestra usando la librería matplotlib.

Paso 4: Guardado de Datos
Los datos del Pokémon se guardan en un archivo JSON dentro de la carpeta pokedex/, con un nombre que corresponde al nombre del Pokémon.

Paso 5: Manejo de Errores
Si el nombre del Pokémon no es válido, el programa muestra un mensaje de error y termina la ejecución.

Contribuciones
Si deseas contribuir a este proyecto, puedes hacerlo de las siguientes maneras:

Enviar un pull request con mejoras o nuevas características.
Reportar issues o sugerencias de mejora.
Aprendizajes del Proyecto
En este proyecto, he aprendido:

Manejo de APIs: Cómo realizar solicitudes HTTP a una API externa y procesar los datos en formato JSON.
Uso de librerías: Cómo utilizar librerías como requests, matplotlib y Pillow para obtener datos, mostrar imágenes y procesar archivos.
Estructura de directorios: Cómo manejar directorios y archivos en Python, y cómo crear directorios automáticamente si no existen.
Interacción con el usuario: Cómo recibir entradas del usuario, validar las respuestas y mostrar mensajes de error cuando es necesario.
