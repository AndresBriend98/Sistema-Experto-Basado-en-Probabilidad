from funciones_difusas import *
import numpy as np

class SistemaExpertoDifuso:
    def __init__(self):
        # Definición de variables lingüísticas
        self.variables_entrada = {
            'QC': 'Calidad de Conexión',
            'VR': 'Velocidad de Red',
            'EC': 'Estabilidad de Conexión',
            'SW': 'Señal Wi-Fi',
            'TR': 'Tiempo de Respuesta'
        }
        
        self.variables_salida = {
            'ER': 'Estado del Router',
            'EI': 'Estado del ISP',
            'EC': 'Estado del Cableado',
            'ES': 'Estado del Servidor',
            'EW': 'Estado de la Red Wi-Fi'
        }

        # Base de reglas difusas
        self.reglas = [
            # Reglas para Estado del Router
            {
                'si': [('QC', 'Muy Baja'), ('VR', 'Muy Lenta')],
                'entonces': ('ER', 'Muy Malo')
            },
            {
                'si': [('QC', 'Media'), ('VR', 'Normal')],
                'entonces': ('ER', 'Regular')
            },
            # Reglas para Estado del ISP
            {
                'si': [('EC', 'Muy Inestable'), ('TR', 'Muy Alto')],
                'entonces': ('EI', 'Muy Malo')
            },
            {
                'si': [('EC', 'Moderada'), ('TR', 'Normal')],
                'entonces': ('EI', 'Regular')
            },
            # Reglas para Estado del Cableado
            {
                'si': [('EC', 'Inestable'), ('QC', 'Baja')],
                'entonces': ('EC', 'Malo')
            },
            {
                'si': [('EC', 'Estable'), ('QC', 'Alta')],
                'entonces': ('EC', 'Bueno')
            },
            # Reglas para Estado del Servidor
            {
                'si': [('VR', 'Lenta'), ('TR', 'Alto')],
                'entonces': ('ES', 'Malo')
            },
            {
                'si': [('VR', 'Rápida'), ('TR', 'Bajo')],
                'entonces': ('ES', 'Bueno')
            },
            # Reglas para Estado de la Red Wi-Fi
            {
                'si': [('SW', 'Muy Débil'), ('QC', 'Baja')],
                'entonces': ('EW', 'Muy Malo')
            },
            {
                'si': [('SW', 'Moderada'), ('QC', 'Media')],
                'entonces': ('EW', 'Regular')
            },
            {
                'si': [('SW', 'Fuerte'), ('EC', 'Estable')],
                'entonces': ('EW', 'Bueno')
            },
            {
                'si': [('SW', 'Débil'), ('EC', 'Inestable')],
                'entonces': ('EW', 'Malo')
            }
        ]

        # Acciones sugeridas por estado
        self.acciones = {
            'ER': {
                'Muy Malo': 'Reemplazar router inmediatamente',
                'Malo': 'Reiniciar router y verificar configuración',
                'Regular': 'Monitorear rendimiento del router',
                'Bueno': 'Mantener configuración actual',
                'Muy Bueno': 'Optimizar configuración para mejor rendimiento'
            },
            'EI': {
                'Muy Malo': 'Contactar al ISP para reportar falla crítica',
                'Malo': 'Reportar problemas al ISP',
                'Regular': 'Monitorear calidad del servicio',
                'Bueno': 'Mantener monitoreo regular',
                'Muy Bueno': 'Considerar upgrade de servicio'
            },
            'EC': {
                'Muy Malo': 'Reemplazar cableado completo',
                'Malo': 'Revisar y reemplazar cables dañados',
                'Regular': 'Realizar mantenimiento preventivo',
                'Bueno': 'Verificar puntos de conexión',
                'Muy Bueno': 'Mantener limpieza y orden'
            },
            'ES': {
                'Muy Malo': 'Reiniciar servidor y verificar hardware',
                'Malo': 'Optimizar recursos del servidor',
                'Regular': 'Monitorear carga del servidor',
                'Bueno': 'Realizar mantenimiento programado',
                'Muy Bueno': 'Considerar expansión de recursos'
            },
            'EW': {
                'Muy Malo': 'Instalar repetidores y reubicar router',
                'Malo': 'Ajustar posición del router',
                'Regular': 'Optimizar canales Wi-Fi',
                'Bueno': 'Monitorear cobertura',
                'Muy Bueno': 'Considerar red mesh'
            }
        }

    def fuzzificar_entrada(self, variable, valor):
        """Convierte un valor numérico en grados de membresía"""
        if variable == 'QC':
            return membresia_calidad_conexion(valor)
        elif variable == 'VR':
            return membresia_velocidad_red(valor)
        elif variable == 'EC':
            return membresia_estabilidad_conexion(valor)
        elif variable == 'SW':
            return membresia_senal_wifi(valor)
        elif variable == 'TR':
            return membresia_tiempo_respuesta(valor)
        return {}

    def evaluar_reglas(self, entradas):
        """Evalúa todas las reglas con los valores de entrada"""
        resultados = {}
        for regla in self.reglas:
            # Evaluar antecedentes
            grado_activacion = 1.0
            for var, valor in regla['si']:
                membresia = self.fuzzificar_entrada(var, entradas[var])
                grado_activacion = min(grado_activacion, membresia.get(valor, 0))
            
            # Actualizar resultados
            var_salida, valor_salida = regla['entonces']
            if var_salida not in resultados:
                resultados[var_salida] = {}
            resultados[var_salida][valor_salida] = max(
                resultados[var_salida].get(valor_salida, 0),
                grado_activacion
            )
        return resultados

    def defuzzificar(self, resultados):
        """Convierte resultados difusos en valores precisos"""
        valores_defuzzificados = {}
        for var_salida, grados in resultados.items():
            # Crear puntos para defuzzificación
            x = np.linspace(0, 100, 1000)
            mu = np.zeros_like(x, dtype=float)
            
            # Agregar contribución de cada conjunto difuso
            for valor, grado in grados.items():
                if valor == 'Muy Malo':
                    mu = np.maximum(mu, grado * trapezoide(x, 0, 0, 20, 40))
                elif valor == 'Malo':
                    mu = np.maximum(mu, grado * triangulo(x, 20, 40, 60))
                elif valor == 'Regular':
                    mu = np.maximum(mu, grado * triangulo(x, 40, 60, 80))
                elif valor == 'Bueno':
                    mu = np.maximum(mu, grado * triangulo(x, 60, 80, 100))
                elif valor == 'Muy Bueno':
                    mu = np.maximum(mu, grado * trapezoide(x, 80, 90, 100, 100))
            
            # Calcular centro de gravedad
            if np.sum(mu) > 0:
                valor_defuzzificado = np.sum(x * mu) / np.sum(mu)
                valores_defuzzificados[var_salida] = valor_defuzzificado
            else:
                valores_defuzzificados[var_salida] = 50  # Valor por defecto
        
        return valores_defuzzificados

    def obtener_diagnostico(self, valores_defuzzificados):
        """Convierte valores defuzzificados en diagnóstico y acciones"""
        diagnostico = {}
        for var, valor in valores_defuzzificados.items():
            if valor < 20:
                estado = 'Muy Malo'
            elif valor < 40:
                estado = 'Malo'
            elif valor < 60:
                estado = 'Regular'
            elif valor < 80:
                estado = 'Bueno'
            else:
                estado = 'Muy Bueno'
            
            diagnostico[var] = {
                'estado': estado,
                'valor': valor,
                'accion': self.acciones[var][estado]
            }
        return diagnostico

    def diagnosticar(self, entradas):
        """Realiza el diagnóstico completo"""
        # Evaluar reglas
        resultados = self.evaluar_reglas(entradas)
        
        # Defuzzificar resultados
        valores_defuzzificados = self.defuzzificar(resultados)
        
        # Obtener diagnóstico y acciones
        diagnostico = self.obtener_diagnostico(valores_defuzzificados)
        
        return diagnostico

