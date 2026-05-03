import streamlit as st
from transformers import pipeline
from PIL import Image
import torch

# ================= LOAD MODELS =================
@st.cache_resource
def load_models():
    import torch  # important for streamlit cache
    return {
        "sentiment": pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        ),
        "generator": pipeline(
            "text-generation",
            model="gpt2"
        ),
        "image": pipeline(
            "image-classification",
            model="google/vit-base-patch16-224"
        ),
        "emotion": pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=None
        )
    }

models = load_models()

# ================= UI =================
st.set_page_config(page_title="AI Multi App", layout="centered")

st.title("🤖 AI Multi-Task App")
st.write("Perform Sentiment Analysis, Text Generation, Image Classification & Emotion Detection")

task = st.sidebar.selectbox(
    "Choose Task",
    ["Sentiment Analysis", "Text Generation", "Image Classification", "Emotion Detection"]
)

# ================= SENTIMENT =================
if task == "Sentiment Analysis":
    text = st.text_area("Enter text:")

    if st.button("Analyze Sentiment"):
        result = models["sentiment"](text)[0]
        st.success(f"Sentiment: {result['label']}")
        st.write(f"Confidence: {result['score']:.4f}")

# ================= TEXT GENERATION =================
elif task == "Text Generation":
    prompt = st.text_area("Enter prompt:")

    if st.button("Generate Text"):
        result = models["generator"](prompt, max_length=50)[0]
        st.write(result["generated_text"])

# ================= IMAGE CLASSIFICATION =================
elif task == "Image Classification":
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image")

        if st.button("Classify Image"):
            result = models["image"](image)
            st.success(f"Prediction: {result[0]['label']}")

# ================= EMOTION DETECTION =================
elif task == "Emotion Detection":
    text = st.text_area("Enter text:")

    if st.button("Analyze Emotion"):
        results = models["emotion"](text)

        if isinstance(results[0], list):
            results = results[0]

        results = sorted(results, key=lambda x: x["score"], reverse=True)

        top = results[0]
        st.success(f"Top Emotion: {top['label']} ({round(top['score']*100,2)}%)")

        st.subheader("Detailed Breakdown")

        for r in results:
            st.write(f"{r['label']} ({round(r['score']*100,2)}%)")
            st.progress(float(r["score"]))