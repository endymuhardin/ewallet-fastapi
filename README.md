# Aplikasi E-Wallet dengan Fast API #


## Setup Project ##

1. Clone Repository

2. Create venv

    ```sh
    python3 -m venv .venv
    ```

3. Activate virtual environment

    ```sh
    source .venv/bin/activate
    ```

4. Install dependencies

    ```
    pip install -r requirements.txt
    ```

5. Run test

    ```
    pytest
    ```

6. Run App

    ```
    fastapi dev app/main.py
    ```


## Setup Database ##

1. Run docker compose untuk menjalankan database server

    ```sh
    docker compose up
    ```

2. Download driver database

    ```sh
    wget -c -P flyway/drivers "https://jdbc.postgresql.org/download/postgresql-42.7.4.jar"
    ```

3. Jalankan migrasi database

    ```sh
    docker run --rm --network=host -v ${PWD}/flyway:/flyway/project flyway/flyway migrate -workingDirectory="project"
    ```

4. Login ke database

    ```sh
    docker exec -it ewallet-fastapi-db-ewallet-1 psql -U ewallet -d ewalletdb
    ```

5. Cek isi database

    ```
    \d
    ```