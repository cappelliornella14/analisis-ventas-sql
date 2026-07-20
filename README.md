# 📊 Análisis de Ventas con SQL y Python

Proyecto de análisis de datos de ventas utilizando **SQL**, **Python** y **Jupyter Notebooks**. Incluye consultas SQL optimizadas, visualizaciones con matplotlib y análisis de negocio.

---

## 🎯 Objetivo

Analizar un dataset de ventas de una tienda (Superstore) para obtener insights de negocio sobre:
- Categorías de productos más vendidas
- Top productos por facturación
- Rendimiento por región geográfica
- Ciudades con mayor volumen de ventas
- Clientes con mayor gasto promedio

---

## 🛠️ Stack Tecnológico

| Tecnología | Uso |
|------------|-----|
| **Python 3.10+** | Lenguaje principal |
| **pandas** | Manipulación y análisis de datos |
| **SQLAlchemy** | Conexión con bases de datos |
| **matplotlib** | Generación de gráficos |
| **SQLite** | Base de datos local |
| **Jupyter Notebook** | Análisis interactivo |

---

## 📁 Estructura del Proyecto

```
analisis-ventas-sql/
├── README.md              # Este archivo
├── requirements.txt       # Dependencias de Python
├── cargar_datos.py        # Script para cargar CSV → SQLite
├── data/
│   ├── train.csv/         # Dataset original
│   │   └── train.csv
│   └── superstore.db      # Base de datos SQLite
├── imagenes/              # Gráficos generados
│   ├── ventas_por_categoria.png
│   ├── top_productos.png
│   ├── ventas_region.png
│   └── top_ciudades.png
├── notebooks/
│   └── analisis.ipynb     # Notebook principal
└── sql/
    └── consultas.sql      # Consultas SQL puras
```

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/cappelliornella14/analisis-ventas-sql.git
cd analisis-ventas-sql
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Cargar los datos en SQLite
```bash
python cargar_datos.py
```

### 4. Ejecutar el notebook
```bash
jupyter notebook notebooks/analisis.ipynb
```

---

## 📈 Consultas SQL

El archivo `sql/consultas.sql` contiene 5 consultas principales:

| # | Consulta | Descripción |
|---|----------|-------------|
| 1 | Ventas por categoría | Total de ventas agrupadas por categoría de producto |
| 2 | Top 5 productos | Los 5 productos con mayor facturación |
| 3 | Ventas por región | Análisis de ventas por región geográfica |
| 4 | Clientes top | Top 10 clientes con mayor gasto promedio |
| 5 | Top 10 ciudades | Ciudades con más ventas |

---

## 📊 Resultados Principales

### Ventas por Categoría
| Categoría | Total Ventas |
|-----------|--------------|
| Technology | $827,455.87 |
| Furniture | $728,658.58 |
| Office Supplies | $705,422.33 |

### Top 5 Productos
1. Canon imageCLASS 2200 Advanced Copier - $61,599.82
2. Fellowes PB500 Electric Punch - $27,453.38
3. Cisco TelePresence System EX90 - $22,638.48
4. HON 5400 Series Task Chairs - $21,870.58
5. GBC DocuBind TL300 - $19,823.48

### Ventas por Región
| Región | Total Ventas | Órdenes |
|--------|--------------|---------|
| West | $710,219.68 | 3,140 |
| East | $669,518.73 | 2,785 |
| Central | $492,646.91 | 2,277 |
| South | $389,151.46 | 1,598 |

---

## 👩‍💻 Autora

**Ornella Cappelli**
- GitHub: [@cappelliornella14](https://github.com/cappelliornella14)
- LinkedIn: [Ornella Cappelli](https://www.linkedin.com/in/ornella-cappelli-051207327/)
