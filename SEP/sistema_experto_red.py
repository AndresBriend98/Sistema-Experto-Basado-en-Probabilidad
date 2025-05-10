# sistema_experto_red.py

# Definición de síntomas y causas
sintomas = {
    "S1": "No hay conexión a Internet",
    "S2": "Conexión intermitente",
    "S3": "Lentitud al acceder a recursos internos",
    "S4": "Errores de DNS",
    "S5": "Señal Wi-Fi débil",
    "S6": "Pérdida de paquetes en ping"
}

causas = {
    "C1": "Falla en el router",
    "C2": "Problemas con el ISP",
    "C3": "Cable de red dañado",
    "C4": "Problemas en el servidor interno",
    "C5": "Señal Wi-Fi insuficiente"
}

# Probabilidades a priori
prob_priori = {
    "C1": 0.20,
    "C2": 0.25,
    "C3": 0.15,
    "C4": 0.20,
    "C5": 0.20
}

# Probabilidades condicionales P(Síntoma|Causa)
prob_condicional = {
    "C1": {"S1": 0.80, "S2": 0.60, "S3": 0.40, "S4": 0.60, "S5": 0.30, "S6": 0.50},
    "C2": {"S1": 0.70, "S2": 0.70, "S3": 0.20, "S4": 0.50, "S5": 0.10, "S6": 0.60},
    "C3": {"S1": 0.10, "S2": 0.20, "S3": 0.30, "S4": 0.10, "S5": 0.05, "S6": 0.80},
    "C4": {"S1": 0.05, "S2": 0.10, "S3": 0.85, "S4": 0.20, "S5": 0.05, "S6": 0.10},
    "C5": {"S1": 0.10, "S2": 0.30, "S3": 0.10, "S4": 0.05, "S5": 0.90, "S6": 0.10}
}

# Reglas condicionales (simplificadas para el ejemplo)
reglas = [
    (["S1", "S6"], "C1", 0.80),
    (["S2", "S4"], "C2", 0.75),
    (["S3", "S6"], "C3", 0.85),
    (["S3", "S1"], "C4", 0.70),
    (["S5", "S2"], "C5", 0.80),
    (["S4", "S1"], "C1", 0.70),
    (["S6", "S2"], "C2", 0.65),
    (["S5", "S1"], "C5", 0.60),
    (["S3", "S4"], "C4", 0.75),
    (["S2", "S1"], "C2", 0.80),
    (["S6", "S5"], "C3", 0.70),
    (["S1", "S4"], "C2", 0.60)
]

# Acciones sugeridas por causa
acciones = {
    "C1": "Reiniciar o reemplazar el router, revisar configuración.",
    "C2": "Contactar al ISP, verificar estado del servicio.",
    "C3": "Cambiar cable, revisar conectores.",
    "C4": "Revisar servidor, recursos y servicios internos.",
    "C5": "Reubicar router, instalar repetidor Wi-Fi."
}

# Tablas PAMA y PyA
def mostrar_tablas():
    print("\nTabla PAMA:")
    print("Percepción\t\t\tAcción\t\t\t\tMedios-Fines\t\t\tAmbiente")
    print("No hay Internet\t\t\tRevisar router, ISP\t\tRestablecer conectividad\tRed local, acceso externo")
    print("Intermitencia\t\t\tVerificar router, ISP\t\tEstabilidad de red\t\tRed local, ISP")
    print("Lentitud interna\t\tRevisar servidor, cableado\tMejorar acceso interno\t\tRed local")
    print("Errores DNS\t\t\tRevisar router, DNS\t\tAcceso a servicios\t\tRed local, Internet")
    print("Wi-Fi débil\t\t\tReubicar router, repetidor\tMejorar señal\t\t\tOficina, Wi-Fi")
    print("Pérdida de paquetes\t\tRevisar cableado, router, ISP\tMejorar estabilidad\t\tRed local, ISP")
    print("\nTabla PyA:")
    print("Percepción\t\t\tAcción")
    print("No hay Internet\t\t\tRevisar router, ISP")
    print("Intermitencia\t\t\tVerificar router, ISP")
    print("Lentitud interna\t\tRevisar servidor, cableado")
    print("Errores DNS\t\t\tRevisar router, DNS")
    print("Wi-Fi débil\t\t\tReubicar router, repetidor")
    print("Pérdida de paquetes\t\tRevisar cableado, router, ISP")

# Inferencia bayesiana
def inferir_causas(sintomas_entrada):
    # Aplicar reglas condicionales primero (si alguna coincide exactamente)
    for sintomas_regla, causa_regla, prob_regla in reglas:
        if all(s in sintomas_entrada for s in sintomas_regla):
            print(f"\nRegla aplicada: Si {', '.join([sintomas[s] for s in sintomas_regla])} => {causas[causa_regla]} ({prob_regla*100:.0f}%)")
            return {causa_regla: prob_regla}

    # Si no hay regla exacta, aplicar inferencia bayesiana
    probabilidades = {}
    for c in causas:
        p_c = prob_priori[c]
        p_s_dado_c = 1.0
        for s in sintomas_entrada:
            p_s_dado_c *= prob_condicional[c].get(s, 0.01)  # Si no está, probabilidad baja
        probabilidades[c] = p_s_dado_c * p_c

    # Normalizar
    total = sum(probabilidades.values())
    if total > 0:
        for c in probabilidades:
            probabilidades[c] /= total
    return probabilidades

def mostrar_diagnostico(probabilidades):
    print("\nDiagnóstico probabilístico:")
    causas_ordenadas = sorted(probabilidades.items(), key=lambda x: x[1], reverse=True)
    for c, p in causas_ordenadas:
        print(f"- {causas[c]}: {p*100:.1f}%")
    causa_mas_probable = causas_ordenadas[0][0]
    print(f"\nAcción sugerida: {acciones[causa_mas_probable]}")

def ejecutar_caso(sintomas_entrada):
    print("\n--- Diagnóstico de red ---")
    print("Síntomas ingresados:")
    for s in sintomas_entrada:
        print(f"- {sintomas[s]}")
    probabilidades = inferir_causas(sintomas_entrada)
    mostrar_diagnostico(probabilidades)

# Casos de prueba
def casos_prueba():
    print("\n\n--- CASOS DE PRUEBA ---")
    casos = [
        (["S1", "S6"], "Caso 1"),
        (["S2", "S4"], "Caso 2"),
        (["S3", "S6"], "Caso 3"),
        (["S5", "S2"], "Caso 4"),
        (["S3", "S4"], "Caso 5")
    ]
    for sintomas_entrada, nombre in casos:
        print(f"\n{nombre}:")
        ejecutar_caso(sintomas_entrada)

if __name__ == "__main__":
    mostrar_tablas()
    casos_prueba()
    # Diagnóstico interactivo
    print("\n\n--- Diagnóstico interactivo ---")
    print("Síntomas disponibles:")
    for k, v in sintomas.items():
        print(f"{k}: {v}")
    entrada = input("Ingrese los códigos de los síntomas separados por coma (ej: S1,S4): ")
    sintomas_usuario = [s.strip().upper() for s in entrada.split(",") if s.strip().upper() in sintomas]
    if sintomas_usuario:
        ejecutar_caso(sintomas_usuario)
    else:
        print("No se ingresaron síntomas válidos.")
