import streamlit as st
from streamlit_option_menu import option_menu

#Navigasi sidebar
with st.sidebar :
    selected = option_menu ('Konversi Satuan (by: Rijallatipudin)',
    ['Konversi satuan panjang', 'Konversi satuan luas', 'Konversi satuan volume', 'Konversi satuan massa',
    'Konversi satuan gaya', 'Konversi satuan suhu', 'Konversi mutu beton'],
    default_index=0)

#halaman Konversi satuan panjang
if (selected == 'Konversi satuan panjang') :
    st.title('konversi satuan panjang')
    
    length = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
    unit1 = st.selectbox("Pilih satuan awal", ["mm", "cm", "dm", "m", "dam", "hm", "km", "inchi"])
    unit2 = st.selectbox("Pilih satuan tujuan", ["mm", "cm", "dm", "m", "dam", "hm", "km", "inchi"])

    def convert(length, unit1, unit2):
        if unit1 == "mm":
            if unit2 == "cm":
                return length / 10
            elif unit2 == "dm":
                return length / 100
            elif unit2 == "m":
                return length / 1000
            elif unit2 == "dam":
                return length / 10000
            elif unit2 == "hm":
                return length / 100000
            elif unit2 == "km":
                return length / 1000000
            elif unit2 == "mm":
                return length / 1
        if unit1 == "cm":
            if unit2 == "dm":
                return length / 10
            elif unit2 == "m":
                return length / 100
            elif unit2 == "dam":
                return length / 1000
            elif unit2 == "hm":
                return length / 10000
            elif unit2 == "km":
                return length / 100000
            elif unit2 == "cm":
                return length / 1
        if unit1 == "dm":
            if unit2 == "m":
                return length / 10
            elif unit2 == "dam":
                return length / 100
            elif unit2 == "hm":
                return length / 1000
            elif unit2 == "km":
                return length / 10000
            elif unit2 == "dm":
                return length / 1
        if unit1 == "m":
            if unit2 == "dam":
                return length / 10
            elif unit2 == "hm":
                return length / 100
            elif unit2 == "km":
                return length / 1000
            elif unit2 == "m":
                return length / 1
        if unit1 == "dam":
            if unit2 == "hm":
                return length / 10
            elif unit2 == "km":
                return length / 100
            elif unit2 == "dam":
                return length / 1
        if unit1 == "hm":
            if unit2 == "km":
                return length / 10
            elif unit2 == "hm":
                return length / 1
        if unit1 == "km":
            if unit2 == "hm":
                return length * 10
            elif unit2 == "dam":
                return length * 100
            elif unit2 == "m":
                return length * 1000
            elif unit2 == "dm":
                return length * 10000
            elif unit2 == "cm":
                return length * 100000
            elif unit2 == "mm":
                return length * 1000000
            elif unit2 == "km":
                return length * 1
        if unit1 == "hm":
            if unit2 == "dam":
                return length * 10
            elif unit2 == "m":
                return length * 100
            elif unit2 == "dm":
                return length * 1000
            elif unit2 == "cm":
                return length * 10000
            elif unit2 == "mm":
                return length * 100000
            elif unit2 == "km":
                return length * 1
        if unit1 == "dam":
            if unit2 == "dam":
                return length * 1
            elif unit2 == "m":
                return length * 10
            elif unit2 == "dm":
                return length * 100
            elif unit2 == "cm":
                return length * 1000
            elif unit2 == "mm":
                return length * 10000
        if unit1 == "m":
            if unit2 == "m":
                return length * 1
            elif unit2 == "dm":
                return length * 10
            elif unit2 == "cm":
                return length * 100
            elif unit2 == "mm":
                return length * 1000
        if unit1 == "dm":
            if unit2 == "dm":
                return length * 1
            elif unit2 == "cm":
                return length * 10
            elif unit2 == "mm":
                return length * 100
        if unit1 == "cm":
            if unit2 == "cm":
                return length * 1
            elif unit2 == "mm":
                return length * 10
        if unit1 == "mm":
            if unit2 == "mm":
                return length * 1
            
        if unit1 == "km":
            if unit2 == "inchi":
                return length / 0.0000254
        if unit1 == "hm":
            if unit2 == "inchi":
                return length / 0.000254
        if unit1 == "dam":
            if unit2 == "inchi":
                return length / 0.00254
        if unit1 == "m":
            if unit2 == "inchi":
                return length / 0.0254
        if unit1 == "dm":
            if unit2 == "inchi":
                return length / 0.254
        if unit1 == "cm":
            if unit2 == "inchi":
                return length / 2.54
        if unit1 == "mm":
            if unit2 == "inchi":
                return length / 25.4
            
        if unit1 == "inchi":
            if unit2 == "km":
                return length * (2.54 / 100000)
        if unit1 == "inchi":
            if unit2 == "hm":
                return length * (2.54 / 10000)
        if unit1 == "inchi":
            if unit2 == "dam":
                return length * (2.54 / 1000)
        if unit1 == "inchi":
            if unit2 == "m":
                return length * (2.54 / 100)
        if unit1 == "inchi":
            if unit2 == "dm":
                return length * (2.54 / 10)
        if unit1 == "inchi":
            if unit2 == "cm":
                return length * (2.54 / 1)
        if unit1 == "inchi":
            if unit2 == "mm":
                return length * (2.54 * 10)

    if st.button("Konversi"):
        result = convert(length, unit1, unit2)
        st.success(f"{length} {unit1} = {result} {unit2}")
        st.text('satuan metrik (SI) : mm, cm, dm, m, dam, hm, km.')
        st.text('satuan imperial : inchi, kaki, mil, yard.')


