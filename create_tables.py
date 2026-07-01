import psycopg2

conn = psycopg2.connect(
    host="switchback.proxy.rlwy.net",
    port=15602,
    database="railway",
    user="postgres",
    password="eCIOwAfGhYmwaNcyvOIuqfHetYjXkole"
)

cur = conn.cursor()

# ===========================
# Storage
# ===========================
cur.execute("""
CREATE TABLE IF NOT EXISTS storages(
    storage_id SERIAL PRIMARY KEY,
    storage_name VARCHAR(100),
    location VARCHAR(100)
);
""")

# ===========================
# ESP Devices
# ===========================
cur.execute("""
CREATE TABLE IF NOT EXISTS esp_devices(
    esp_id SERIAL PRIMARY KEY,
    device_name VARCHAR(50),
    storage_id INTEGER REFERENCES storages(storage_id),
    position VARCHAR(100)
);
""")

# ===========================
# Sensor Readings
# ===========================
cur.execute("""
CREATE TABLE IF NOT EXISTS sensor_readings(
    reading_id SERIAL PRIMARY KEY,
    esp_id INTEGER REFERENCES esp_devices(esp_id),

    temperature FLOAT,
    humidity FLOAT,

    gas FLOAT,
    ethylene FLOAT,

    door_status BOOLEAN,

    reading_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# ===========================
# Actuators
# ===========================
cur.execute("""
CREATE TABLE IF NOT EXISTS actuators(
    actuator_id SERIAL PRIMARY KEY,

    storage_id INTEGER REFERENCES storages(storage_id),

    actuator_type VARCHAR(50),

    position VARCHAR(100)
);
""")

# ===========================
# Actuator Log
# ===========================
cur.execute("""
CREATE TABLE IF NOT EXISTS actuator_log(

    log_id SERIAL PRIMARY KEY,

    actuator_id INTEGER REFERENCES actuators(actuator_id),

    action VARCHAR(20),

    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()

cur.close()
conn.close()

print("All Tables Created Successfully")