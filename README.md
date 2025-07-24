# 🛍️ Proyecto: Item Detail Page (Estilo MercadoLibre)

Este proyecto es un prototipo completo que incluye:

✅ **Frontend** en Angular + TailwindCSS  
✅ **Backend** en Python/FastAPI con arquitectura hexagonal  
✅ **Datos locales** en JSON (sin base de datos)  
✅ **Cobertura de tests** del 99%  
✅ **Diseño inspirado** en la página de detalle de producto de MercadoLibre

## � Tabla de Contenidos
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Testing](#testing)
- [Endpoints API](#endpoints-api)
- [Arquitectura](#arquitectura)

## 🗂️ Estructura del Repositorio

```
/
├── 🎯 webapi/          → Backend FastAPI con Arquitectura Hexagonal
│   ├── api/           → Controladores y rutas HTTP
│   ├── application/   → Casos de uso de negocio
│   ├── domain/        → Entidades y puertos
│   ├── infrastructure/→ Repositorios y datos JSON
│   └── tests/         → Suite completa de pruebas (99% cobertura)
└── 🖥️ webapp/          → Frontend Angular + TailwindCSS
    ├── src/app/       → Componentes Angular
    ├── src/domain/    → Modelos TypeScript
    └── src/service/   → Servicios HTTP
```

## ✨ Características

### 🎯 Funcionalidades Principales
- 🔐 **Autenticación JWT** - Sistema de login seguro
- 📦 **Detalle de Productos** - Información completa con imágenes, precios, stock
- 💳 **Métodos de Pago** - Tarjetas de crédito, débito y efectivo
- ⭐ **Productos Recomendados** - Sistema de recomendaciones
- 🔗 **Productos Relacionados** - Sugerencias de productos similares
- 👤 **Información del Vendedor** - Perfil, calificaciones y ventas

### 🏗️ Arquitectura Backend (Hexagonal)
- **Puertos y Adaptadores** - Separación clara de responsabilidades
- **Casos de Uso** - Lógica de negocio encapsulada
- **Repositorios** - Abstracción de persistencia
- **Modelos de Dominio** - Entidades de negocio bien definidas

## 🛠️ Tecnologías

### 🖥️ Frontend (webapp)
- **Angular** 17+ - Framework principal
- **TailwindCSS** - Estilos utilitarios
- **TypeScript** - Tipado estático
- **RxJS** - Programación reactiva

### 🗄️ Backend (webapi)
- **Python** 3.8+ - Lenguaje principal
- **FastAPI** - Framework web moderno
- **Pydantic** v2 - Validación de datos
- **JWT** - Autenticación
- **pytest** - Framework de testing
- **coverage.py** - Medición de cobertura

## 🚀 Instalación

### Prerrequisitos
- Python 3.8+
- Node.js 16+
- pip (Python)
- npm (Node.js)

### Backend Setup
```bash
cd webapi
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd webapp
npm install
```

## ▶️ Ejecución

### 🗄️ Ejecutar Backend
```bash
cd webapi

# Opción 1: Con uvicorn directamente
python -m uvicorn api.app:app --reload --host 127.0.0.1 --port 8000

# Opción 2: Con script personalizado
python start_server.py
```

El backend estará disponible en:
- **API:** http://127.0.0.1:8000
- **Documentación:** http://127.0.0.1:8000/docs

### 🖥️ Ejecutar Frontend
```bash
cd webapp
npm start
```

El frontend estará disponible en: http://localhost:4200

## 🧪 Testing

### 📊 Cobertura Actual: **99%**

El proyecto cuenta con una suite completa de pruebas que garantiza la calidad y funcionamiento del código.

### 🚀 Ejecutar Todos los Tests

```bash
cd webapi

# Ejecutar todos los tests con cobertura
python -m pytest tests/ --cov=. --cov-report=term-missing --cov-report=html

# Ejecutar tests específicos
python -m pytest tests/test_api.py -v
python -m pytest tests/test_models.py -v
python -m pytest tests/test_use_cases.py -v
```

### 📁 Suite de Tests Disponibles

| Test File | Descripción | Cobertura |
|-----------|-------------|-----------|
| `test_api.py` | Tests de integración de endpoints | 100% |
| `test_models.py` | Tests de modelos Pydantic | 100% |
| `test_use_cases.py` | Tests de casos de uso de negocio | 100% |
| `test_repositories.py` | Tests de repositorios JSON | 100% |
| `test_routes.py` | Tests de controladores HTTP | 100% |
| `test_security.py` | Tests de autenticación JWT | 100% |
| `test_controller_integration.py` | Tests de integración de controladores | 100% |
| `test_ports.py` | Tests de interfaces (puertos) | 100% |
| `test_edge_cases.py` | Tests de casos edge | 100% |

### 🎯 Tipos de Pruebas Implementadas

#### 🔍 **Tests Unitarios**
- **Modelos de Dominio** - Validación de entidades Pydantic
- **Casos de Uso** - Lógica de negocio aislada
- **Repositorios** - Operaciones de datos con mocking
- **Utilidades** - Funciones auxiliares

#### 🔗 **Tests de Integración**
- **API Endpoints** - Pruebas end-to-end de la API
- **Controladores** - Integración entre rutas y casos de uso
- **Autenticación** - Flujo completo de JWT
- **Serialización** - Conversión de modelos a JSON

#### ⚡ **Tests de Casos Edge**
- **Manejo de Errores** - Respuestas 404, 401, 500
- **Datos Inválidos** - Validación de entrada
- **Archivos Faltantes** - Manejo de FileNotFoundError
- **Permisos** - Manejo de PermissionError

### 📈 Reporte de Cobertura Detallado

```bash
# Generar reporte HTML detallado
python -m pytest tests/ --cov=. --cov-report=html

# Ver reporte en navegador
# El archivo estará en: htmlcov/index.html
```

### 🔧 **Tests de Funcionalidad Específica**

#### 🔐 Autenticación
```bash
# Tests de JWT y login
python -m pytest tests/test_security.py::TestJWTSecurity -v
python -m pytest tests/test_api.py -k "login" -v
```

#### 📦 Productos
```bash
# Tests de endpoints de productos
python -m pytest tests/test_api.py -k "product" -v
python -m pytest tests/test_repositories.py::TestJSONProductRepository -v
```

#### 💳 Métodos de Pago
```bash
# Tests de payment methods
python -m pytest tests/test_api.py -k "payment" -v
python -m pytest tests/test_use_cases.py::TestGetPaymentMethodsUseCase -v
```

### 🚨 **Ejecutar Tests con Diferentes Niveles de Detalle**

```bash
# Tests básicos (solo resultados)
python -m pytest tests/

# Tests verbosos (con nombres de tests)
python -m pytest tests/ -v

# Tests con output de print statements
python -m pytest tests/ -v -s

# Tests con stack trace corto en fallos
python -m pytest tests/ --tb=short

# Tests de solo un archivo específico
python -m pytest tests/test_api.py --tb=short -v
```

### 📋 **Validaciones Incluidas**

✅ **Funcionalidad Completa**
- Todos los endpoints funcionan correctamente
- Autenticación JWT operativa
- Serialización JSON sin errores
- Manejo de errores HTTP apropiado

✅ **Casos de Error**
- Productos no encontrados (404)
- Credenciales inválidas (401)
- Tokens JWT expirados
- Archivos JSON corruptos

✅ **Integración**
- Conexión entre capas de arquitectura
- Repositorios con casos de uso
- Controladores con autenticación
- Modelos con validación Pydantic

### 🎉 **Resultado Final**
- **90 tests** ejecutados exitosamente
- **99% de cobertura** de código
- **0 fallos** en la suite completa
- **Tiempo de ejecución:** ~2 segundos

## 🌐 Endpoints API

### 🔐 Autenticación
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `POST` | `/login` | Login con credenciales | No |

**Ejemplo de Login:**
```bash
curl -X POST "http://127.0.0.1:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=admin&password=password"
```

### 📦 Productos
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `GET` | `/api/items/{product_id}` | Obtener detalle de producto | No |

**Ejemplo:**
```bash
curl "http://127.0.0.1:8000/api/items/samsung-a55-5g"
```

### 💳 Métodos de Pago
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `GET` | `/api/payment-methods` | Obtener métodos de pago disponibles | No |

### ⭐ Productos Recomendados
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `GET` | `/api/recommended-products` | Obtener productos recomendados | No |

### 🔗 Productos Relacionados
| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| `GET` | `/api/related-products` | Obtener productos relacionados | No |

### 📚 Documentación
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/docs` | Documentación interactiva Swagger UI |
| `GET` | `/redoc` | Documentación alternativa ReDoc |

## 🏛️ Arquitectura

### 🔷 Arquitectura Hexagonal (Puertos y Adaptadores)

```
┌─────────────────────────────────────────────────────────────┐
│                    🎯 API LAYER                            │
├─────────────────────────────────────────────────────────────┤
│  Controllers (FastAPI Routes)                              │
│  • auth_routes.py         • product_routes.py             │
│  • payment_methods_routes.py  • recommended_products.py   │
│  • related_products_routes.py                             │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                 🧠 APPLICATION LAYER                       │
├─────────────────────────────────────────────────────────────┤
│  Use Cases (Business Logic)                               │
│  • GetProductDetailUseCase                                │
│  • GetPaymentMethodsUseCase                               │
│  • GetRecommendedProductsUseCase                          │
│  • GetRelatedProductsUseCase                              │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│                 💎 DOMAIN LAYER                           │
├─────────────────────────────────────────────────────────────┤
│  Entities & Ports                                         │
│  • Product, Seller, Features                             │
│  • PaymentMethods, RecommendedProduct                    │
│  • ProductRepository (Interface)                          │
│  • PaymentMethodsRepository (Interface)                   │
└─────────────────┬───────────────────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────────────────┐
│               🔧 INFRASTRUCTURE LAYER                      │
├─────────────────────────────────────────────────────────────┤
│  Repository Implementations                               │
│  • JSONProductRepository                                  │
│  • JSONPaymentMethodsRepository                          │
│  • JSONRecommendedProductsRepository                     │
│  • JSONRelatedProductsRepository                         │
│                                                           │
│  Data Sources (JSON Files)                               │
│  • products.json                                         │
│  • payment_methods.json                                  │
│  • recommended_products.json                             │
│  • related_products.json                                 │
└─────────────────────────────────────────────────────────────┘
```

### 🔍 Beneficios de esta Arquitectura

✅ **Separación de Responsabilidades** - Cada capa tiene un propósito específico  
✅ **Testabilidad** - Fácil testing con mocking de dependencias  
✅ **Mantenibilidad** - Cambios en una capa no afectan las otras  
✅ **Flexibilidad** - Fácil intercambio de implementaciones  
✅ **Escalabilidad** - Preparada para crecimiento del proyecto  

## 📋 Requisitos Cumplidos

✔️ **API RESTful** sin base de datos real  
✔️ **Datos persistidos** en archivos JSON  
✔️ **Arquitectura hexagonal** bien implementada  
✔️ **Cobertura de código ≥99%** en el backend  
✔️ **Documentación completa** y actualizada  
✔️ **Tests exhaustivos** con casos edge  
✔️ **Autenticación JWT** funcional  
✔️ **Endpoints completamente operativos**  

## 🚀 Estado del Proyecto

- **Backend:** ✅ **COMPLETAMENTE FUNCIONAL**
- **Tests:** ✅ **99% DE COBERTURA**
- **API:** ✅ **TODOS LOS ENDPOINTS OPERATIVOS**
- **Documentación:** ✅ **ACTUALIZADA**
- **Arquitectura:** ✅ **HEXAGONAL IMPLEMENTADA**

## 👥 Equipo

**Desarrolladora Principal:** Lucía Colorado  
**Colaborador en Testing:** GitHub Copilot

---

### 📝 Notas Adicionales

Para más detalles técnicos, consulta:
- `design.md` - Decisiones de diseño y arquitectura
- `run.md` - Instrucciones detalladas de ejecución  
- `/tests/` - Suite completa de pruebas con ejemplos

