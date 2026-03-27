# Data Analyst - Manipulación de Datos con Pandas

Proyecto de ejercicios para aprender manipulación de datos con Pandas.

## Requisitos

- Python 3.12 o superior
- pip

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd data-analyst-data-manipulation-with-panda
```

2. Crear y activar el entorno virtual:
```bash
python -m venv venv
source venv/Scripts/activate  # En Windows
# source venv/bin/activate    # En Linux/Mac
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
.
├── transformacion-dataframes/
│   ├── 1.dataframes.py        # Ejercicios de DataFrames
│   ├── homelessness.csv       # Dataset de personas sin hogar
│   ├── avoplotto.pkl          # Dataset de aguacates
│   ├── sales_subset.csv       # Dataset de ventas
│   └── temperatures.csv       # Dataset de temperaturas
├── requirements.txt           # Dependencias del proyecto
└── .gitignore                # Archivos ignorados por Git
```

## Uso

Para ejecutar los ejercicios:

```bash
cd transformacion-dataframes
python 1.dataframes.py
```

## Contenido

### 1. DataFrames
- Inspección de DataFrames (head, info, shape, describe)
- Más secciones por agregar...
