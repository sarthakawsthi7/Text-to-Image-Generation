# import tkinter as tk
# import customtkinter as ctk
# from PIL import Image, ImageTk
# import torch
# from diffusers import StableDiffusionXLPipeline
# import os
# model_path = r"C:\Users\hp\Desktop\StableDiffusionApp-main\StableDiffusionApp-main\realvisxlV50_v50LightningBakedvae.safetensors"

# if not os.path.exists(model_path):
#     raise FileNotFoundError(f"Model file not found: {model_path}")
# device = "cuda" if torch.cuda.is_available() else "cpu"
# torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
# pipe = StableDiffusionXLPipeline.from_single_file(model_path, torch_dtype=torch_dtype)
# pipe.to(device)
# app = tk.Tk()
# app.geometry("532x632")
# app.title("Stable Bud")
# ctk.set_appearance_mode("dark")
# prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
# prompt.place(x=10, y=10)
# lmain = ctk.CTkLabel(app, height=512, width=512)
# lmain.place(x=10, y=110)

# def generate():
#     """Generate an image from the entered prompt."""
#     with torch.no_grad():
#         image = pipe(prompt.get(), guidance_scale=8.5).images[0]

#     image.save("generatedimage.png")
#     img = Image.open("generatedimage.png").resize((512, 512), Image.Resampling.LANCZOS)
#     img_tk = ImageTk.PhotoImage(img)

#     lmain.configure(image=img_tk)
#     lmain.image = img_tk

# trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=generate)
# trigger.configure(text="Generate")
# trigger.place(x=206, y=60)

# app.mainloop()


import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import torch
from diffusers import StableDiffusionXLPipeline
import os

# Model Path
model_path = r"C:\Users\hp\Desktop\StableDiffusionApp-main\StableDiffusionApp-main\realvisxlV50_v50LightningBakedvae.safetensors"

# Ensure model exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

# Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# Load model once
pipe = StableDiffusionXLPipeline.from_single_file(model_path, torch_dtype=torch_dtype).to(device)

# Tkinter App Setup
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

# Input Box
prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

# Output Image Box
lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

def generate():
    """Generate an image from the entered prompt."""
    text_prompt = prompt.get().strip()

    if not text_prompt:
        return  # Ignore empty prompts

    try:
        with torch.no_grad():
            image = pipe(text_prompt, guidance_scale=8.5).images[0]

        # Save generated image to a different file
        output_path = "generated_tkinter.png"
        image.save(output_path)

        # Load and display image
        img = Image.open(output_path).resize((512, 512), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        lmain.configure(image=img_tk)
        lmain.image = img_tk
    except Exception as e:
        print(f"Error: {e}")

# Generate Button
trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=generate)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)

app.mainloop()

