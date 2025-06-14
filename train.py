from diffusers import StableDiffusionXLPipeline
from peft import LoraConfig
import torch

# 1. Load base model
model = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", 
    torch_dtype=torch.float16
).to("cuda")

# 2. Configure LoRA
lora_config = LoraConfig(
    r=32,
    lora_alpha=64,
    target_modules=["to_k", "to_q", "to_v", "to_out.0"],
    lora_dropout=0.1,
    bias="none"
)

# 3. Add LoRA adapters
model.unet.add_adapter(lora_config)

# 4. Training loop (simplified)
def train(dataset, epochs=10, lr=1e-4):
    optimizer = torch.optim.AdamW(model.unet.parameters(), lr=lr)
    
    for epoch in range(epochs):
        for batch in dataset:
            images, texts = batch
            loss = model(images, texts).loss
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

# 5. Save LoRA weights
model.unet.save_pretrained("lora-weights")
