def konversisuhu(temperature, value):  # Mendefinisikan fungsi konversisuhu dengan parameter temperature dan value
    if value == 'C':  # Memeriksa apakah unit suhu yang diberikan adalah 'C' (Celsius)
        temperaturesuhu = (temperature - 32) * 5/9  # Menghitung suhu dalam Celsius dari Fahrenheit
        return temperaturesuhu, 'C'  # Mengembalikan nilai suhu yang telah dikonversi dan unit 'C'
    else:  # Jika unit bukan 'C', eksekusi pindah ke blok ini
        temperaturesuhu = (temperature * 9/5) + 32  # Menghitung suhu dalam Fahrenheit dari Celsius
        return temperaturesuhu, 'F'  # Mengembalikan nilai suhu yang telah dikonversi dan unit 'F'

celsius_temperature = 30  # Mendefinisikan variabel celsius_temperature dengan nilai 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')  # Memanggil fungsi untuk konversi ke Fahrenheit
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")  # Mencetak hasil konversi Celsius ke Fahrenheit

fahrenheit_temperature = 86  # Mendefinisikan variabel fahrenheit_temperature dengan nilai 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')  # Memanggil fungsi untuk konversi ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")  # Mencetak hasil konversi Fahrenheit ke Celsius