#halaman Konversi satuan gaya
if (selected == 'Konversi satuan gaya') :
    st.title('Konversi satuan gaya')
    option_unit_from = ['Newton', 'KN']
    value = st.number_input('Masukkan nilai yang akan dikonversi:')
    option_unit_to = ['Newton', 'KN']
    
    unit_from = st.selectbox('Satuan dari:', option_unit_from)
    unit_to = st.selectbox('Satuan menjadi:', option_unit_to)
    
    def convert_newton(value, unit_from, unit_to):
        if unit_from == 'KN':
            value = value * 1000
        if unit_from == 'Newton':
            value = value / 1000
    
        return value
    def show_result(value, unit_from, unit_to, result):
        st.write(value, unit_from, '=', result, unit_to)
    
    if st.button('Konversi'):
        if unit_from == unit_to:
            st.warning('Satuan tidak boleh sama')
        else:
            if unit_from == 'Newton':
                result = convert_newton(value, unit_from, unit_to)
                show_result(value, unit_from, unit_to, result)
            if unit_from == 'KN':
                result = convert_newton(value, unit_from, unit_to)
                show_result(value, unit_from, unit_to, result)

#halaman Konversi satuan luas
if (selected == 'Konversi satuan luas') :
    st.title('Konversi satuan luas')
    length = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
    unit1 = st.selectbox("Pilih satuan awal", ["mm^2", "cm^2", "dm^2", "m^2", "dam^2", "hm^2", "km^2"])
    unit2 = st.selectbox("Pilih satuan tujuan", ["mm^2", "cm^2", "dm^2", "m^2", "dam^2", "hm^2", "km^2"])

    def convert(length, unit1, unit2):
        if unit1 == "mm^2":
            if unit2 == "cm^2":
                return length / 100
            elif unit2 == "dm^2":
                return length / 10000
            elif unit2 == "m^2":
                return length / 1000000
            elif unit2 == "dam^2":
                return length / 100000000
            elif unit2 == "hm^2":
                return length / 10000000000
            elif unit2 == "km^2":
                return length / 1000000000000
            elif unit2 == "mm^2":
                return length / 1
        
        if unit1 == "cm^2":
            if unit2 == "cm^2":
                return length / 1
            elif unit2 == "dm^2":
                return length / 100
            elif unit2 == "m^2":
                return length / 10000
            elif unit2 == "dam^2":
                return length / 1000000
            elif unit2 == "hm^2":
                return length / 100000000
            elif unit2 == "km^2":
                return length / 10000000000
            
        if unit1 == "dm^2":
            if unit2 == "dm^2":
                return length / 1
            elif unit2 == "m^2":
                return length / 100
            elif unit2 == "dam^2":
                return length / 10000
            elif unit2 == "hm^2":
                return length / 1000000
            elif unit2 == "km^2":
                return length / 100000000
            
        if unit1 == "m^2":
            if unit2 == "m^2":
                return length / 1
            elif unit2 == "dam^2":
                return length / 100
            elif unit2 == "hm^2":
                return length / 10000
            elif unit2 == "km^2":
                return length / 1000000
            
        if unit1 == "dam^2":
            if unit2 == "dam^2":
                return length / 1
            elif unit2 == "hm^2":
                return length / 100
            elif unit2 == "km^2":
                return length / 10000
            
        if unit1 == "hm^2":
            if unit2 == "hm^2":
                return length / 1
            elif unit2 == "km^2":
                return length / 100
        
        if unit1 == "km^2":
            if unit2 == "km^2":
                return length / 1
            
        if unit1 == "km^2":
            if unit2 == "hm^2":
                return length * 100
            elif unit2 == "dam^2":
                return length * 10000
            elif unit2 == "m^2":
                return length * 1000000
            elif unit2 == "dm^2":
                return length * 100000000
            elif unit2 == "cm^2":
                return length * 10000000000
            elif unit2 == "mm^2":
                return length * 1000000000000
    
        if unit1 == "hm^2":
            if unit2 == "dam^2":
                return length * 100
            elif unit2 == "m^2":
                return length * 10000
            elif unit2 == "dm^2":
                return length * 1000000
            elif unit2 == "cm^2":
                return length * 100000000
            elif unit2 == "mm^2":
                return length * 10000000000
            
        if unit1 == "dam^2":
            if unit2 == "m^2":
                return length * 100
            elif unit2 == "dm^2":
                return length * 10000
            elif unit2 == "cm^2":
                return length * 1000000
            elif unit2 == "mm^2":
                return length * 100000000
            
        if unit1 == "m^2":
            if unit2 == "dm^2":
                return length * 100
            elif unit2 == "cm^2":
                return length * 10000
            elif unit2 == "mm^2":
                return length * 1000000
        
        if unit1 == "dm^2":
            if unit2 == "cm^2":
                return length * 100
            elif unit2 == "mm^2":
                return length * 10000

        if unit1 == "cm^2":
            if unit2 == "mm^2":
                return length * 100

    if st.button("Konversi"):
        result = convert(length, unit1, unit2)
        st.success(f"{length} {unit1} = {result} {unit2}")

