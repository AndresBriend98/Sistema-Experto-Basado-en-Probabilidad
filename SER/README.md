# Sistema Experto Basado en Reglas (SER)

Este sistema experto utiliza un enfoque basado en reglas lógicas para diagnosticar problemas en una red informática. A diferencia de los sistemas basados en probabilidad o lógica difusa, este sistema utiliza reglas booleanas simples para tomar decisiones.

## Características

- **Variables de Entrada**:
  - Calidad de Conexión (QC)
  - Velocidad de Red (VR)
  - Estabilidad de Conexión (EC)
  - Señal Wi-Fi (SW)
  - Tiempo de Respuesta (TR)

- **Variables de Salida**:
  - Estado del Router (ER)
  - Estado del ISP (EI)
  - Estado del Cableado (EC)
  - Estado del Servidor (ES)
  - Estado de la Red Wi-Fi (EW)

## Funcionamiento

1. **Clasificación de Valores**:
   - Cada variable de entrada tiene rangos predefinidos
   - Los valores numéricos se clasifican en categorías (Muy Bajo, Bajo, Normal, Alto, Muy Alto)

2. **Evaluación de Reglas**:
   - Las reglas se evalúan de forma booleana (verdadero/falso)
   - Una regla se activa solo si TODAS sus condiciones se cumplen exactamente

3. **Diagnóstico**:
   - Si múltiples reglas se activan, se elige el peor estado
   - Se sugiere una acción específica para cada diagnóstico

## Diferencias con otros Sistemas

- **vs Sistema Probabilístico**:
  - No usa probabilidades
  - Decisiones más "definitivas"
  - No maneja incertidumbre

- **vs Sistema Difuso**:
  - No usa grados de membresía
  - No usa defuzzificación
  - Reglas más estrictas

## Uso

1. Ejecutar el programa:
   ```bash
   python sistema_experto_reglas.py
   ```

2. El programa ejecutará casos de prueba predefinidos

3. Luego entrará en modo interactivo donde podrás ingresar tus propios valores

## Ejemplo de Regla

```python
{
    'si': [
        ('QC', 'Muy Baja'),
        ('VR', 'Muy Lenta')
    ],
    'entonces': ('ER', 'Muy Malo')
}
```

Esta regla indica que si la calidad de conexión es muy baja Y la velocidad de red es muy lenta, entonces el estado del router es muy malo. 