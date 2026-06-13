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

    repair_costs = {
        "Scratch": 2500,
        "Dent": 6000,
        "Crack": 10000,
        "Bumper": 8000,
        "Light": 4500,
        "Door": 12000,
        "Fender": 7000
    }

    total_cost = 0

    for pred in predictions:

        damage_class = pred.get("class")
        confidence = pred.get("confidence", 0)

        st.write(
            f"Class: {damage_class} | Confidence: {confidence*100:.2f}%"
        )

        if damage_class in repair_costs:
            total_cost += repair_costs[damage_class]

    if total_cost < 5000:
        severity = "Minor Damage"
    elif total_cost < 15000:
        severity = "Moderate Damage"
    else:
        severity = "Severe Damage"

    st.info(f"Damage Severity: {severity}")
    st.success(f"Estimated Repair Cost: ₹{total_cost:,}")

else:
    st.warning("No damage detected.")
