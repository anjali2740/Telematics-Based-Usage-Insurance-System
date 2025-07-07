import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # change if needed
        password="root",  # change if needed
        database="telematics_insurance"
    )

def insert_data(driver_id, speed, acc, brake, distance, behavior, risk, premium, feedback):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO driving_data 
        (driver_id, speed, acceleration, braking, distance_travelled, behavior_score, risk_score, premium, feedback)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (driver_id, speed, acc, brake, distance, behavior, risk, premium, feedback))
    conn.commit()
    conn.close()

def fetch_data():
    conn = connect()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM driving_data")
    rows = cursor.fetchall()
    conn.close()
    return rows
