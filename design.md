Diseño y decisiones de arquitectura
🔹 Objetivo
Construir una página de detalle de producto inspirada en MercadoLibre, con un backend RESTful y datos locales (JSON), evitando bases de datos reales.

✅ Frontend
Stack elegido:

Angular

TailwindCSS

Estructura:

Componente principal: product-page

Subcomponentes:

product-gallery

product-info

product-description

product-buy-box

method-payment

seller-info

recommended-products

related-products

Decisiones de diseño:

Angular ofrece estructura modular, fácil enrutamiento y soporte para pruebas unitarias.

Tailwind permite un diseño responsivo y consistente de forma rápida.

Componentización facilita el mantenimiento y el desarrollo incremental, imitando la estructura de MercadoLibre.

Responsiveness:

Uso de Tailwind Grid y Flex.

Media queries adaptativas.

Imágenes escalables.

✅ Backend
Stack elegido:

Python

Flask

Arquitectura:

Inspirada en Clean/Hexagonal:

api/routes (exposición HTTP)

application/use_cases (lógica de negocio)

domain/models (entidades)

infrastructure/repositories (persistencia local en JSON)

Datos locales:

Archivos JSON:

products.json

payment_methods.json

recommended_products.json

related_products.json

Decisiones de diseño:

Flask es ligero, fácil de configurar y adecuado para prototipos rápidos.

Separación en capas mejora mantenibilidad y testabilidad.

Uso de JSON local cumple la restricción de no usar base de datos real.

✅ Principales Desafíos y Soluciones
Desafío	Solución Implementada
Mantener datos consistentes sin DB	Archivos JSON bien estructurados y validados al leer
Responder rápido con Flask	Rutas desacopladas y limpias con Blueprints
Garantizar >80% cobertura en backend	Pruebas Pytest con mocks de archivos locales
Diseño responsivo similar a Meli	Tailwind + Angular grid/flex layout
Comunicación frontend-backend	Servicios Angular con HttpClient
Organización de carpetas	Modular tanto en Angular como en Flask

✅ Conclusión
El proyecto separa claramente frontend y backend, usa tecnologías modernas pero sencillas, y cumple con las restricciones del reto (datos locales, API RESTful, diseño similar a MercadoLibre).

El resultado es fácilmente mantenible, extensible y comprensible para nuevos desarrolladores.