#halaman Konversi satuan volume
if (selected == 'Konversi satuan volume') :
    st.title('Konversi satuan volume')
    length = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
    unit1 = st.selectbox("Pilih satuan awal", ["mm^3", "cm^3", "dm^3", "m^3", "dam^3", "hm^3", "km^3"])
    unit2 = st.selectbox("Pilih satuan tujuan", ["mm^3", "cm^3", "dm^3", "m^3", "dam^3", "hm^3", "km^3"])

    def convert(length, unit1, unit2):
        if unit1 == "mm^3":
            if unit2 == "cm^3":
                return length / 1000
            elif unit2 == "dm^3":
                return length / 1000000
            elif unit2 == "m^3":
                return length / 1000000000
            elif unit2 == "dam^3":
                return length / 1000000000000
            elif unit2 == "hm^3":
                return length / 1000000000000000
            elif unit2 == "km^3":
                return length / 1000000000000000000
            elif unit2 == "mm^3":
                return length / 1
        
        if unit1 == "cm^3":
            if unit2 == "cm^3":
                return length / 1
            elif unit2 == "dm^3":
                return length / 1000
            elif unit2 == "m^3":
                return length / 1000000
            elif unit2 == "dam^3":
                return length / 1000000000
            elif unit2 == "hm^3":
                return length / 1000000000000
            elif unit2 == "km^3":
                return length / 1000000000000000
            
        if unit1 == "dm^3":
            if unit2 == "dm^3":
                return length / 1
            elif unit2 == "m^3":
                return length / 1000
            elif unit2 == "dam^3":
                return length / 1000000
            elif unit2 == "hm^3":
                return length / 1000000000
            elif unit2 == "km^3":
                return length / 1000000000000
            
        if unit1 == "m^3":
            if unit2 == "m^3":
                return length / 1
            elif unit2 == "dam^3":
                return length / 1000
            elif unit2 == "hm^3":
                return length / 1000000
            elif unit2 == "km^3":
                return length / 1000000000
            
        if unit1 == "dam^3":
            if unit2 == "dam^3":
                return length / 1
            elif unit2 == "hm^3":
                return length / 1000
            elif unit2 == "km^3":
                return length / 1000000
            
        if unit1 == "hm^3":
            if unit2 == "hm^3":
                return length / 1
            elif unit2 == "km^3":
                return length / 1000
        
        if unit1 == "km^3":
            if unit2 == "km^3":
                return length / 1
            
        if unit1 == "km^3":
            if unit2 == "hm^3":
                return length * 1000
            elif unit2 == "dam^3":
                return length * 1000000
            elif unit2 == "m^3":
                return length * 1000000000
            elif unit2 == "dm^3":
                return length * 1000000000000
            elif unit2 == "cm^3":
                return length * 1000000000000000
            elif unit2 == "mm^3":
                return length * 1000000000000000000
    
        if unit1 == "hm^3":
            if unit2 == "dam^3":
                return length * 1000
            elif unit2 == "m^3":
                return length * 1000000
            elif unit2 == "dm^3":
                return length * 1000000000
            elif unit2 == "cm^3":
                return length * 1000000000000
            elif unit2 == "mm^3":
                return length * 1000000000000000
            
        if unit1 == "dam^3":
            if unit2 == "m^3":
                return length * 1000
            elif unit2 == "dm^3":
                return length * 1000000
            elif unit2 == "cm^3":
                return length * 1000000000
            elif unit2 == "mm^3":
                return length * 1000000000000
            
        if unit1 == "m^3":
            if unit2 == "dm^3":
                return length * 1000
            elif unit2 == "cm^3":
                return length * 1000000
            elif unit2 == "mm^3":
                return length * 1000000000
        
        if unit1 == "dm^3":
            if unit2 == "cm^3":
                return length * 1000
            elif unit2 == "mm^3":
                return length * 1000000

        if unit1 == "cm^3":
            if unit2 == "mm^3":
                return length * 1000

    if st.button("Konversi"):
        result = convert(length, unit1, unit2)
        st.success(f"{length} {unit1} = {result} {unit2}") 

