import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖",
    layout="centered"
)

# Application title
st.title("🤖 AI Text Generator")
st.write("Generate text using the GPT-Neo 125M language model.")

# Load the model only once
@st.cache_resource
def load_model():
    generator = pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )
    return generator

# Load model
with st.spinner("Loading AI model..."):
    generator = load_model()

# User input
prompt = st.text_area(
    "✍️ Enter your text prompt:",
    placeholder="Example: Artificial Intelligence is",
    height=150
)

# Generate button
if st.button("🚀 Generate Text"):
    if prompt.strip() == "":
        st.warning("Please enter a text prompt.")
    else:
        with st.spinner("Generating text..."):
            result = generator(
                prompt,
                max_length=100,
                num_return_sequences=1,
                do_sample=True
            )

        generated_text = result[0]["generated_text"]

        st.subheader("📝 Generated Text")
        st.write(generated_text)

# Footer
st.markdown("---")
st.caption("Powered by GPT-Neo 125M | Hugging Face Transformers | Streamlit")
