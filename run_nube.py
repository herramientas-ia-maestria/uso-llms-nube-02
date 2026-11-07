"""
"""

import requests
from config import API_KEY, URL, MODEL

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def uso_api_openrouter(frase):
    prompt = f"""
Clasifica la siguiente frase en una sola categoría.

Categorías permitidas:
deportes, crónica roja, política, economía, salud, educación, tecnología.
Cuando no tengas claro qué categoría, usar: sin categoria
Responde únicamente con el nombre de la categoría.

Frase:
"{frase}"
"""

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0,
        "max_tokens": 100
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=data,
        timeout=60
    )

    response.raise_for_status()
    # print(response.json())

    return response.json()["choices"][0]["message"]["content"].strip().lower()


def clasificar():
    lineas = [
        "La selección ecuatoriana de fútbol consiguió una importante victoria en las eliminatorias mundialistas.",
        "La Policía Nacional detuvo a cinco sospechosos durante un operativo contra el crimen organizado.",
        "El presidente anunció nuevas reformas destinadas a mejorar la administración pública.",
        "El Banco Central informó sobre un incremento en las exportaciones durante el último trimestre.",
        "Especialistas recomiendan realizar actividad física diariamente para prevenir enfermedades cardiovasculares.",
        "Varias universidades incorporan herramientas de inteligencia artificial en sus programas académicos.",
        "Una empresa tecnológica presentó un nuevo procesador diseñado para acelerar modelos de inteligencia artificial.",
        "Un equipo de investigadores desarrolla una vacuna experimental contra una enfermedad infecciosa.",
        "La Asamblea Nacional inició el debate de una propuesta de reforma electoral.",
        "Los precios de los productos agrícolas registraron variaciones en los mercados nacionales."
    ]
    # lineas = [s.replace("\n", "") for s in lineas]
    # lineas = [s.split("|") for s in lineas]

    for l in lineas[0:1]:
        print(l)
        print(uso_api_openrouter(l))
        print("--------------------")


if __name__ == "__main__":
    clasificar()