def ejecutar_caso_prueba(sistema, caso_numero, entradas):
    """Ejecuta un caso de prueba y muestra los resultados"""
    print(f"\nCaso de Prueba {caso_numero}")
    print("Entradas:")
    for var, valor in entradas.items():
        print(f"- {sistema.variables_entrada[var]}: {valor}")
    
    diagnostico = sistema.diagnosticar(entradas)
    
    print("\nDiagnóstico:")
    for var, info in diagnostico.items():
        print(f"\n{sistema.variables_salida[var]}:")
        print(f"- Estado: {info['estado']}")
        print(f"- Valor: {info['valor']:.2f}")
        print(f"- Acción sugerida: {info['accion']}")

def main():
    # Crear instancia del sistema
    sistema = SistemaExpertoDifuso()
    
    # Casos de prueba
    casos = [
        {
            'QC': 10,  # Muy baja calidad
            'VR': 15,  # Muy lenta
            'EC': 85,  # Muy estable
            'SW': -90, # Muy débil
            'TR': 900  # Muy alto
        },
        {
            'QC': 50,  # Media
            'VR': 45,  # Normal
            'EC': 55,  # Moderada
            'SW': -50, # Moderada
            'TR': 500  # Normal
        },
        {
            'QC': 90,  # Muy alta
            'VR': 85,  # Muy rápida
            'EC': 95,  # Muy estable
            'SW': -20, # Fuerte
            'TR': 100  # Muy bajo
        },
        {
            'QC': 30,  # Baja
            'VR': 35,  # Lenta
            'EC': 25,  # Inestable
            'SW': -70, # Débil
            'TR': 700  # Alto
        },
        {
            'QC': 60,  # Alta
            'VR': 65,  # Rápida
            'EC': 75,  # Estable
            'SW': -40, # Moderada
            'TR': 300  # Bajo
        }
    ]
    
    # Ejecutar casos de prueba
    for i, caso in enumerate(casos, 1):
        ejecutar_caso_prueba(sistema, i, caso)
    
    # Modo interactivo
    print("\n\n--- Modo Interactivo ---")
    print("Ingrese los valores para cada variable:")
    entradas = {}
    for var, desc in sistema.variables_entrada.items():
        valor = float(input(f"{desc} (0-100): "))
        entradas[var] = valor
    
    ejecutar_caso_prueba(sistema, "Interactivo", entradas)

if __name__ == "__main__":
    main() 