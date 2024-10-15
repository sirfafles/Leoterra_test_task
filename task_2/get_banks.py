import json
import sqlite3


def get_banks_info_by_id(unique_id):
    conn = sqlite3.connect("counterparties.db")
    cursor = conn.cursor()

    query = """
    SELECT 
        json_each.value AS bank_info
    FROM counterparties
    JOIN json_each(banks) ON 1=1
    WHERE counterparties.id = ?;
    """

    cursor.execute(query, (unique_id,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            bank_info_str = row[0]
            bank_info = json.loads(bank_info_str)

            # Извлекаем необходимые поля
            name = bank_info.get("name", "N/A")
            account = bank_info.get("account", "N/A")
            corr_account = bank_info.get("corr_account", "N/A")
            bik = bank_info.get("bik", "N/A")

            print(
                f"Название банка: {name}, Расчетный счет: {account}, Корреспондентский счет: {corr_account}, БИК: {bik}"
            )
    else:
        print(f"Банки не найдены для заказчика с id {unique_id}.")

    conn.close()


# Пример использования функции
bank_id = int(input("Введите нужный id записи"))
get_banks_info_by_id(bank_id)