#halaman Konversi satuan massa
if (selected == 'Konversi satuan massa') :
    st.title('konversi satuan massa')
    
    length = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
    unit1 = st.selectbox("Pilih satuan awal", ["mg", "cg", "dg", "g", "dag", "hg", "kg"])
    unit2 = st.selectbox("Pilih satuan tujuan", ["mg", "cg", "dg", "g", "dag", "hg", "kg"])

    def convert(length, unit1, unit2):
        if unit1 == "mg":
            if unit2 == "mg":
                return length / 1
            elif unit2 == "cg":
                return length / 10
            elif unit2 == "dg":
                return length / 100
            elif unit2 == "g":
                return length / 1000
            elif unit2 == "dag":
                return length / 10000
            elif unit2 == "hg":
                return length / 100000
            elif unit2 == "kg":
                return length / 1000000
        if unit1 == "cg":
            if unit2 == "dg":
                return length / 10
            elif unit2 == "g":
                return length / 100
            elif unit2 == "dag":
                return length / 1000
            elif unit2 == "hg":
                return length / 10000
            elif unit2 == "kg":
                return length / 100000
            elif unit2 == "cg":
                return length / 1
        if unit1 == "dg":
            if unit2 == "g":
                return length / 10
            elif unit2 == "dag":
                return length / 100
            elif unit2 == "hg":
                return length / 1000
            elif unit2 == "kg":
                return length / 10000
            elif unit2 == "dg":
                return length / 1
        if unit1 == "g":
            if unit2 == "dag":
                return length / 10
            elif unit2 == "hg":
                return length / 100
            elif unit2 == "kg":
                return length / 1000
            elif unit2 == "g":
                return length / 1
        if unit1 == "dag":
            if unit2 == "hg":
                return length / 10
            elif unit2 == "kg":
                return length / 100
            elif unit2 == "dag":
                return length / 1
        if unit1 == "hg":
            if unit2 == "kg":
                return length / 10
            elif unit2 == "hg":
                return length / 1
        if unit1 == "kg":
            if unit2 == "hg":
                return length * 10
            elif unit2 == "dag":
                return length * 100
            elif unit2 == "g":
                return length * 1000
            elif unit2 == "dg":
                return length * 10000
            elif unit2 == "cg":
                return length * 100000
            elif unit2 == "mg":
                return length * 1000000
            elif unit2 == "kg":
                return length * 1
        if unit1 == "hg":
            if unit2 == "dag":
                return length * 10
            elif unit2 == "g":
                return length * 100
            elif unit2 == "dg":
                return length * 1000
            elif unit2 == "cg":
                return length * 10000
            elif unit2 == "mg":
                return length * 100000
            elif unit2 == "hg":
                return length * 1
        if unit1 == "dag":
            if unit2 == "dag":
                return length * 1
            elif unit2 == "g":
                return length * 10
            elif unit2 == "dg":
                return length * 100
            elif unit2 == "cg":
                return length * 1000
            elif unit2 == "mg":
                return length * 10000
        if unit1 == "g":
            if unit2 == "g":
                return length * 1
            elif unit2 == "dg":
                return length * 10
            elif unit2 == "cg":
                return length * 100
            elif unit2 == "mg":
                return length * 1000
        if unit1 == "dg":
            if unit2 == "dg":
                return length * 1
            elif unit2 == "cg":
                return length * 10
            elif unit2 == "mg":
                return length * 100
        if unit1 == "cg":
            if unit2 == "cg":
                return length * 1
            elif unit2 == "mg":
                return length * 10
        if unit1 == "mg":
            if unit2 == "mg":
                return length * 1
            
    if st.button("Konversi"):
        result = convert(length, unit1, unit2)
        st.success(f"{length} {unit1} = {result} {unit2}")
        st.text('satuan metrik (SI) : mg, cg, dg, g, dag, hg, kg.')

