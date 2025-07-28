import torch
from diffusers import StableDiffusionPipeline
import gradio as gr
import random

device = "cuda" if torch.cuda.is_available() else "cpu"


model_id = "CompVis/stable-diffusion-v1-4"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float32 if device == "cpu" else torch.float16,
    safety_checker=None
).to(device)

styles = {
    "Default": "",
    "Anime": "anime style, cel-shaded, colorful, cute",
    "Photorealistic": "high resolution, ultra-realistic, 8k, photography",
    "Cyberpunk": "cyberpunk, neon lights, futuristic city",
    "Fantasy": "epic fantasy, magical, detailed, mythical creatures"
}

def generate_images(prompt, style, steps, width, height):
    full_prompt = f"{prompt}, {styles.get(style, '')}"
    with torch.inference_mode():
        result = pipe(
            full_prompt,
            num_inference_steps=steps,
            height=height,
            width=width,
            num_images_per_prompt=2
        )
    return result.images[0], result.images[1]

with gr.Blocks(theme=gr.themes.Soft()) as main:
    gr.Markdown("🎨 AI-Generated Branding from Text to Image 🎨")
    gr.Markdown('''AI-Generated Branding from Text to Image is a lightweight generative AI project that turns text prompts into branding visuals — including logos, mockups, and marketing materials. Ideal for startups, designers, and creators, this tool eliminates the need for manual design and speeds up brand ideation using AI.''')

    with gr.Row():
        prompt = gr.Textbox(label="Enter your prompt", placeholder="e.g. A fantasy castle in the clouds", lines=2)
        style = gr.Dropdown(label="Style", choices=list(styles.keys()), value="Default")

    with gr.Row():
        steps = gr.Slider(label="Inference Steps", minimum=10, maximum=50, value=20, step=5)
        width = gr.Slider(label="Width", minimum=256, maximum=768, value=512, step=64)
        height = gr.Slider(label="Height", minimum=256, maximum=768, value=512, step=64)

    run_button = gr.Button("🚀 Generate")
    with gr.Row():
        img1 = gr.Image(label="Image 1")
        img2 = gr.Image(label="Image 2")

    run_button.click(fn=generate_images, inputs=[prompt, style, steps, width, height], outputs=[img1, img2])

main.launch()