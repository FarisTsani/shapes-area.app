import streamlit as st
from streamlit_option_menu import option_menu

#navigasi side bar

with st.sidebar :
    selected = option_menu ('Pilih Bangun Datar',
                            ['Persegi','Persegi Panjang','Segitiga'],
                            default_index=0)

#hitung luas persegi
if (selected == 'Persegi') :
    st.title('Luas Persegi')

    sisi = st.number_input ('Nilai Sisi :',0)
    hitung = st.button('Hitung Luas')

    if hitung :
        luas = sisi*sisi
        st.write ('Luas Persegi adalah =',luas)
        st.success(f'Luas Persegi adalah = {luas}')

#hitung luas persegi panjang
if (selected == 'Persegi Panjang') :
    st.title('Luas Persegi Panjang')

    panjang = st.number_input ('Nilai Panjang :',0)
    lebar = st.number_input ('Nilai Lebar :',0)
    hitung = st.button('Hitung Luas')

    if hitung :
        luas = panjang*lebar
        st.write ('Luas Persegi Panjang adalah =',luas)
        st.success(f'Luas Persegi Panjang adalah = {luas}')

#hitung luas segitiha
if (selected == 'Segitiga') :
    st.title('Luas Segitiga')

    alas = st.slider ('Masukkan Nilai alas :', 0, 100)
    tinggi = st.slider ('Masukkan Nilai tinggi :', 0, 100)
    hitung = st.button('Hitung Luas')

    if hitung :
        luas = (alas*tinggi)/2
        st.write ('Luas Segitiga adalah =',luas)
        st.success(f'Luas Segitiga adalah = {luas}')