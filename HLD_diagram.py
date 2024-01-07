pip install graphviz

from google.colab import drive

drive.mount('/content/drive/')

import graphviz

# Создаем объект графа
graph = graphviz.Digraph()

# Добавляем узлы
graph.node("API Service")
graph.node("Data Processing Service")
graph.node("Web Interface")
graph.node("Database")
graph.node("Message Queue")
graph.node("External Service 1")
graph.node("External Service 2")

# Добавляем связи между узлами
graph.edge("API Service", "Data Processing Service")
graph.edge("Data Processing Service", "Web Interface")
graph.edge("Data Processing Service", "Database")
graph.edge("Data Processing Service", "Message Queue")
graph.edge("Web Interface", "External Service 1")
graph.edge("Web Interface", "External Service 2")
graph.edge("Message Queue", "External Service 1")
graph.edge("Message Queue", "External Service 2")

# Отрисовка графа
graph.render("/content/drive/MyDrive/system_diagram_", format="png")
