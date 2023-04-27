import pandas as  pd

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel('TestGrowPro.xlsx')

# Reemplazar los valores de texto por formato fecha en la columna 'fecha'
df['Date Of Birth'] = pd.to_datetime(df['Date Of Birth'], format='%d/%m/%Y')

# Reemplazar los valores de texto por formato número en la columna 'numero'
df['Test Result'] = df['Test Result'].astype(float)

# Guardar el DataFrame modificado en un nuevo archivo de Excel
df.to_excel('TestGrowPro_modificado.xlsx', index=False)