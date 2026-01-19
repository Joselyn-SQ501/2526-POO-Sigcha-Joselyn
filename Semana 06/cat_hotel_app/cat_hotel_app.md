# 🐱 Sistema de Gestión de Hotel para Gatos

## 📝 Descripción del programa
Este programa es una aplicación desarrollada en Python cuyo propósito principal es la gestión de un hotel para gatos a partir de sus características y detalles de los felinos.

La aplicación evalúa características como el estado de salud de los gatos, la información del hotel y los servicios disponibles para inferir la situación de cada felino y ofrecer datos relevantes de los gatos y el lugar de su hospedaje mediante un menú interactivo
en consola.

Este proyecto ha sido desarrollado como parte de la práctica de clases, objetos, herencia, encapsulamiento y polimorfismo.

---

## 🎯 Objetivo de la Aplicación
El objetivo de la aplicación es aplicar los conocimientos de programación estructurada y orientada a objetos para:

* **Gestionar Gatos**: Evaluar estado de salud, información básica y características generales de los felinos.

* **Procesar Información del Hotel**: Analizar servicios, habitaciones y datos del establecimiento mediante el modelo CatHotelDetails.

* **Determinar el Estado de los Gatos**: Identificar automáticamente si el gato está adoptado, disponible o con problemas de salud, basándose en su información.

---

## Detalles Técnicos (Criterios de Evaluación)

### 1. Clases e Herencia
- Se implementa una **clase base** (`Cats`) y una **clase derivada** (`DetailsCats`)
  que hereda atributos y métodos de la clase base.
- La clase derivada extiende la funcionalidad agregando color, edad, estado
  de salud, adopción, historial médico y descripción.

### 2. Encapsulación
- Se aplican **atributos privados** en ambas clases (ej. `__name_cats`, `__age_cats`,
  `__health_status_cats`) para proteger los datos internos.
- Los atributos privados se acceden o modifican mediante **métodos getter y setter**,
  controlando el acceso.

### 3. Polimorfismo
- Se demuestra **polimorfismo** al usar objetos de la clase hija `DetailsCats`
  a través de métodos heredados de la clase base (`get_Information_Cats`),
  mostrando cómo un mismo método puede comportarse según el tipo de objeto.
- Esto permite que los métodos trabajen con objetos diferentes sin depender de
  la clase específica.

### 4. Instancias y Uso de Métodos
- Se crean instancias de las clases (`gato_simple`, `gato_detallado`) para registrar
  información de los gatos.
- Se utilizan los métodos definidos en cada clase para mostrar información,
  actualizar estado de salud, registrar adopciones y agregar descripciones.

### 5. Documentación y Comentarios
- Todas las funciones y métodos incluyen **docstrings** explicativos.  
- Se agregaron **comentarios de línea** donde es necesario, explicando la lógica
  y el flujo de la aplicación (registro de gatos, adopciones, actualización
  de información, etc.).
---

## 📂 Estructura del Repositorio

La arquitectura del software está dividida de forma modular:

 - `models/` → Contiene las clases que representan los datos (`Cats`, `DetailsCats`, `CatHotelDetails`).
  - `services/` → Contiene la lógica del sistema (`CatsServices`).
  - `main.py` → Archivo principal para ejecutar la aplicación y mostrar el menú interactivo.
---

## 🚀 Cómo Ejecutar el Programa

1. **Clonar el repositorio**:
2. **Abrir en IDE**: Abrir la carpeta raíz en **PyCharm** o **Visual Studio Code**.
3. **Ejecutar**:
    ```bash
    python main.py
    ```