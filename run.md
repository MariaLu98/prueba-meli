Instrucciones para ejecutar el proyecto
Este proyecto contiene:

Backend (webapi): API REST en Python/Flask

Frontend (webapp): Aplicación Angular + TailwindCSS

🔹 Requisitos previos
Node.js (≥ 16 recomendado)

npm (≥ 9 recomendado)

Python 3.10 o superior

pip

## 1. Levantar el Backend (webapi)
a. Instalar dependencias
bash
Copy
Edit
cd webapi
pip install -r requirements.txt
b. Variables de entorno (opcional)
Hay un archivo .env con configuraciones de ejemplo.

c. Ejecutar servidor
nginx
Copy
Edit
python -m api.app
Por defecto se inicia en:

cpp
Copy
Edit
http://127.0.0.1:8000
d. Datos locales
La API lee datos desde archivos JSON en:

bash
Copy
Edit
infrastructure/data/
## 2. Levantar el Frontend (webapp)
a. Instalar dependencias
bash
Copy
Edit
cd ../webapp
npm install
b. Servir aplicación
sql
Copy
Edit
npm start
Por defecto se abre en:

arduino
Copy
Edit
http://localhost:4200
## 3. Ejecutar Tests
# Backend
bash
Copy
Edit
cd webapi
pytest --cov
Verifica cobertura ≥80%

# Frontend
bash
Copy
Edit
cd ../webapp
npm run test
Incluye pruebas unitarias en Karma/Jasmine.

## 4. Observaciones
Todos los datos están en archivos locales JSON, cumpliendo la restricción de no usar base de datos real.

El backend ofrece endpoints RESTful para detalle de producto, métodos de pago, productos recomendados y relacionados.

El frontend consume esos endpoints para construir la vista de producto estilo MercadoLibre.