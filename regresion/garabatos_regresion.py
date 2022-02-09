# Probando las dos fórmulas de regresión
def prom(a):
    return sum(a) / len(a)


n = 10
X = [x for x in range(1, n)]
Y = [y for y in range(1, n)]
x_prom = prom(X)
y_prom = prom(Y)

# Devore
a = [(x - x_prom) * (y - y_prom) for x, y in zip(X, Y)]
b = [(x - x_prom)**2 for x in X]
A = sum(a)
B = sum(b)
m_d = A / B

print(f'Resultado Devore: {A} / {B} = {m_d}')

# Manual
c = [x * y for x, y in zip(X, Y)]
c_1 = sum(c)
C = n * c_1 - (sum(X) * sum(Y))

d = [x**2 for x in X]
d_1 = sum(d)
D = n * d_1 - (sum(X))**2

m_M = C / D

print(f'Resultado manual: {C} / {D} = {m_M}')

# AL FIN ME DIO LO MISMO LPM
