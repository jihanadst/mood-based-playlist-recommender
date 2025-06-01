import random

# Data awal lagu
playlist = [
    {'Judul': 'like JENNIE', 'Artis': 'JENNIE', 'Mood': 'happy'},
    {'Judul': 'Membasuh', 'Artis': 'Hindia', 'Mood': 'sad'},
    {'Judul': 'Bags', 'Artis': 'Clairo', 'Mood': 'chill'},
    {'Judul': 'Supernatural', 'Artis': 'Ariana Grande', 'Mood': 'energetic'},
    {'Judul': 'Sunflower', 'Artis': 'Post Malone', 'Mood': 'chill'}
]

# Deteksi mood dari kalimat
def deteksi_mood(kalimat):
    kalimat = kalimat.lower()
    if "senang" in kalimat or "bahagia" in kalimat:
        return "happy"
    elif "sedih" in kalimat or "galau" in kalimat:
        return "sad"
    elif "lelah" in kalimat or "santai" in kalimat:
        return "chill"
    elif "semangat" in kalimat or "energi" in kalimat:
        return "energetic"
    else:
        return None

# Tampilkan daftar mood yang tersedia
print("🎧 Kamu bisa masukkan kalimat bebas, contoh:")
print("- Aku lagi bahagia banget")
print("- Lagi galau dan sedih")
print("- Butuh energi")
print("- Pengen rebahan")

kalimat = input("\nTuliskan suasana hatimu saat ini: ")
mood_input = deteksi_mood(kalimat)

if mood_input:
    print(f"\n✅ Mood terdeteksi: {mood_input}")

    # Simpan ke histori
    with open("mood_history.txt", "a", encoding="utf-8") as f:
        f.write(f"{mood_input}\n")

    # Filter lagu sesuai mood
    hasil = [lagu for lagu in playlist if lagu['Mood'] == mood_input]

    if hasil:
        print("\n🎶 Lagu sesuai mood kamu:")
        for lagu in hasil:
            print(f"- {lagu['Judul']} oleh {lagu['Artis']}")

        rekomendasi = random.choice(hasil)
        print(f"\n⭐ Rekomendasi spesial: {rekomendasi['Judul']} oleh {rekomendasi['Artis']}")

        # Favoritkan lagu
        fav = input("\nMau simpan salah satu lagu ke favorit? (ya/tidak): ").lower()
        if fav == "ya":
            judul_fav = input("Masukkan judul lagu yang kamu suka: ")
            found = next((lagu for lagu in hasil if lagu['Judul'].lower() == judul_fav.lower()), None)
            if found:
                with open("favorit.txt", "a", encoding="utf-8") as f:
                    f.write(f"{found['Judul']} - {found['Artis']} [{found['Mood']}]\n")
                print("⭐ Lagu ditambahkan ke daftar favorit!")
            else:
                print("❌ Lagu tidak ditemukan.")
    else:
        print("❌ Tidak ada lagu dengan mood tersebut.")

else:
    print("❌ Tidak bisa mendeteksi mood dari kalimat kamu.")

# Tambah lagu baru
tambah = input("\nApakah kamu ingin menambahkan lagu baru? (ya/tidak): ").lower()
if tambah == "ya":
    judul = input("Judul lagu: ")
    artis = input("Artis: ")
    mood = input("Mood: ").lower()
    playlist.append({'Judul': judul, 'Artis': artis, 'Mood': mood})
    print("✅ Lagu berhasil ditambahkan!")

# Simpan playlist ke file
simpan = input("\nApakah kamu ingin menyimpan playlist ke file? (ya/tidak): ").lower()
if simpan == "ya":
    with open("playlist_kamu.txt", "w", encoding="utf-8") as f:
        for lagu in playlist:
            f.write(f"{lagu['Judul']} - {lagu['Artis']} [{lagu['Mood']}]\n")
    print("📁 Playlist berhasil disimpan ke 'playlist_kamu.txt'")

# Statistik mood manual tanpa Counter
lihat_stat = input("\nMau lihat statistik mood kamu? (ya/tidak): ").lower()
if lihat_stat == "ya":
    try:
        with open("mood_history.txt", "r", encoding="utf-8") as f:
            moods = f.read().splitlines()

        if moods:
            print("\n📊 Statistik mood kamu:")
            statistik = {}
            for mood in moods:
                if mood in statistik:
                    statistik[mood] += 1
                else:
                    statistik[mood] = 1

            for mood, count in sorted(statistik.items(), key=lambda item: item[1], reverse=True):
                print(f"- {mood}: {count}x")
        else:
            print("Belum ada data mood.")
    except FileNotFoundError:
        print("Belum ada histori mood.")

print("\nTerima kasih sudah menggunakan Playlist Rekomendasi! 🎵")
