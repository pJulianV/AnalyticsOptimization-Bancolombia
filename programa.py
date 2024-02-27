def calcular_promedio_ventas(ventas_diarias):
    suma_ventas = sum(ventas_diarias)
    promedio = suma_ventas / len(ventas_diarias)
    return promedio

# Ejemplo de uso
ventas_ultimos_15_dias = [1000, 1500, 1200, 800, 2000, 1300, 1100, 1600, 900, 1200, 1800, 1000, 1400, 1700, 1500]
promedio_ventas = calcular_promedio_ventas(ventas_ultimos_15_dias)
print("El promedio de ventas diarias es:", promedio_ventas)