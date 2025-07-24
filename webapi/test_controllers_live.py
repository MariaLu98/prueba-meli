#!/usr/bin/env python3
"""
Script para probar todos los controladores de la WebAPI en vivo
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

def test_controller(name, url, method="GET", data=None, headers=None):
    """Función auxiliar para probar un controlador"""
    try:
        print(f"\n🔄 Probando {name}...")
        print(f"   URL: {method} {url}")
        
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers)
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code < 400:
            print(f"   ✅ {name} - FUNCIONANDO")
            if response.content:
                try:
                    response_data = response.json()
                    if isinstance(response_data, list):
                        print(f"   Respuesta: Lista con {len(response_data)} elementos")
                    elif isinstance(response_data, dict):
                        print(f"   Respuesta: Objeto con claves: {list(response_data.keys())}")
                except:
                    print(f"   Respuesta: {response.text[:100]}...")
        else:
            print(f"   ❌ {name} - ERROR: {response.text}")
            
        return response.status_code < 400
        
    except requests.exceptions.ConnectionError:
        print(f"   ❌ {name} - ERROR: No se puede conectar al servidor")
        return False
    except Exception as e:
        print(f"   ❌ {name} - ERROR: {str(e)}")
        return False

def main():
    print("🚀 PROBANDO CONTROLADORES DE LA WEBAPI")
    print("=" * 50)
    print(f"Servidor: {BASE_URL}")
    print(f"Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = {}
    
    # 1. Probar endpoint raíz / documentación
    results["docs"] = test_controller(
        "Documentación API",
        f"{BASE_URL}/docs"
    )
    
    # 2. Probar controlador de autenticación
    results["auth_success"] = test_controller(
        "Auth Controller - Login Exitoso",
        f"{BASE_URL}/login",
        method="POST",
        data={"username": "admin", "password": "password"}
    )
    
    results["auth_fail"] = test_controller(
        "Auth Controller - Login Fallido",
        f"{BASE_URL}/login",
        method="POST",
        data={"username": "wrong", "password": "wrong"}
    )
    
    # 3. Probar controlador de productos
    results["product_existing"] = test_controller(
        "Product Controller - Producto Existente",
        f"{BASE_URL}/api/items/samsung-a55-5g"
    )
    
    results["product_not_found"] = test_controller(
        "Product Controller - Producto No Encontrado",
        f"{BASE_URL}/api/items/producto-inexistente"
    )
    
    # 4. Probar controlador de métodos de pago
    results["payment_methods"] = test_controller(
        "Payment Methods Controller",
        f"{BASE_URL}/api/payment-methods"
    )
    
    # 5. Probar controlador de productos recomendados
    results["recommended_products"] = test_controller(
        "Recommended Products Controller",
        f"{BASE_URL}/api/recommended-products"
    )
    
    # 6. Probar controlador de productos relacionados
    results["related_products"] = test_controller(
        "Related Products Controller",
        f"{BASE_URL}/api/related-products"
    )
    
    # Resumen final
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE RESULTADOS")
    print("=" * 50)
    
    successful = sum(1 for success in results.values() if success)
    total = len(results)
    
    for test_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {test_name:.<30} {status}")
    
    print("-" * 50)
    print(f"Exitosos: {successful}/{total}")
    print(f"Porcentaje: {(successful/total)*100:.1f}%")
    
    if successful == total:
        print("\n🎉 ¡TODOS LOS CONTROLADORES ESTÁN FUNCIONANDO CORRECTAMENTE!")
    else:
        print(f"\n⚠️  Hay {total - successful} controladores con problemas")
    
    return successful == total

if __name__ == "__main__":
    main()
