from io import BytesIO
from google import genai
from google.genai import types
from PIL import Image
import streamlit as st

# Page layout configuration
st.set_page_config(
    page_title="AI Baddie Doll Generator", page_icon="🏗️", layout="centered"
)

st.title("🏗️ Y2K Baddie Doll Generator")
st.write(
    "Generate stylized fashion dolls in construction settings with toy blasters"
    " using the Google GenAI SDK."
)

# Securely grab the API key from Streamlit's secrets manager
if "GEMINI_API_KEY" in st.secrets:
  api_key = st.secrets["GEMINI_API_KEY"]
else:
  api_key = st.text_input("Enter your Google AI API Key:", type="password")

# Preset prompt optimized to fit safety guidelines while capturing the look
default_prompt = (
    "A stylized 3D render of a Y2K fashion doll with a baddie aesthetic, "
    "heavy glam makeup, trendy streetwear, and metal braces on her teeth. "
    "She is standing on an active construction site background with steel beams "
    "and scaffolding, holding a brightly colored neon toy foam dart blaster. "
    "High quality digital art, vibrant lighting."
)

prompt = st.text_area("Image Prompt:", value=default_prompt, height=120)

if st.button("Generate Baddie Image", type="primary"):
  if not api_key:
    st.error("Please enter your Google AI API Key to proceed.")
  else:
    try:
      with st.spinner(
          "Connecting to Google's remote brain... Painting pixels..."
      ):
        # Initialize the Google GenAI client
        client = genai.Client(api_key=api_key)

        # Request image generation using the correct multimodal flash image model
        response = client.models.generate_content(
            model="gemini-3.1-flash-image",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )

        image_found = False
        for part in response.parts:
          if part.inline_data:
            image_found = True
            image_bytes = part.inline_data.data
            image = Image.open(BytesIO(image_bytes))

            st.success("Generation complete!")
            st.image(
                image, caption="Y2K Construction Baddie", use_container_width=True
            )

        if not image_found:
          st.warning(
              "The model responded, but no image data was returned. Try"
              " tweaking your prompt text."
          )

    except Exception as e:
      st.error(f"An error occurred: {e}")
