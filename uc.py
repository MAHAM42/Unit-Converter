import streamlit as st

# 🎨 Streamlit Page Config
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for Purple Theme
st.markdown("""
    <style>
        /* Change text color of title */
        h1 {
            color: #800080 !important;
        }

        /* Change radio buttons color */
        div[role="radiogroup"] label {
            color: #800080 !important;
            font-weight: bold;
        }

        /* Change sidebar title color */
        .sidebar .sidebar-content {
            color: #800080 !important;
        }

        /* Convert Button */
        div.stButton > button {
            background-color: #800080 !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
        }

        /* Selectbox dropdown */
        div[data-baseweb="select"] > div {
            background-color: #800080 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 5px !important;
        }

        /* Number Input Field */
        input[type="number"] {
            background-color: #f3e5f5 !important; /* Light Purple Background */
            border: 2px solid #800080 !important;
            color: #800080 !important;
            font-weight: bold !important;
            border-radius: 5px !important;
            padding: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🚀 App Title
st.markdown("<h1 style='text-align: center;'>🔥 Universal Unit Converter 🚀</h1>", unsafe_allow_html=True)
st.write("---")

# 📌 Function for Length Conversion
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        'Meters (M)': 1, 'Kilometers (KM)': 0.001, 'Centimeters (CM)': 100, 'Millimeters (MM)': 1000,
        'Miles (MI)': 0.000621371, 'Yards (YD)': 1.09361, 'Feet (FT)': 3.28084, 'Inches (IN)': 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# 📌 Function for Weight Conversion
def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        'Kilograms (KG)': 1, 'Grams (G)': 1000, 'Pounds (LB)': 2.20462, 'Ounces (OZ)': 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# 📌 Function for Temperature Conversion
def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius (C)' and to_unit == 'Fahrenheit (F)':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit (F)' and to_unit == 'Celsius (C)':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius (C)' and to_unit == 'Kelvin (K)':
        return value + 273.15
    elif from_unit == 'Kelvin (K)' and to_unit == 'Celsius (C)':
        return value - 273.15
    return value

# 🏆 Sidebar for Conversion Selection
st.sidebar.header("⚙️ Conversion Options")
conversion_type = st.sidebar.radio("Choose Conversion Type:", ["Length 📏", "Weight ⚖️", "Temperature 🌡️"])

# 📌 User Input Value
value = st.number_input("🔢 Enter Value:", min_value=0.0, step=0.1)

# 📌 Define Units Based on Selection
if conversion_type == "Length 📏":
    units = ['Meters (M)', 'Kilometers (KM)', 'Centimeters (CM)', 'Millimeters (MM)',
             'Miles (MI)', 'Yards (YD)', 'Feet (FT)', 'Inches (IN)']
elif conversion_type == "Weight ⚖️":
    units = ['Kilograms (KG)', 'Grams (G)', 'Pounds (LB)', 'Ounces (OZ)']
else:
    units = ['Celsius (C)', 'Fahrenheit (F)', 'Kelvin (K)']

# 🔄 From & To Unit Selection
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("🔄 Convert From:", units)
with col2:
    to_unit = st.selectbox("➡️ Convert To:", units)

# 🎯 Convert Button
if st.button("🚀 Convert Now"):
    if conversion_type == "Length 📏":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight ⚖️":
        result = weight_converter(value, from_unit, to_unit)
    else:
        result = temperature_converter(value, from_unit, to_unit)
    
    # ✅ Stylish Result Display
    st.markdown(f"""
        <div style="
            background-color: #800080; 
            color: white; 
            padding: 15px; 
            border-radius: 10px; 
            text-align: center; 
            font-size: 18px;">
            🎯 {value} {from_unit} = <b>{round(result, 4)} {to_unit}</b>
        </div>
    """, unsafe_allow_html=True)

# 🌟 Footer
st.write("---")
st.markdown("<p style='text-align: center; color: #800080;'>Created with ❤️ by <b>Maham Shahid</b></p>", unsafe_allow_html=True)
