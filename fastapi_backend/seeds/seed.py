from fastapi_backend.db.psql_connection import pool

def run_seed():
    conn = pool

    with pool.connection() as conn:
        conn.execute("""
            DROP TABLE IF EXISTS bubbles;
            DROP TABLE IF EXISTS visits;
            DROP TABLE IF EXISTS pests;
            DROP TABLE IF EXISTS data;
            DROP TABLE IF EXISTS backgroundimages;
            DROP TABLE IF EXISTS settings;
        """)
        conn.execute("""
            CREATE TABLE bubbles
            (
            bubble_id SERIAL PRIMARY KEY NOT NULL,
            label VARCHAR(200) NOT NULL,
            location_x INT DEFAULT 0 NOT NULL,
            location_y INT DEFAULT 0 NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE visits
            (
            visit_id SERIAL PRIMARY KEY NOT NULL,
            year INT NOT NULL,
            visit_name VARCHAR(200),
            visit_date TIMESTAMP NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE pests
            (
            pest_id SERIAL PRIMARY KEY NOT NULL,
            pest_name VARCHAR(200) NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE data
            (
            data_id SERIAL PRIMARY KEY NOT NULL,
            bubble_id INT REFERENCES bubbles(bubble_id) NOT NULL,
            visit_id INT REFERENCES visits(visit_id),
            pest_id INT REFERENCES pests(pest_id),
            value INT
            )
        """)
        conn.execute("""
            CREATE TABLE backgroundimages
            (
            image_id SERIAL PRIMARY KEY NOT NULL,
            image_url TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE settings
            (
            setting_id SERIAL PRIMARY KEY NOT NULL,
            no_colors INT NOT NULL DEFAULT 20,
            bubble_size_min INT,
            bubble_size_max INT
            )
        """)
    
    conn.close()


