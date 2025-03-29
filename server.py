from flask import Flask, render_template, request, send_file
import torch
from diffusers import StableDiffusionXLPipeline
import os

app = Flask(__name__)

model_path = r"C:\Users\hp\Desktop\StableDiffusionApp-main\StableDiffusionApp-main\realvisxlV50_v50LightningBakedvae.safetensors"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

device = "cuda" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

pipe = StableDiffusionXLPipeline.from_single_file(model_path, torch_dtype=torch_dtype).to(device)

os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()

        if prompt:
            try:
                with torch.no_grad():
                    image = pipe(prompt, guidance_scale=8.5).images[0]

                image_path = "static/generated_flask.png"
                image.save(image_path)

                return render_template("index.html", image_path=image_path)
            except Exception as e:
                return f"Error: {e}", 500

    return render_template("index.html", image_path=None)

@app.route("/download")
def download():
    return send_file("static/generated_flask.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
