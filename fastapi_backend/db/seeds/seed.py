from fastapi_backend.db.psql_connection import  get_conn 
from fastapi_backend.schemas.seed_models import Bubble, Visit, Pest, Data, BackgroundImage, Settings
from typing import List

async def run_seed(
        bubbles: List[Bubble],
        visits: List[Visit],
        pests: List[Pest],
        data: List[Data],
        backgroundimages: List[BackgroundImage],
        settings: List[Settings]
    ):

    async with  get_conn() as conn:
        async with conn.cursor() as cur:
            await cur.execute("""   
                DROP TABLE IF EXISTS backgroundimages;
                DROP TABLE IF EXISTS settings;
                DROP TABLE IF EXISTS data;
                DROP TABLE IF EXISTS bubbles;
                DROP TABLE IF EXISTS visits;
                DROP TABLE IF EXISTS pests;
            """)
            await cur.execute("""
                CREATE TABLE bubbles
                (
                bubble_id SERIAL PRIMARY KEY NOT NULL,
                label VARCHAR(200) NOT NULL,
                location_x INT DEFAULT 0 NOT NULL,
                location_y INT DEFAULT 0 NOT NULL
                )
            """)
            await cur.execute("""
                CREATE TABLE pests
                (
                pest_id SERIAL PRIMARY KEY NOT NULL,
                pest_name VARCHAR(200) NOT NULL
                )
            """)
            await cur.execute("""
                CREATE TABLE visits
                (
                visit_id SERIAL PRIMARY KEY NOT NULL,
                pest_id INT REFERENCES pests(pest_id),
                visit_name VARCHAR(200),
                visit_date TIMESTAMP NOT NULL
                )
            """)
            await cur.execute("""
                CREATE TABLE data
                (
                data_id SERIAL PRIMARY KEY NOT NULL,
                bubble_id INT REFERENCES bubbles(bubble_id) NOT NULL,
                visit_id INT REFERENCES visits(visit_id),
                value INT
                )
            """)
            await cur.execute("""
                CREATE TABLE backgroundimages
                (
                image_id SERIAL PRIMARY KEY NOT NULL,
                image_url TEXT
                )
            """)
            await cur.execute("""
                CREATE TABLE settings
                (
                setting_id SERIAL PRIMARY KEY NOT NULL,
                no_colors INT NOT NULL DEFAULT 20,
                bubble_size_min INT,
                bubble_size_max INT
                )
            """)