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
st.write("Upload a vehicle image and detect damage using Roboflow")

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

    if image.mode != "RGB":
        image = image.convert("RGB")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:

        image.save(temp.name, format="JPEG")

        api_key = st.secrets["ROBOFLOW_API_KEY"]

        url = f"https://detect.roboflow.com/car-damage-detection-t0g92/3?api_key={api_key}"

        with open(temp.name, "rb") as img_file:

            response = requests.post(
                url,
                files={"file": img_file}
            )

        result = response.json()

        st.subheader("Detection Results")
        st.json(result)

        predictions = result.get("predictions", [])

        if len(predictions) > 0:

            st.success(
                f"Damage Detected! Found {len(predictions)} damage area(s)."
            )

            for pred in predictions:

                st.write(
                    f"Class: {pred.get('class')} | Confidence: {round(pred.get('confidence',0)*100,2)}%"
                )

        else:
            st.warning("No damage detected.")
