import streamlit as st
from diffusers import StableDiffusionXLPipeline
import torch

# Load base model with LoRA
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
)
pipe.unet.load_attn_procs("lora-weights")
pipe.to("cuda")

# Streamlit UI
st.title("SDXL-LoRA Image Generator")
prompt = st.text_input("Enter prompt:", "A futuristic cityscape at dusk")
scale = st.slider("LoRA scale", 0.0, 1.0, 0.8)

if st.button("Generate"):
    with st.spinner("Generating..."):
        image = pipe(
            prompt, 
            num_inference_steps=25,
            cross_attention_kwargs={"scale": scale}
        ).images[0]
    st.image(image)
