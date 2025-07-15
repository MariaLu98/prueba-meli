Proyecto: Item Detail Page (Estilo MercadoLibre)
Este proyecto es un prototipo completo que incluye:

✅ Frontend en Angular + TailwindCSS
✅ Backend en Python/Flask con datos locales en JSON
✅ Inspiración en el diseño de la página de detalle de producto de MercadoLibre

🗂️ Estructura del repositorio
Copy
Edit
/
├── webapi/   → Backend Flask
└── webapp/   → Frontend Angular
✅ Descripción general
🎯 Objetivo
Construir una página de detalle de producto que muestre:

Imágenes de producto

Título y descripción

Precio

Métodos de pago

Información del vendedor

Stock, calificaciones o detalles adicionales

El backend expone endpoints RESTful para servir toda la información usando archivos locales en JSON, cumpliendo con la restricción de no usar bases de datos reales.

✅ Tecnologías utilizadas
🖥️ Frontend (webapp)
Angular

TailwindCSS

TypeScript

🗄️ Backend (webapi)
Python 3

Flask

Archivos locales JSON como fuente de datos

✅ Instrucciones de ejecución
Consulta el archivo run.md para ver los pasos detallados para instalar dependencias, levantar ambos servidores y ejecutar las pruebas.

En resumen:

bash
Copy
Edit
# Backend
cd webapi
pip install -r requirements.txt
python -m api.app

# Frontend
cd ../webapp
npm install
npm start
✅ Testing
Backend: pytest --cov (con cobertura ≥80%)

Frontend: npm run test (Jasmine/Karma)

✅ Diseño y decisiones técnicas
Consulta el archivo design.md para una explicación detallada de:

Decisiones de stack

Arquitectura del proyecto

Estructura de carpetas y componentes

Desafíos encontrados y soluciones implementadas

✅ Requisitos cumplidos
✔️ API RESTful sin base de datos real

✔️ Datos persistidos en archivos JSON

✔️ Página responsiva y modular

✔️ Cobertura de código ≥80% en el backend

✔️ Documentación completa

✅ Autora
Lucía Colorado

