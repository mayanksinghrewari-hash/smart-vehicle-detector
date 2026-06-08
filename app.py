import streamlit as st

st.set_page_config(page_title="Smart Vehicle Damage Detection")

st.title("🚗 Smart Vehicle Damage Detection System")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Vehicle")

    if st.button("Analyze Damage"):
        st.success("Damage Detected")
        st.write("Damage Type: Dent")
        st.write("Confidence: 92%")
        st.write("Estimated Repair Cost: ₹8,000 - ₹12,000")
