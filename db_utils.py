import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="jugadores_db"
    )

def calculate_combinations(players, positions_def, positions_of):
    """
    Calcula combinaciones óptimas de jugadores considerando valores defensivos, ofensivos y generales.

    Args:
        players (DataFrame): DataFrame con los datos de los jugadores.
        positions_def (list): Lista de posiciones defensivas.
        positions_of (list): Lista de posiciones ofensivas.

    Returns:
        DataFrame: Combinaciones ordenadas por valores defensivo, ofensivo, general y total.
    """
    from itertools import permutations
    import pandas as pd

    # Calcular el puntaje total para cada jugador considerando todas las posiciones posibles
    players["Puntaje Total"] = players.apply(
        lambda row: sum(row[pos] for pos in positions_def + positions_of) + row["General"],
        axis=1
    )

    # Ordenar jugadores por puntaje total
    players = players.sort_values(by="Puntaje Total", ascending=False)

    # Obtener los nombres de los jugadores ordenados por su puntaje total
    jugadores = players["Nombres"].tolist()

    # Generar todas las combinaciones de 6 jugadores
    combinaciones = list(permutations(jugadores, 6))

    resultados = []
    for combinacion in combinaciones:
        valor_def = 0
        valor_of = 0
        valor_gen = 0

        # Evaluar cada jugador en su mejor posición defensiva y ofensiva
        for i, jugador in enumerate(combinacion):
            jugador_data = players[players["Nombres"] == jugador].iloc[0]

            # Mejor valor defensivo y ofensivo para el jugador
            mejor_valor_def = max(jugador_data[pos] for pos in positions_def)
            mejor_valor_of = max(jugador_data[pos] for pos in positions_of)

            valor_def += mejor_valor_def
            valor_of += mejor_valor_of
            valor_gen += jugador_data["General"]

        suma_total = valor_def + valor_of + valor_gen

        resultados.append({
            "Combinación": combinacion,
            "Valor Defensivo": valor_def,
            "Valor Ofensivo": valor_of,
            "Valor General": valor_gen,
            "Suma Total": suma_total
        })

    # Crear un DataFrame con los resultados y ordenarlo por la suma total
    return pd.DataFrame(resultados).sort_values(by="Suma Total", ascending=False)
