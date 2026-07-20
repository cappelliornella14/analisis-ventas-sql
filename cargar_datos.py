"""
Script para cargar datos de ventas desde CSV a SQLite.

Uso:
    python cargar_datos.py

Este script lee el archivo train.csv, lo carga en una base de datos
SQLite y muestra un resumen de los datos cargados.
"""

import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


def cargar_datos(csv_path: str = "data/train.csv/train.csv", 
                 db_path: str = "data/superstore.db") -> None:
    """
    Carga datos desde un archivo CSV a una base de datos SQLite.
    
    Args:
        csv_path: Ruta al archivo CSV con los datos
        db_path: Ruta donde se guardará la base de datos SQLite
    """
    # Verificar que el archivo CSV existe
    csv_file = Path(csv_path)
    if not csv_file.exists():
        print(f"❌ Error: No se encontró el archivo {csv_path}")
        print("   Asegurate de que el dataset esté en la ruta correcta.")
        sys.exit(1)
    
    try:
        print(f"📂 Cargando datos desde: {csv_path}")
        df = pd.read_csv(csv_path, encoding='latin1')
        
        print(f"📊 Filas encontradas: {len(df)}")
        print(f"📋 Columnas: {len(df.columns)}")
        
        # Crear directorio si no existe
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Crear base de datos SQLite
        engine = create_engine(f"sqlite:///{db_path}")
        
        # Cargar los datos en la base
        df.to_sql('ventas', engine, if_exists='replace', index=False)
        
        print(f"\n✅ Base de datos creada con éxito en: {db_path}")
        print(f"✅ Tabla 'ventas' creada con {len(df)} registros")
        
        # Mostrar primeras filas
        print("\n📊 Primeras 5 filas:")
        print(df.head().to_string())
        
        # Mostrar estadísticas básicas
        print("\n📈 Resumen estadístico:")
        print(df.describe().to_string())
        
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        sys.exit(1)


if __name__ == "__main__":
    cargar_datos()
