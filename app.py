import streamlit as st
import requests
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Vehicle Damage Detection",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Vehicle Damage Detection System")
st.write("CNN-Based Vehicle Damage Analysis using Roboflow")

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

        url = f"https://detect.roboflow.com/damage-vehicle/3?api_key={api_key}"

        with open(temp.name, "rb") as img_file:
            response = requests.post(
                url,
                files={"file": img_file}
            )

        result = response.json()

    st.subheader("Detection Results")

    if "predictions" in result:

        predictions = result["predictions"]

        if len(predictions) == 0:
            st.warning("No damage detected.")

        else:
            st.success(f"Detected {len(predictions)} damage area(s)")

            for pred in predictions:

                st.write(
                    f"""
                    Damage Type: {pred.get('class','Unknown')}
                    
                    Confidence: {round(pred.get('confidence',0)*100,2)}%
                    """
                )

    else:
        st.error("Unable to get prediction from model.")
