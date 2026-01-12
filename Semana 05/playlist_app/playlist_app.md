# 🎧 Analizador de Playlists

## 📝 Descripción del programa
Este programa es una aplicación desarrollada en Python cuyo propósito principal es el análisis de playlists a partir de sus características y de los hábitos de consumo del usuario.

La aplicación evalúa características como el formato del contenido, la duración de la playlist y las interacciones del usuario (reproducciones, likes, comentarios y compartidos) para inferir el tipo de usuario y ofrecer recomendaciones generales sobre el uso de la playlist.

Este proyecto ha sido desarrollado como parte de la práctica de tipos de datos, identificadores y convenciones de nomenclatura en Python.

---

## 🎯 Objetivo de la Aplicación
El objetivo de la aplicación es aplicar los conocimientos de programación estructurada y orientada a objetos para:

* **Analizar Playlists**: Evaluar duración, formato y características generales del contenido.

* **Procesar Hábitos de Consumo**: Analizar interacciones del usuario mediante el modelo ListeningHabits.

* **Determinar el Perfil de Usuario**: Identificar automáticamente si el usuario es consumidor, participativo, creador o una combinación de estos perfiles, basándose en su comportamiento.

* **Generar Recomendaciones Generales**: Sugerir contextos de uso de la playlist según su duración y formato.

---

## 🛠️ Detalles Técnicos (Criterios de Evaluación)

### 1. Tipos de Datos Implementados
Se emplean los tipos de datos nativos de Python de la siguiente manera:
* **Integer (`int`)**: Contadores de reproducciones y número de canciones.
* **Float (`float`)**: Duración promedio de canciones y duración total de la playlist.
* **String (`str`)**: Nombres de playlists, formatos de contenido, tipo de usuarios y más.
* **Boolean (`bool`)**: Indicadores de interacción del usuario (likes, comentarios, compartidos, creador).

### 2. Identificadores y Convenciones
Siguiendo las mejores prácticas de la comunidad (PEP 8):
* **snake_case**: Todas las variables y funciones utilizan nombres descriptivos en minúsculas unidos por guiones bajos (ej. `calculate_total_duration`).
* **CamelCase**: Se utiliza para las clases (ej. `User`, `PlaylistDetails`).



### 3. Documentación y Comentarios
El código fuente cuenta con:
* **Docstrings**: Explicación al inicio de cada función.
* **Comentarios de línea**: Breves explicaciones sobre la lógica de los cálculos de duración y filtros de usuario.

---

## 📂 Estructura del Repositorio

La arquitectura del software está dividida de forma modular:

* `main.py`: El punto de entrada que orquesta la ejecución del programa.
* `modelos/`: Contiene las clases que definen los tipos de datos (Usuario, Detalles de Playlist, Hábitos).
* `servicios/`: Contiene la lógica de procesamiento y el algoritmo de recomendación (`PlaylistService.py`).
* `__pycache__/`: Archivos compilados por Python para mejorar la velocidad de ejecución.

---

## 🚀 Cómo Ejecutar el Programa

1.  **Clonar el repositorio**:
2.  **Abrir en IDE**: Abrir la carpeta raíz en **PyCharm** o **Visual Studio Code**.
3.  **Ejecutar**:
    ```bash
    python main.py
    ```