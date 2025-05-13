class SistemaExpertoReglas:
    def __init__(self):
        # Definición de variables de entrada
        self.variables_entrada = {
            'QC': 'Calidad de Conexión',
            'VR': 'Velocidad de Red',
            'EC': 'Estabilidad de Conexión',
            'SW': 'Señal Wi-Fi',
            'TR': 'Tiempo de Respuesta'
        }
        
        # Definición de variables de salida
        self.variables_salida = {
            'ER': 'Estado del Router',
            'EI': 'Estado del ISP',
            'EC': 'Estado del Cableado',
            'ES': 'Estado del Servidor',
            'EW': 'Estado de la Red Wi-Fi'
        }

        # Definición de rangos para cada variable
        self.rangos = {
            'QC': {'Muy Baja': (0, 20), 'Baja': (20, 40), 'Media': (40, 60), 'Alta': (60, 80), 'Muy Alta': (80, 100)},
            'VR': {'Muy Lenta': (0, 20), 'Lenta': (20, 40), 'Normal': (40, 60), 'Rápida': (60, 80), 'Muy Rápida': (80, 100)},
            'EC': {'Muy Inestable': (0, 20), 'Inestable': (20, 40), 'Moderada': (40, 60), 'Estable': (60, 80), 'Muy Estable': (80, 100)},
            'SW': {'Muy Débil': (-100, -80), 'Débil': (-80, -60), 'Moderada': (-60, -40), 'Fuerte': (-40, -20), 'Muy Fuerte': (-20, 0)},
            'TR': {'Muy Alto': (800, 1000), 'Alto': (600, 800), 'Normal': (400, 600), 'Bajo': (200, 400), 'Muy Bajo': (0, 200)}
        }

        # Base de reglas
        self.reglas = [
            # Reglas para Estado del Router
            {
                'si': [
                    ('QC', 'Muy Baja'),
                    ('VR', 'Muy Lenta')
                ],
                'entonces': ('ER', 'Muy Malo')
            },
            {
                'si': [
                    ('QC', 'Media'),
                    ('VR', 'Normal')
                ],
                'entonces': ('ER', 'Regular')
            },
            {
                'si': [
                    ('QC', 'Baja'),
                    ('VR', 'Lenta')
                ],
                'entonces': ('ER', 'Malo')
            },
            {
                'si': [
                    ('QC', 'Alta'),
                    ('VR', 'Rápida')
                ],
                'entonces': ('ER', 'Bueno')
            },
            {
                'si': [
                    ('QC', 'Muy Alta'),
                    ('VR', 'Muy Rápida')
                ],
                'entonces': ('ER', 'Muy Bueno')
            },
            # Reglas para Estado del ISP
            {
                'si': [
                    ('EC', 'Muy Inestable'),
                    ('TR', 'Muy Alto')
                ],
                'entonces': ('EI', 'Muy Malo')
            },
            {
                'si': [
                    ('EC', 'Moderada'),
                    ('TR', 'Normal')
                ],
                'entonces': ('EI', 'Regular')
            },
            {
                'si': [
                    ('EC', 'Inestable'),
                    ('TR', 'Alto')
                ],
                'entonces': ('EI', 'Malo')
            },
            {
                'si': [
                    ('EC', 'Estable'),
                    ('TR', 'Bajo')
                ],
                'entonces': ('EI', 'Bueno')
            },
            {
                'si': [
                    ('EC', 'Muy Estable'),
                    ('TR', 'Muy Bajo')
                ],
                'entonces': ('EI', 'Muy Bueno')
            },
            # Reglas para Estado del Cableado
            {
                'si': [
                    ('EC', 'Inestable'),
                    ('QC', 'Baja')
                ],
                'entonces': ('EC', 'Malo')
            },
            {
                'si': [
                    ('EC', 'Estable'),
                    ('QC', 'Alta')
                ],
                'entonces': ('EC', 'Bueno')
            },
            {
                'si': [
                    ('EC', 'Muy Inestable'),
                    ('QC', 'Muy Baja')
                ],
                'entonces': ('EC', 'Muy Malo')
            },
            {
                'si': [
                    ('EC', 'Moderada'),
                    ('QC', 'Media')
                ],
                'entonces': ('EC', 'Regular')
            },
            {
                'si': [
                    ('EC', 'Muy Estable'),
                    ('QC', 'Muy Alta')
                ],
                'entonces': ('EC', 'Muy Bueno')
            },
            # Reglas para Estado del Servidor
            {
                'si': [
                    ('VR', 'Lenta'),
                    ('TR', 'Alto')
                ],
                'entonces': ('ES', 'Malo')
            },
            {
                'si': [
                    ('VR', 'Rápida'),
                    ('TR', 'Bajo')
                ],
                'entonces': ('ES', 'Bueno')
            },
            {
                'si': [
                    ('VR', 'Muy Lenta'),
                    ('TR', 'Muy Alto')
                ],
                'entonces': ('ES', 'Muy Malo')
            },
            {
                'si': [
                    ('VR', 'Normal'),
                    ('TR', 'Normal')
                ],
                'entonces': ('ES', 'Regular')
            },
            {
                'si': [
                    ('VR', 'Muy Rápida'),
                    ('TR', 'Muy Bajo')
                ],
                'entonces': ('ES', 'Muy Bueno')
            },
            # Reglas para Estado de la Red Wi-Fi
            {
                'si': [
                    ('SW', 'Muy Débil'),
                    ('QC', 'Baja')
                ],
                'entonces': ('EW', 'Muy Malo')
            },
            {
                'si': [
                    ('SW', 'Moderada'),
                    ('QC', 'Media')
                ],
                'entonces': ('EW', 'Regular')
            },
            {
                'si': [
                    ('SW', 'Débil'),
                    ('QC', 'Baja')
                ],
                'entonces': ('EW', 'Malo')
            },
            {
                'si': [
                    ('SW', 'Fuerte'),
                    ('QC', 'Alta')
                ],
                'entonces': ('EW', 'Bueno')
            },
            {
                'si': [
                    ('SW', 'Muy Fuerte'),
                    ('QC', 'Muy Alta')
                ],
                'entonces': ('EW', 'Muy Bueno')
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

    def clasificar_valor(self, variable, valor):
        """Clasifica un valor numérico en su categoría correspondiente"""
        rangos = self.rangos[variable]
        for categoria, (min_val, max_val) in rangos.items():
            if min_val <= valor <= max_val:
                return categoria
        return None

    def evaluar_reglas(self, entradas):
        """Evalúa todas las reglas con los valores de entrada"""
        resultados = {}
        for regla in self.reglas:
            # Evaluar antecedentes
            regla_cumple = True
            for var, valor_esperado in regla['si']:
                valor_actual = entradas[var]
                categoria = self.clasificar_valor(var, valor_actual)
                if categoria != valor_esperado:
                    regla_cumple = False
                    break
            
            # Si la regla se cumple, actualizar resultados
            if regla_cumple:
                var_salida, valor_salida = regla['entonces']
                if var_salida not in resultados:
                    resultados[var_salida] = {}
                resultados[var_salida][valor_salida] = True
        
        return resultados

    def obtener_diagnostico(self, resultados):
        """Convierte resultados de reglas en diagnóstico y acciones"""
        diagnostico = {}
        
        # Si no hay resultados, asignar estado por defecto
        if not resultados:
            for var_salida in self.variables_salida.keys():
                diagnostico[var_salida] = {
                    'estado': 'Regular',
                    'accion': self.acciones[var_salida]['Regular']
                }
            return diagnostico
            
        # Procesar resultados existentes
        for var_salida, estados in resultados.items():
            # Si hay múltiples estados, elegir el peor
            if 'Muy Malo' in estados:
                estado = 'Muy Malo'
            elif 'Malo' in estados:
                estado = 'Malo'
            elif 'Regular' in estados:
                estado = 'Regular'
            elif 'Bueno' in estados:
                estado = 'Bueno'
            else:
                estado = 'Muy Bueno'
            
            diagnostico[var_salida] = {
                'estado': estado,
                'accion': self.acciones[var_salida][estado]
            }
            
        # Completar diagnóstico para variables sin reglas activadas
        for var_salida in self.variables_salida.keys():
            if var_salida not in diagnostico:
                diagnostico[var_salida] = {
                    'estado': 'Regular',
                    'accion': self.acciones[var_salida]['Regular']
                }
                
        return diagnostico

    def diagnosticar(self, entradas):
        """Realiza el diagnóstico completo"""
        # Evaluar reglas
        resultados = self.evaluar_reglas(entradas)
        
        # Obtener diagnóstico y acciones
        diagnostico = self.obtener_diagnostico(resultados)
        
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
        print(f"- Acción sugerida: {info['accion']}")

def main():
    # Crear instancia del sistema
    sistema = SistemaExpertoReglas()
    
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