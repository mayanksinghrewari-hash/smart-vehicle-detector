import streamlit as st
import requests
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Smart Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Smart Vehicle Damage Detection")
st.write("CNN-Based Vehicle Damage Analysis using Roboflow")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

   with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:

    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(temp.name, format="JPEG")

        api_key = st.secrets["ROBOFLOW_API_KEY"]

        url = f"https://detect.roboflow.com/vehicle-damage-detection-hhxfj/1?api_key={api_key}"

        with open(temp.name, "rb") as img_file:
            response = requests.post(
                url,
                files={"file": img_file}
            )

        result = response.json()

    st.subheader("Detection Results")

    predictions = result.get("predictions", [])

    if len(predictions) == 0:
        st.warning("No damage detected")
    else:
        st.success(f"{len(predictions)} damage area(s) detected")

        for pred in predictions:

            damage_type = pred.get("class", "Damage")
            confidence = pred.get("confidence", 0)

            st.write(f"### {damage_type}")
            st.write(f"Confidence: {confidence*100:.2f}%")

            if confidence > 0.8:
                st.write("Estimated Repair Cost: ₹15,000 - ₹30,000")
            elif confidence > 0.5:
                st.write("Estimated Repair Cost: ₹8,000 - ₹15,000")
            else:
                st.write("Estimated Repair Cost: ₹3,000 - ₹8,000")

            st.divider()

st.markdown("---")
st.markdown("""
### Project Information

- CNN Model: Roboflow Vehicle Damage Detection
- Framework: Streamlit
- Technology: Computer Vision
- Damage Detection: Deep Learning
""")
