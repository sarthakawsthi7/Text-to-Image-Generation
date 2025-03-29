### **Text-to-Image Generation with Stable Diffusion**



**Project Overview**


This project enables Text-to-Image Generation using Stable Diffusion with ComfyUI and LoRA Checkpoints, integrated seamlessly with a Flask-based API. It allows users to generate high-quality AI-generated images based on text prompts.
___________ _______________________ _______________________________ __________________________________________________________ _ _ _ _ _ _ _ 
**✨ Features**

🖼 Stable Diffusion for high-quality image synthesis

🎨 ComfyUI Integration for advanced workflow customization

🔗 LoRA Checkpoints support for fine-tuned models

🌐 Flask API for seamless web-based interaction

📸 Sample Image Previews for generated outputs

📷 Sample Images

**Below are some AI-generated images using the project:**

![WhatsApp Image 2025-03-30 at 02 54 53_e5b8c023](https://github.com/user-attachments/assets/172e7179-2e83-49a6-becb-e76c541378f5)

**ComfyUI workflows integrated with Flask**


![unnamed](https://github.com/user-attachments/assets/67ee4380-d10b-4039-b593-366a2466fa32)
![unnamed](https://github.com/user-attachments/assets/5c50eef0-710d-4790-96b0-493fdfbc9bb6)
![unnamed](https://github.com/user-attachments/assets/1e70959d-0947-4df2-8234-6cf7c54d34af)

**🔧 Installation & Setup**

1️⃣ Clone the Repository
git clone https://github.com/yourusername/text-to-image-flask.git
cd text-to-image-flask

2️⃣ Install Dependencies
pip install -r requirements.txt

Ensure you have Python installed, then run:

pip install -r requirements.txt

3️⃣ Download Stable Diffusion Checkpoints & LoRAs

Place Stable Diffusion model files in models/Stable-diffusion/

Place LoRA Checkpoints in models/Lora/

4️⃣ Run the Flask Server

python app.py

The server will be available at http://127.0.0.1:5000/

**📡 API Usage**

Endpoint: Generate Image

URL: POST /generate

Request Example:

{
  "prompt": "A futuristic city at night, cyberpunk style",
  "steps": 50,
  "guidance_scale": 7.5
}

Response Example:

{
  "image_url": "/static/generated/image_12345.png"
}

**🛠 Technologies Used**

Stable Diffusion - AI Image Generation Model

ComfyUI - Visual workflow for Stable Diffusion

LoRA - Lightweight model finetuning

Flask - Python web framework

Python - Backend scripting

**🎯 Future Enhancements**

🔹 Implement Web UI for real-time image generation

🔹 Support for different AI models (SDXL, SD 2.1, etc.)

🔹 Cloud deployment for wider accessibility
