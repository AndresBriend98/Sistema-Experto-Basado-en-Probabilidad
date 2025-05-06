from pgmpy.models import DiscreteBayesianNetwork
import networkx as nx
import matplotlib.pyplot as plt

# Definir la estructura del modelo bayesiano (solo relaciones relevantes)
modelo = DiscreteBayesianNetwork([
    ('C1', 'S1'), ('C2', 'S1'), ('C3', 'S1'),
    ('C1', 'S2'), ('C2', 'S2'), ('C5', 'S2'),
    ('C1', 'S3'), ('C4', 'S3'), ('C3', 'S3'),
    ('C1', 'S4'), ('C2', 'S4'),
    ('C5', 'S5'),
    ('C1', 'S6'), ('C2', 'S6'), ('C3', 'S6')
])

# Crear el grafo de networkx
grafo_nx = nx.DiGraph()

# Agregar nodos y aristas
for edge in modelo.edges():
    grafo_nx.add_edge(edge[0], edge[1])

# Definir posiciones manuales para mayor claridad
causas = ['C1', 'C2', 'C3', 'C4', 'C5']
sintomas = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6']

# Posiciones: causas arriba, síntomas abajo
pos = {}
for i, c in enumerate(causas):
    pos[c] = (i, 1)
for i, s in enumerate(sintomas):
    pos[s] = (i, 0)

# Visualizar la red bayesiana
plt.figure(figsize=(12, 6))

# Dibujar nodos de causas
nx.draw_networkx_nodes(grafo_nx, pos, 
                      nodelist=causas,
                      node_color="lightblue",
                      node_size=4000,
                      alpha=0.8,
                      node_shape='s')

# Dibujar nodos de síntomas
nx.draw_networkx_nodes(grafo_nx, pos, 
                      nodelist=sintomas,
                      node_color="lightgreen",
                      node_size=3000,
                      alpha=0.8,
                      node_shape='o')

# Dibujar aristas
nx.draw_networkx_edges(grafo_nx, pos,
                      edge_color="gray",
                      arrows=True,
                      arrowsize=20)

# Agregar etiquetas
nx.draw_networkx_labels(grafo_nx, pos,
                       font_size=12,
                       font_weight="bold")

# Agregar leyenda
plt.text(-0.5, 1.15, 'Causas', bbox=dict(facecolor='lightblue', alpha=0.5))
plt.text(-0.5, -0.15, 'Síntomas', bbox=dict(facecolor='lightgreen', alpha=0.5))

plt.title("Red Bayesiana de Diagnóstico de Red - Datatech SRL", pad=20)
plt.axis('off')  # Ocultar ejes

# Ajustar márgenes
plt.tight_layout()

plt.show()
