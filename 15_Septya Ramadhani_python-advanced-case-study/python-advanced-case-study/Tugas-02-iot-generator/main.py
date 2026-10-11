def baca_suhu():
    """Menghasilkan data suhu secara bertahap."""
    for suhu in [16.5, 18.0, 19.8, 20.0, 22.4, 25.0, 27.6, 30.0, 31.5, 34.2, 37.0]:
        yield suhu

def kategori(suhu):
    if suhu < 20: return "Dingin"
    if suhu <= 30: return "Normal"
    return "Panas"

print("=== PEMANTAUAN SUHU SENSOR IoT ===")
sensor = baca_suhu()
for nomor in range(1, 11):
    suhu = next(sensor)
    print(f"Pembacaan ke-{nomor:02}: {suhu:4.1f} °C | Status: {kategori(suhu)}")