#Halaman konversi suhu
if (selected == 'Konversi satuan suhu') :
    st.title('Konversi satuan suhu')
    suhu = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
    unit1 = st.selectbox("Pilih satuan suhu", ["C", "F", "K", "Re"])
    unit2 = st.selectbox("Pilih satuan suhu tujuan", ["F", "C", "K", "Re"])    
    
    def convert(suhu, unit1, unit2):
        if unit1 == "C":
            if unit2 == "C":
                return suhu
            if unit2 == "F":
                return ((9 / 5) * suhu) + 32
            if unit2 == "K":
                return suhu + 273.15
            if unit2 == "Re":
                return (4 / 5) * suhu

        if unit1 == "F":
            if unit2 == "F":
                return suhu
            if unit2 == "C":
                return (5 / 9) * (suhu - 32)
            if unit2 == "K":
                return (5 / 9 * (suhu - 32)) + 273.15
            if unit2 == "Re":
                return (4 / 9) * (suhu - 32)
        
        if unit1 == "K":
            if unit2 == "K":
                return suhu
            if unit2 == "C":
                return suhu - 273.15
            if unit2 == "F":
                return ((9 / 5) * (suhu - 273.15)) + 32
            if unit2 == "Re":
                return (4 / 5) * (suhu - 273.15)

        if unit1 == "Re":
            if unit2 == "Re":
                return suhu
            if unit2 == "C":
                return (5 / 4) * suhu
            if unit2 == "F":
                return ((9 / 4) * (suhu)) + 32
            if unit2 == "K":
                return ((5 / 4) * suhu) + 273.15

    if st.button("Konversi"):
        result = convert(suhu, unit1, unit2)
        st.success(f"{suhu} {unit1} = {result} {unit2}")
    st.text('Keterangan :')
    st.text('Celsius    = C')
    st.text('Fahrenheit = F') 
    st.text('Kelvin     = K')
    st.text('Reaumure   = Re')   

#Halaman konversi mutu beton
if (selected == 'Konversi mutu beton') :
    st.title('Konversi mutu beton')
    length = st.number_input("Masukkan nilai yang akan dikonversi", min_value=0.0)
    unit1 = st.selectbox("Pilih satuan kuat tekan beton", ["MPa", "Kg/cm^2"])
    unit2 = st.selectbox("Pilih satuan kuat tekan beton tujuan", ["Kg/cm^2", "MPa"])    

    def convert(length, unit1, unit2):
        if unit1 == "MPa":
            if unit2 == "Kg/cm^2":
                return length * 10.1972 / 0.83
            if unit2 == "MPa":
                return length
        if unit1 == "Kg/cm^2":
            if unit2 == "MPa":
                return length * 0.098067 * 0.83
            if unit2 == "Kg/cm^2":
                return length
                
    if st.button("Konversi"):
        result = convert(length, unit1, unit2)
        st.success(f"{length} {unit1} = {result} {unit2}") 
        st.text('Keterangan :')
        st.text('# Satuan (MPa) benda uji selinder diameter 15 cm tinggi 30 cm')
        st.text('# Satuan (K) benda uji kubus 15 cm x 15 cm x 15 cm')
        st.text('# 1 Mega pascal (MPa) = 10.1972 Kg/cm^2')
        st.text('# K = Kg/mm^2')
        



       