import json
import sqlite3


def get_customers():
    conn = sqlite3.connect("counterparties.db")
    cursor = conn.cursor()

    query = """
    SELECT id, internal_name, person, heads
    FROM counterparties
    ORDER BY person ASC, internal_name ASC;  -- Сортируем по типу и локальному имени
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print(
            "Список всех заказчиков (id, локальное имя, тип, актуальный руководитель):"
        )
        for row in rows:
            customer_id = row[0]
            internal_name = row[1]
            person = row[2]
            full_name_json = row[3]

            try:
                full_name_data = json.loads(full_name_json)
                actual_manager = (
                    list(full_name_data.keys())[0] if full_name_data else "Не указано"
                )
            except json.JSONDecodeError:
                actual_manager = "Ошибка в формате JSON"

            print(
                f"ID: {customer_id}, Локальное имя: {internal_name}, Тип: {person}, Актуальный руководитель: {actual_manager}"
            )
    else:
        print("Заказчики не найдены.")

    conn.close()


get_customers()
