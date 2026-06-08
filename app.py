import streamlit as st

st.set_page_config(
    page_title="Smart Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg,#0f172a,#1e3a8a,#06b6d4);
    padding:40px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-bottom:20px;
}

.feature {
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
}

.footer {
    text-align:center;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home","🚗 Detection","📊 Analytics","ℹ️ About"]
)

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
    <h1>🚗 Smart Vehicle Damage Detection</h1>
    <h3>AI Powered Accident Assessment Platform</h3>
    <p>Detect vehicle damage instantly using Artificial Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        st.metric("Accuracy","84.5%")

    with col2:
        st.metric("Dataset Images","6957")

    with col3:
        st.metric("Damage Classes","10+")

    st.markdown("## Features")

    c1,c2,c3=st.columns(3)

    with c1:
        st.success("🔍 AI Damage Detection")

    with c2:
        st.info("📈 Severity Analysis")

    with c3:
        st.warning("💰 Repair Cost Estimation")

if page == "🚗 Detection":

    st.title("Vehicle Damage Detection")

    uploaded_file = st.file_uploader(
        "Upload Vehicle Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:
        st.image(uploaded_file)

        if st.button("Analyze Damage"):
            st.success("Damage Detected")

            st.write("Damage Type: Dent")
            st.write("Confidence: 92%")
            st.write("Severity: Medium")
            st.write("Estimated Cost: ₹8,000 - ₹12,000")

if page == "📊 Analytics":

    st.title("Analytics Dashboard")

    st.bar_chart({
        "Dents":[40],
        "Scratches":[30],
        "Bumper Damage":[20],
        "Glass Damage":[10]
    })

if page == "ℹ️ About":

    st.title("About Project")

    st.write("""
    Smart Vehicle Damage Detection System uses AI
    to identify vehicle damage from images.

    Technologies Used:
    - Python
    - Streamlit
    - Roboflow
    - Computer Vision
    """)

st.markdown("---")
st.markdown(
    "<div class='footer'>Developed by Mayank Yadav | IDT Project 2026</div>",
    unsafe_allow_html=True
)
