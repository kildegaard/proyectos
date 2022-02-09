# %%
import pandas as pd

archivo = 'Data/BBVA.csv'

df = pd.read_csv(archivo, delimiter=';')
# %%
df['Monto total'].sum()

# %%
df['Movimiento'].value_counts()

# %%
holi = [df['Importe'] * (df['Cuotas totales'] - df['Cuotas pagas'] + 1)]
sum(*holi)
# %%
