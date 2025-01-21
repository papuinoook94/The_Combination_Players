import mysql.connector
from db_utils import get_connection, fetch_players, calculate_combinations

def main():
    conn = get_connection()
    players = fetch_players(conn)

    positions_def = [
        "extremo_izquierdo_def", "segundo_izquierdo_60", "central_def",
        "central_def", "segundo_derecho_60", "extremo_derecho_def"
    ]

    positions_of = [
        "extremo_izquierdo", "lateral_izquierdo", "central_of",
        "pivote", "lateral_derecho", "extremo_derecho_of"
    ]

    combinations = calculate_combinations(players, positions_def, positions_of)
    for combo in combinations[:5]:  # Mostrar las 5 mejores combinaciones
        print(combo)

if __name__ == "__main__":
    main()
