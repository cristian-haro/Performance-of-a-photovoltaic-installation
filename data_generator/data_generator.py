import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parámetros de la instalación y la simulación
capacidad_kw = 2.5  # Capacidad máxima en kW
eficiencia = 0.85  # Eficiencia del sistema
horas_diurnas = range(8, 19)  # Horas de generación solar (8 AM a 6 PM)
dias_simulacion = 30

# Rango de fechas y horas
date_range = pd.date_range(start="2024-01-01", periods=dias_simulacion * 24, freq="H")

# Generación de datos para energía generada por hora
energia_generada = pd.DataFrame({
    "Fecha": date_range.date,
    "Hora": date_range.time,
    # La generación es un valor entre 1.5 y capacidad máxima ajustado por eficiencia, solo durante horas diurnas
    "EnergiaGenerada_kWh": [
        round(np.random.uniform(1.5, capacidad_kw) * eficiencia, 4) if dt.hour in horas_diurnas else 0
        for dt in date_range
    ]
})

# Asegúrate de que los valores son floats y están en el rango correcto
energia_generada["EnergiaGenerada_kWh"] = energia_generada["EnergiaGenerada_kWh"].astype(float)

# Guardar en CSV
energia_generada.to_csv("energia_generada.csv", index=False, sep=';', decimal=',')


# Consumo de cada electrodoméstico por hora
electrodomesticos = {
    "Refrigerador": 0.15,
    "Lavadora": 0.5,
    "AireAcondicionado": 1.2,
    "Television": 0.1,
    "Iluminacion": 0.3,
    "Microondas": 0.8
}

# Creación de la estructura de consumo
consumo = []
for dt in date_range:
    consumo.append([dt.date(), dt.time(), "Refrigerador",electrodomesticos["Refrigerador"]])
    consumo.append([dt.date(), dt.time(), "Lavadora", electrodomesticos["Lavadora"] if np.random.rand() < 0.1 and 14 <= dt.hour < 17 else 0])
    consumo.append([dt.date(), dt.time(), "AireAcondicionado", electrodomesticos["AireAcondicionado"] if 13 <= dt.hour < 18 else 0])
    consumo.append([dt.date(), dt.time(), "Television", electrodomesticos["Television"] if 19 <= dt.hour < 23 else 0])
    consumo.append([dt.date(), dt.time(), "Iluminacion", electrodomesticos["Iluminacion"] if 18 <= dt.hour < 23 else 0])
    consumo.append([dt.date(), dt.time(), "Microondas", np.random.choice([0, electrodomesticos["Microondas"]], p=[0.95, 0.05])])

# Convertir a DataFrame
consumo_df = pd.DataFrame(consumo, columns=["Fecha", "Hora", "Electrodomestico", "Consumo_kWh"])

# Guardar el archivo en CSV
consumo_df.to_csv("consumo_electrodomesticos.csv", index=False, sep=';', decimal=',')

