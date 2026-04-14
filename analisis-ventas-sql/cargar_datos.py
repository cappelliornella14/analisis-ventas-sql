import pandas as pd
from sqlalchemy import create_engine

# Cargar el CSV
df = pd.read_csv('data/train.csv/train.csv', encoding='latin1')

# Crear base de datos SQLite
engine = create_engine('sqlite:///data/superstore.db')

# Cargar los datos en la base
df.to_sql('ventas', engine, if_exists='replace', index=False)

print("✅ Base de datos creada con éxito")
print(f"Filas cargadas: {len(df)}")
print(df.columns.tolist())