from session import my_engine

try:
    conn = my_engine.connect()
    print("✅ DB CONNECTED")
    conn.close()
except Exception as e:
    print("❌ DB FAILED:", e)