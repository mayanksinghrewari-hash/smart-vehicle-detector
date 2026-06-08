import streamlit as st
from inference_sdk import InferenceHTTPClient
import tempfile

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
    margin-bottom:25px;
}

.footer {
    text-align:center;
    color:gray;
    padding:20px;
}
</style>

""", unsafe_allow_html=True)

page = st.sidebar.radio(
"Navigation",
["🏠 Home", "🚗 Detection", "📊 Analytics", "ℹ️ About"]
)

if page == "🏠 Home":

```
st.markdown("""
<div class="hero">
<h1>🚗 Smart Vehicle Damage Detection System</h1>
<h3>AI Powered Accident Assessment Platform</h3>
<p>Detect dents, scratches and vehicle damage using Artificial Intelligence.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", "84.5%")

with col2:
    st.metric("Dataset Images", "6957")

with col3:
    st.metric("Damage Classes", "10+")

st.markdown("## Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🔍 AI Damage Detection")

with c2:
    st.info("📈 Severity Analysis")

with c3:
    st.warning("💰 Repair Cost Estimation")
```

elif page == "🚗 Detection":

```
st.title("🚗 Vehicle Damage Detection")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Vehicle",
        use_container_width=True
    )

    if st.button("🔍 Analyze Damage"):

        try:

            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                tmp.write(uploaded_file.read())
                image_path = tmp.name

            CLIENT = InferenceHTTPClient(
                api_url="https://serverless.roboflow.com",
                api_key=st.secrets["ROBOFLOW_API_KEY"]
            )

            result = CLIENT.infer(
                image_path,
                model_id="automobile-damage-detection/1"
            )

            st.success("Analysis Complete")

            st.subheader("AI Prediction")
            st.json(result)

        except Exception as e:
            st.error(f"Error: {e}")
```

elif page == "📊 Analytics":

```
st.title("📊 Analytics Dashboard")

st.bar_chart({
    "Dent": [40],
    "Scratch": [30],
    "Bumper": [20],
    "Glass": [10]
})
```

elif page == "ℹ️ About":

```
st.title("ℹ️ About Project")

st.write("""
Smart Vehicle Damage Detection System uses AI
to identify vehicle damage from images.

Technologies Used:
• Python
• Streamlit
• Roboflow
• Computer Vision
• CNN / Object Detection

Objective:
To automate vehicle damage assessment and
estimate repair costs.
""")

st.subheader("Project Team")

st.write("• Mayank Yadav")
st.write("• Koustuv Singh")
st.write("• Avi Kumar")
st.write("• Gaurav Sharma")
```

st.markdown("---")

st.markdown(
"<div class='footer'>Developed for IDT Project | Smart Vehicle Damage Detection System</div>",
unsafe_allow_html=True
)
