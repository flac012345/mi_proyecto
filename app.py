from flask import Flask, render_template, jsonify

app = Flask(__name__)

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "category": "Arquitectura de Software",
        "topic": "Arquitectura Hexagonal (Ports & Adapters)",
        "question": "¿Cuál es el propósito principal de la Arquitectura Hexagonal?",
        "options": [
            "Obligar al uso de bases de datos NoSQL para ganar escalabilidad horizontal.",
            "Aislar la lógica de dominio de frameworks, bases de datos y agentes externos mediante interfaces y adaptadores.",
            "Reemplazar las APIs REST por WebSockets para comunicación bidireccional.",
            "Empaquetar la aplicación en exactamente seis contenedores Docker independientes."
        ],
        "answer": 1,
        "explanation": "La Arquitectura Hexagonal desacopla el núcleo de negocio (dominio) de los detalles de infraestructura externa (UI, BD, APIs de terceros) mediante puertos (interfaces) y adaptadores (implementaciones concretas)."
    },
    {
        "id": 2,
        "category": "Estrategia de Stack",
        "topic": "Monolito Modular vs Microservicios",
        "question": "En un sistema en fase temprana con un equipo pequeño, ¿por qué suele recomendarse un Monolito Modular antes que Microservicios?",
        "options": [
            "Porque los microservicios son incompatibles con bases de datos relacionales como PostgreSQL.",
            "Para evitar la sobrecarga operacional (latencia de red, consistencia distribuida, despliegues complejos) y acelerar iteraciones.",
            "Porque un monolito siempre tiene menor consumo de memoria y CPU sin importar la carga.",
            "Porque los monolitos no requieren pruebas unitarias ni entornos de integración continua."
        ],
        "answer": 1,
        "explanation": "Los microservicios añaden complejidad distribuida significativa (observabilidad, transacciones complejas, orquestación). Un monolito bien modularizado permite iterar y refactorizar con alta velocidad sin esa sobrecarga."
    },
    {
        "id": 3,
        "category": "Sistemas Distribuidos",
        "topic": "Arquitectura Orientada a Eventos (EDA) & Brokers",
        "question": "Al integrar un Message Broker como Apache Kafka o RabbitMQ, ¿qué ventaja ofrece el desacoplamiento temporal?",
        "options": [
            "Permite a los productores emitir eventos sin depender de que los consumidores estén activos o procesen de inmediato.",
            "Elimina por completo la necesidad de almacenamiento persistente en bases de datos.",
            "Garantiza que el tiempo de respuesta HTTP hacia el cliente final sea 0 ms.",
            "Hace innecesario el uso de cifrado TLS o protocolos seguros en la red."
        ],
        "answer": 0,
        "explanation": "El desacoplamiento temporal posibilita la comunicación asíncrona: los productores publican mensajes a la cola/tópico y los consumidores procesan a su propio ritmo según su capacidad."
    },
    {
        "id": 4,
        "category": "Teoría de Sistemas",
        "topic": "Teorema CAP & Consistencia",
        "question": "En presencia de una partición de red (P) en un sistema distribuido, ¿qué establece el Teorema CAP?",
        "options": [
            "Se debe elegir entre usar Python o Go para optimizar el throughput de la partición.",
            "Se debe elegir entre Consistencia (C: todos los nodos ven el mismo dato) o Disponibilidad (A: cada petición recibe respuesta).",
            "El sistema se recupera automáticamente duplicando la memoria de los nodos afectados.",
            "La partición debe resolverse reiniciando inmediatamente todos los servidores de base de datos."
        ],
        "answer": 1,
        "explanation": "El Teorema CAP demuestra que ante un fallo de red inevitable (P), no es posible garantizar simultáneamente consistencia estricta (C) y disponibilidad total (A); se debe priorizar una de las dos."
    },
    {
        "id": 5,
        "category": "Rendimiento y Stack",
        "topic": "Patrón Cache-Aside (Lazy Loading)",
        "question": "¿Cómo opera el patrón Cache-Aside con una base de datos relacional y un caché en memoria como Redis?",
        "options": [
            "La aplicación consulta primero el caché; ante un 'cache miss', lee de la BD, guarda el dato en Redis y retorna el resultado.",
            "La base de datos actualiza el caché de forma síncrona en cada transacción antes del commit en disco.",
            "Todas las solicitudes de lectura y escritura son redirigidas exclusivamente a la memoria RAM del cliente.",
            "El caché reemplaza completamente el almacenamiento físico de la base de datos."
        ],
        "answer": 0,
        "explanation": "En Cache-Aside, la aplicación administra directamente el caché: si el dato está en Redis se retorna de inmediato; si no, se busca en la base de datos y se carga en el caché con un TTL apropiado."
    },
    {
        "id": 6,
        "category": "Patrones de Integración",
        "topic": "Backend for Frontend (BFF)",
        "question": "¿Cuál es la motivación técnica primordial para implementar el patrón BFF?",
        "options": [
            "Permitir que un solo archivo HTML sea renderizado en microcontroladores sin navegador.",
            "Crear una capa de backend optimizada específicamente para las necesidades de consumo de cada cliente (Web, Móvil, IoT).",
            "Eliminar la necesidad de autenticación y autorización en los servicios de negocio.",
            "Migrar automáticamente código de frontend en JavaScript a código backend en C++."
        ],
        "answer": 1,
        "explanation": "El patrón BFF crea servicios de backend dedicados para cada experiencia de usuario (ej. app móvil vs desktop), adaptando payloads, agregando llamadas y minimizando el uso de red según las características de cada cliente."
    }
]

AUTHOR_INFO = {
    "name": "Miguel Ángel Raigosa Sánchez",
    "role": "Ingeniería Informática (6.° Semestre) | Desarrollador Full Stack & Web",
    "bio": "Estudiante de sexto semestre de Ingeniería Informática y Desarrollador Full Stack & Web. Apasionado por Python, Flask, diseño de arquitecturas limpias y tecnologías web modernas y escalables.",
    "skills": ["Full-Stack & Web Dev", "Python / Flask", "JavaScript Moderno", "Arquitectura de Software", "APIs RESTful", "Bases de Datos", "Docker & Git", "Clean Code"],
    "quote": "«Construyendo software con propósito: código limpio, arquitecturas escalables y soluciones web modernas.»"
}

@app.route('/')
def home():
    return render_template('index.html', questions=QUIZ_QUESTIONS, author=AUTHOR_INFO)

@app.route('/api/quiz')
def get_quiz():
    return jsonify({
        "questions": QUIZ_QUESTIONS,
        "total": len(QUIZ_QUESTIONS)
    })

if __name__ == '__main__':
    app.run(debug=True)