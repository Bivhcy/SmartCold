from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# الاتصال بقاعدة البيانات
def get_connection():
    return psycopg2.connect(
        host="switchback.proxy.rlwy.net",
        port=15602,
        database="railway",
        user="postgres",
        password="eCIOwAfGhYmwaNcyvOIuqfHetYjXkole"
    )


@app.route("/")
def home():
    return "SmartCold API is Running Successfully 🚀"


@app.route("/sensor-data", methods=["POST"])
def sensor_data():

    try:

        # استقبال البيانات القادمة من ESP أو من test_send.py
        data = request.get_json()

        conn = get_connection()
        cur = conn.cursor()

        # حفظ البيانات في قاعدة البيانات
        cur.execute("""
            INSERT INTO sensor_readings
            (
                esp_id,
                temperature,
                humidity,
                gas,
                ethylene,
                door_status,
                reading_time
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            data["device_id"],
            data["temperature"],
            data["humidity"],
            data["gas"],
            data["ethylene"],
            data["door"],
            data["time"]
        ))

        conn.commit()

        cur.close()
        conn.close()

        return jsonify({
            "message": "Saved Successfully"
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)