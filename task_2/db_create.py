import sqlite3

# Подключаемся к базе данных (если файла нет, он будет создан)
conn = sqlite3.connect("counterparties.db")
cursor = conn.cursor()

# SQL-запросы для создания таблиц и вставки данных
sql_script = """
CREATE TABLE IF NOT EXISTS type_person(
    value varchar(16) PRIMARY KEY
);

INSERT INTO type_person(value) VALUES
('Юр. лицо'),
('Физ. лицо');

CREATE TABLE IF NOT EXISTS counterparties(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    internal_name   varchar(64)     NOT NULL UNIQUE,
    person          varchar(16)     NOT NULL REFERENCES type_person(value) DEFAULT 'Юр. лицо',
    INN             varchar(12)     NOT NULL UNIQUE,
    KPP             varchar(9),
    OGRN            varchar(15)     UNIQUE,
    heads           json            NOT NULL DEFAULT '{"Фамилия Имя Отчество": {"position": "Должность", "surname": "Фамилия", "first_name": "Имя", "middle_name": "Отчество", "sex": "Пол", "act_upon": "Устава", "from_date_of": "2000-01-01", "up_to_date_of": ""}}',
    banks           json            NOT NULL DEFAULT '{"Название банка": {"account": "00000000000000000000", "name": "Наименование банка", "corr_account": "00000000000000000000", "bik": "000000000"}}',
    full_name       varchar(512)    NOT NULL,
    active          boolean         NOT NULL DEFAULT true
);

INSERT INTO counterparties(internal_name, INN, KPP, OGRN, heads, banks, full_name) VALUES
('Компания 1', '5073530173', '504120546', '5644193644208', '{"Петров Евгений Васильевич": {"position": "Генеральный директор", "surname": "Петров", "first_name": "Евгений", "middle_name": "Васильевич", "sex": "male", "act_upon": "Устава", "from_date_of": "2009-11-16", "up_to_date_of": ""}}', '{"Банк ВТБ": {"account": "46235285108075356324", "name": "Банк ВТБ", "corr_account": "82456846202400480848", "bik": "715493251"}}', 'Общество с ограниченной ответственностью "Компания Первых"'),
('Компания Егора', '5091475412', '506193519', '2883519172040', '{"Поддубный Егор Дмитрович": {"position": "Директор", "surname": "Поддубный", "first_name": "Егор", "middle_name": "Дмитрович", "sex": "male", "act_upon": "Устава", "from_date_of": "2012-10-01", "up_to_date_of": ""}}', '{"Банк СБЕР": {"account": "91423421155207912522", "name": "Банк СБЕР", "corr_account": "03610058264387258146", "bik": "520474627"}}', 'Общество с ограниченной ответственностью "ПЕДСтрой"'),
('ООО Вымпелком', '5018246125', '505239156', '7256372514834', '{"Разумовский Виктор Игоревич": {"position": "Исполнительный директор", "surname": "Разумовский", "first_name": "Виктор", "middle_name": "Игоревич", "sex": "male", "act_upon": "Устава", "from_date_of": "2021-04-09", "up_to_date_of": ""}, "Никифоров Арсений Витальевич": {"position": "Генеральный директор", "surname": "Никифоров", "first_name": "Арсений", "middle_name": "Витальевич", "sex": "male", "act_upon": "Устава", "from_date_of": "2016-04-03", "up_to_date_of": "2021-04-09"}}', '{"Банк ГАЗПРОМ": {"account": "84629341521383256729", "name": "Банк ГАЗПРОМ", "corr_account": "12493746237492990023", "bik": "718544306"}}', 'Общество с ограниченной ответственностью "Вымпелком"'),
('Рога и копыта', '5084764622', '507477325', '6407886451211', '{"Курпина Евгения Анатольевна": {"position": "Генеральный директор", "surname": "Курпина", "first_name": "Евгения", "middle_name": "Анатольевна", "sex": "female", "act_upon": "Устава", "from_date_of": "2013-06-21", "up_to_date_of": ""}}', '{"Банк Тинькоф": {"account": "94854348840008631648", "name": "Банк Тинькоф", "corr_account": "74746662829900034332", "bik": "932113118"}}', 'Общество с ограниченной ответственностью "Рога и Копыта"');
"""

# Выполняем SQL-запросы
cursor.executescript(sql_script)

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()

print("Таблицы успешно созданы и данные добавлены!")
