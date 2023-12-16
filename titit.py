import streamlit as st

def calculate_bmi(weight, height):
    # Konversi berat ke pound dan tinggi ke inci
    weight_pound = weight * 2.20462
    height_inch = height * 0.39
    
    # Hitung BMI
    bmi = (weight_pound * 703) / (height_inch ** 2)
    return bmi

# Tampilan web
st.title("Kalkulator BMI")
st.write(""" Web untuk menghitung indeks ke-idealan berat terhadap tinggi badan~~ dianajah""")

# Input berat dan tinggi
weight = st.number_input("Masukkan Berat Badan (kg):")
height = st.number_input("Masukkan Tinggi Badan (centimeter):")

# Tombol untuk menghitung BMI
if st.button("Hitung BMI"):
    bmi_result = calculate_bmi(weight, height)
    st.success(f"Indeks Massa Tubuh (BMI): {bmi_result:.2f}")

# Catatan tambahan
st.write("""
Catatan:
- BMI kurang dari 18.5: Kurus
- BMI antara 18.5 dan 24.9: Normal
- BMI lebih dari 25: Gemuk
- Semua butuh ngising dan protein
""")
st.markdown("[Link ke Google](http://192.168.20.82:8502)")