# Evaluación 2 - Telepresencia y Entornos Innovadores de Colaboración Humana (CUY6142)

**Estudiante:** Angel Cañizales  
**Docente:** Horacio Vega Fuentes  
**Sede:** Alonso de Ovalle  

---

## Descripción del Proyecto

Este repositorio contiene los programas desarrollados para la Evaluación Parcial N° 2 en la consultora "API Ltda." en conjunto con la Biblioteca Nacional. El proyecto se divide en dos módulos principales:

1. **Gestión de Catálogo de Biblioteca (API REST):**
   - Creación, actualización y consulta de libros mediante **Postman**.
   - Automatización de poblamiento masivo agregando 50 libros aleatorios a través del script `Ramdom50libros.py` utilizando Python (`requests` y `faker`)[cite: 1, 2].

2. **Software de Geolocalización y Rutas:**
   - Script interactivo `geolocalizacion.py` conectado a la API de GraphHopper Directions.
   - Interacción traducida al español, opción de salida (`s` / `salir`), redondeo de respuestas a dos decimales y narrativa del viaje paso a paso en español.

---

## Instrucciones de Ejecución

### 1. Script para agregar 50 libros a la biblioteca (`Ramdom50libros.py`)
Para ejecutar el script que genera y registra 50 libros aleatorios en el servidor de la biblioteca:
```bash
python3 Ramdom50libros.py
