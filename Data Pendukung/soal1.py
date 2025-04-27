def deteksi_hama(gejala):
    G1 = gejala.get("daun_menguning", False)
    G2 = gejala.get("bercak_hitam", False)
    G3 = gejala.get("daun_berlubang", False)
    G4 = gejala.get("tanaman_layu", False)

    hasil = []

    if G1 and G4:
        hasil.append("Wereng")
    if G2 and G4:
        hasil.append("Jamur Patogen")
    if G3 and G1:
        hasil.append("Ulat Grayak")
    if G1 and G2 and G4:
        hasil.append("Kutu Daun")

    if not hasil:
        return "Hama tidak teridentifikasi berdasarkan gejala yang diberikan."
    return "Hama yang terdeteksi: " + ', '.join(set(hasil))
    
# Contoh penggunaan:
gejala_input = {
    "daun_menguning": True,
    "bercak_hitam": True,
    "daun_berlubang": False,
    "tanaman_layu": True
}

print(deteksi_hama(gejala_input))
