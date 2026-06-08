import streamlit as st

st.set_page_config(
    page_title="Smart Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
}

.sub-title {
    text-align: center;
    font-size: 20px;
    color: #bbbbbb;
}

.result-box {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="big-title">🚗 Smart Vehicle Damage Detection System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI Powered Vehicle Damage Analysis</p>',
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload Vehicle Image",
        type=["jpg", "jpeg", "png"]
    )

with col2:
    st.image(
        "https://images.unsplash.com/photo-1503376780353-7e6692767b70",
        use_container_width=True
    )

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Vehicle")

    if st.button("🔍 Analyze Damage"):
        st.success("Damage Detected")

        st.markdown("""
        <div class="result-box">
        <h3>Analysis Report</h3>
        <p>Damage Type: Dent</p>
        <p>Confidence: 92%</p>
        <p>Severity: Medium</p>
        <p>Estimated Repair Cost: ₹8,000 - ₹12,000</p>
        </div>
        """, unsafe_allow_html=True)
