data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 88, "uts": 91, "uas": 90},
]

mahasiswa = [{**m, "nilai_akhir": round(m["tugas"] * .30 + m["uts"] * .30 + m["uas"] * .40, 2)} for m in data_mahasiswa]
berprestasi = [m for m in mahasiswa if m["nilai_akhir"] > 80]
peringkat = sorted(mahasiswa, key=lambda m: m["nilai_akhir"], reverse=True)

print("=== ANALISIS NILAI MAHASISWA ===")
print("Bobot: Tugas 30% | UTS 30% | UAS 40%")
print("\nDAFTAR NILAI AKHIR")
for m in mahasiswa:
    print(f'{m["nama"]:<10} NIM: {m["nim"]} | Nilai akhir: {m["nilai_akhir"]:.2f}')
print("\nMAHASISWA BERPRESTASI (nilai > 80)")
for m in berprestasi:
    print(f'- {m["nama"]} ({m["nim"]}) - {m["nilai_akhir"]:.2f}')
print("\nPERINGKAT")
for i, m in enumerate(peringkat, 1):
    print(f'{i}. {m["nama"]} ({m["nim"]}) - {m["nilai_akhir"]:.2f}')
terbaik = peringkat[0]
print(f'\nMAHASISWA TERBAIK: {terbaik["nama"]}, NIM {terbaik["nim"]}, nilai {terbaik["nilai_akhir"]:.2f}')
