import os
import streamlit as st
from converter import length_converter, weight_converter, temperature_converter

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")  # ✅ Full-Width Layout

# ✅ Dynamic Path for Images
base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "converter")  # Images folder ka sahi path

# Custom CSS Styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #ff9966, #ff5e62,#ADFF2F);
            color: blue;
            padding: 0px;
            margin: 0px;
            overflow-x: hidden;
        }
        .header-image {
            width: 100%;
            height: 350px; /* ✅ Header image ka size bara kar diya */
            object-fit: cover;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            border-radius: 5px;
            font-size: 16px;
        }
        .stTextInput>div>div>input {
            border-radius: 5px;
            padding: 10px;
        }
        .content {
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
           /* ✅ Stylish Gradient Heading */
        .styled-heading {
            text-align: center;
            font-size: 100px; /* ✅ Size bara */
            font-weight: bold;
            font-family: 'Poppins', sans-serif; /* ✅ Stylish Font */
            background: -webkit-linear-gradient(left, yellow, green);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
            
    </style>
""", unsafe_allow_html=True)

# ✅ Stylish Heading with Gradient
st.markdown("<h1 class='styled-heading'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

# ✅ Full-Width Header Image
st.image(os.path.join(image_path, "header.jpg"), use_container_width=True, output_format="JPEG")

category = st.sidebar.selectbox("Choose Category", ["Length", "Weight", "Temperature"])

st.markdown("<div class='content'>", unsafe_allow_html=True)  # ✅ Start content wrapper

if category == "Length":
    st.image(os.path.join(image_path, "length.png"), width=80)
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", ["meter", "kilometer", "centimeter", "mile", "yard", "foot"])
    to_unit = st.selectbox("To", ["meter", "kilometer", "centimeter", "mile", "yard", "foot"])
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    st.image(os.path.join(image_path, "weight.png"), width=80)
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", ["kilogram", "gram", "pound", "ounce"])
    to_unit = st.selectbox("To", ["kilogram", "gram", "pound", "ounce"])
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    st.image(os.path.join(image_path, "tem.png"), width=80)
    value = st.number_input("Enter Value:", format="%.2f")
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

st.markdown("</div>", unsafe_allow_html=True)  # ✅ End content wrapper



# ✅ Stylish Footer Code (Insert Here)
st.markdown("""
    <style>
  .footer-text {
    text-align: center;
    font-size: 60px !important; /* ✅ Force Large Size */
    font-weight: bold;
    font-family: 'Lobster', cursive; /* ✅ Stylish Font */
    background: -webkit-linear-gradient(left, #ADFF2F, #008000); /* ✅ Purple to Orange Gradient */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-top: 50px;
    padding: 20px;
}


    </style>
""", unsafe_allow_html=True)

# ✅ Stylish Footer
st.markdown("<p class='footer-text'>Made by Zunair shah</p>", unsafe_allow_html=True)