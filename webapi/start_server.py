#!/usr/bin/env python3
"""
Script para ejecutar la aplicación FastAPI
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
