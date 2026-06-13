import streamlit as st
from inference_sdk import InferenceHTTPClient
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Smart Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide"
)

# Roboflow Client
CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=st.secrets["ROBOFLOW_API_KEY"]
)

# Header
st.markdown("""
# 🚗 Smart Vehicle Damage Detection System

### CNN-Based Vehicle Damage Analysis

Upload a vehicle image and detect damages using a trained Computer Vision model.
""")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, caption="Uploaded Vehicle", use_container_width=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)

        result = CLIENT.infer(
            temp_file.name,
            model_id="vehicle-damage-detection-hhxfj/1"
        )

    with col2:

        st.subheader("Detection Results")

        predictions = result.get("predictions", [])

        if len(predictions) == 0:
            st.warning("No damage detected.")
        else:

            st.success(f"{len(predictions)} damage region(s) detected")

            for pred in predictions:

                damage_type = pred.get("class", "Damage")
                confidence = pred.get("confidence", 0)

                st.write(f"**Damage Type:** {damage_type}")
                st.write(f"**Confidence:** {confidence*100:.2f}%")

                if confidence > 0.8:
                    cost = "₹15,000 - ₹30,000"
                elif confidence > 0.5:
                    cost = "₹8,000 - ₹15,000"
                else:
                    cost = "₹3,000 - ₹8,000"

                st.write(f"**Estimated Repair Cost:** {cost}")
                st.divider()

st.divider()

st.markdown("""
### 📊 Project Information

- Model: CNN-based Roboflow Vision Model
- Framework: Streamlit
- Damage Detection: Computer Vision
- Cost Estimation: Rule-based Analysis

Developed for Academic Project Demonstration.
""")
