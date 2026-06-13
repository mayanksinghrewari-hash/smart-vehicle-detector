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
st.write("AI-Based Vehicle Dent & Scratch Detection using Roboflow")

uploaded_file = st.file_uploader(
    "Upload Vehicle Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:

        if image.mode != "RGB":
            image = image.convert("RGB")

        image.save(temp.name, format="JPEG")

        api_key = st.secrets["ROBOFLOW_API_KEY"]

        url = f"https://detect.roboflow.com/car_dent_scratch_detection-1/9?api_key={api_key}"

        with open(temp.name, "rb") as img_file:

            response = requests.post(
                url,
                files={"file": img_file}
            )

        result = response.json()

        st.subheader("Detection Results")

        st.json(result)

        predictions = result.get("predictions", [])

        if predictions:

            st.success(f"Detected {len(predictions)} damage area(s)")

            for pred in predictions:

                st.write(
                    f"Damage Type: {pred['class']} | "
                    f"Confidence: {round(pred['confidence'] * 100, 2)}%"
                )

        else:

            st.warning("No damage detected.")
