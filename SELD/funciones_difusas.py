import numpy as np

def triangulo(x, a, b, c):
    """Función de membresía triangular"""
    if isinstance(x, np.ndarray):
        y = np.zeros_like(x, dtype=float)
        mask1 = (x >= a) & (x <= b)
        mask2 = (x > b) & (x <= c)
        y[mask1] = (x[mask1] - a) / (b - a)
        y[mask2] = (c - x[mask2]) / (c - b)
        return y
    else:
        if x <= a or x >= c:
            return 0
        elif a <= x <= b:
            return (x - a) / (b - a)
        else:
            return (c - x) / (c - b)

def trapezoide(x, a, b, c, d):
    """Función de membresía trapezoidal"""
    if isinstance(x, np.ndarray):
        y = np.zeros_like(x, dtype=float)
        mask1 = (x >= a) & (x < b)
        mask2 = (x >= b) & (x <= c)
        mask3 = (x > c) & (x <= d)
        y[mask1] = (x[mask1] - a) / (b - a)
        y[mask2] = 1
        y[mask3] = (d - x[mask3]) / (d - c)
        return y
    else:
        if x <= a or x >= d:
            return 0
        elif b <= x <= c:
            return 1
        elif a <= x <= b:
            return (x - a) / (b - a)
        else:
            return (d - x) / (d - c)

def membresia_calidad_conexion(x):
    """Función de membresía para Calidad de Conexión"""
    muy_baja = trapezoide(x, 0, 0, 20, 40)
    baja = triangulo(x, 20, 40, 60)
    media = triangulo(x, 40, 60, 80)
    alta = triangulo(x, 60, 80, 100)
    muy_alta = trapezoide(x, 80, 90, 100, 100)
    return {
        'Muy Baja': muy_baja,
        'Baja': baja,
        'Media': media,
        'Alta': alta,
        'Muy Alta': muy_alta
    }

def membresia_velocidad_red(x):
    """Función de membresía para Velocidad de Red"""
    muy_lenta = trapezoide(x, 0, 0, 20, 40)
    lenta = triangulo(x, 20, 40, 60)
    normal = triangulo(x, 40, 60, 80)
    rapida = triangulo(x, 60, 80, 100)
    muy_rapida = trapezoide(x, 80, 90, 100, 100)
    return {
        'Muy Lenta': muy_lenta,
        'Lenta': lenta,
        'Normal': normal,
        'Rápida': rapida,
        'Muy Rápida': muy_rapida
    }

def membresia_estabilidad_conexion(x):
    """Función de membresía para Estabilidad de Conexión"""
    muy_inestable = trapezoide(x, 0, 0, 20, 40)
    inestable = triangulo(x, 20, 40, 60)
    moderada = triangulo(x, 40, 60, 80)
    estable = triangulo(x, 60, 80, 100)
    muy_estable = trapezoide(x, 80, 90, 100, 100)
    return {
        'Muy Inestable': muy_inestable,
        'Inestable': inestable,
        'Moderada': moderada,
        'Estable': estable,
        'Muy Estable': muy_estable
    }

def membresia_senal_wifi(x):
    """Función de membresía para Intensidad de Señal Wi-Fi"""
    muy_debil = trapezoide(x, -100, -100, -80, -60)
    debil = triangulo(x, -80, -60, -40)
    moderada = triangulo(x, -60, -40, -20)
    fuerte = triangulo(x, -40, -20, 0)
    muy_fuerte = trapezoide(x, -20, -10, 0, 0)
    return {
        'Muy Débil': muy_debil,
        'Débil': debil,
        'Moderada': moderada,
        'Fuerte': fuerte,
        'Muy Fuerte': muy_fuerte
    }

def membresia_tiempo_respuesta(x):
    """Función de membresía para Tiempo de Respuesta"""
    muy_alto = trapezoide(x, 800, 800, 900, 1000)
    alto = triangulo(x, 600, 800, 1000)
    normal = triangulo(x, 400, 600, 800)
    bajo = triangulo(x, 200, 400, 600)
    muy_bajo = trapezoide(x, 0, 100, 200, 200)
    return {
        'Muy Alto': muy_alto,
        'Alto': alto,
        'Normal': normal,
        'Bajo': bajo,
        'Muy Bajo': muy_bajo
    }

def centro_gravedad(x, mu):
    """Calcula el centro de gravedad para defuzzificación"""
    return np.sum(x * mu) / np.sum(mu)

def evaluar_regla(antecedentes, consecuente, valores_entrada):
    """Evalúa una regla difusa y retorna el grado de activación"""
    grado_activacion = 1.0
    for ant, val in zip(antecedentes, valores_entrada):
        grado_activacion = min(grado_activacion, ant[val])
    return grado_activacion 