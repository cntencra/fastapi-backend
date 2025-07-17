from fastapi_backend.db.db_manager import  DBManager
from fastapi_backend.db.schemas.seed_models import SeedDataDB

async def seed(
        db_manager: DBManager,
        seed_data: SeedDataDB
    ):

    async with  db_manager.get_conn() as conn:
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
                value INT,
                pest_id INT REFERENCES pests(pest_id)
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
            await cur.executemany("""
                INSERT INTO bubbles (label, location_x, location_y)
                VALUES (%s, %s, %s)
            """, [(bubble.label, bubble.location_x, bubble.location_y) for bubble in seed_data.bubbles])
            await cur.executemany("""
                INSERT INTO pests (pest_name)
                VALUES (%s)
            """, [(pest.pest_name,) for pest in seed_data.pests])
            await cur.executemany("""
                INSERT INTO visits (visit_name, visit_date)
                VALUES (%s, %s)
            """, [(visit.visit_name, visit.visit_date) for visit in seed_data.visits])
            await cur.executemany("""
                INSERT INTO data (bubble_id, visit_id, value, pest_id)
                VALUES (%s, %s, %s, %s)
            """, [(datum.bubble_id, datum.visit_id, datum.value, datum.pest_id ) for datum in seed_data.data])
            await cur.executemany("""
                INSERT INTO backgroundimages (image_url)
                VALUES (%s)
            """, [(image.image_url,) for image in seed_data.backgroundimages])
            await cur.executemany("""
                INSERT INTO settings (no_colors, bubble_size_min, bubble_size_max)
                VALUES (%s, %s, %s)
            """, [(setting.no_colors, setting.bubble_size_min, setting.bubble_size_max) for setting in seed_data.settings])
            await conn.commit()