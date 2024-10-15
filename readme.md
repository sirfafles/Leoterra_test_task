# Документация по запуску заданий

## Задание 1: Запуск Flask приложения с помощью Docker

1. **Перейдите в директорию с приложением:**
   Откройте терминал и выполните следующую команду, чтобы перейти в папку с Flask приложением:
   ```bash
   cd task1_flask_app/app
2. **Запустите Docker Compose:**
    Выполните команду ниже для запуска приложения с помощью Docker Compose:
     ```bash
     sudo docker-compose up
     ```
## Задание 2: Работа с базой данных и запуск скриптов
1. **Перейдите в директорию с заданием:**
Откройте новый терминал и выполните следующую команду для перехода в папку со вторым заданием:
    ```bash
    cd task_2
2. **Создайте базу данных:**
Запустите скрипт db_create.py, который создаст базу данных:
    ```bash
    python3 db_create.py
3. **Запустите скрипты для получения информации:**  
После успешного создания базы данных выполните следующие команды по очереди для запуска скриптов:
    ```bash
    python3 get_customer.py
    python3 get_banks.py
    ```