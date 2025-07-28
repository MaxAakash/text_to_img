===========================
#Readme
===========================

📌 HOW TO RUN
-------------

1. Make sure Python 3.8+ is installed (Colab works fine too).
2. Install required libraries:

   pip install diffusers transformers accelerate gradio

3. Run the script:

   python stable_diffusion_ui.py

4. A web interface will open in your browser.
   Enter your prompt, choose style, resolution, steps — and click "Generate".

💻 TECHNOLOGIES USED
---------------------

- 🤖 Diffusers (by HuggingFace): Core library for Stable Diffusion pipelines.
- ⚙️ Transformers: Required for handling prompt tokenization.
- 🚀 Accelerate: Helps with device (CPU/GPU) compatibility.
- 🎨 Gradio: Easy and beautiful web interface for image generation apps.
- 🔍 torch (PyTorch): Underlying deep learning framework.

🧠 WHY THESE TOOLS?
--------------------

- HuggingFace's `diffusers` is the most flexible and lightweight way to run Stable Diffusion.
- `Gradio` makes it easy to create a friendly, shareable UI — no frontend code needed.
- `torch` and `accelerate` let the model automatically choose CUDA if available, otherwise fallback to CPU.
- Designed to run **without login, keys, or APIs** — lightweight and offline-ready.

⚠️ TROUBLESHOOTING
--------------------

- If the **images are taking too long to generate**, it's likely you're running on CPU.
- The model runs much faster with **CUDA (GPU)**. If it's unavailable, generation time will be higher.
- To fix this:
   ✅ Enable **GPU** in Colab (`Runtime > Change runtime type > GPU`)
  
   ✅ Try running the code in Google Colab (with GPU enabled in settings).

   ✅ Or, run it on your **own machine** if you have a dedicated GPU (NVIDIA recommended).

- If you're using Colab and GPU quota is over, wait a few hours or try CPU mode (but slower).

📂 OUTPUT
---------

- The app generates **2 images per prompt** and displays them in the interface.
- Future versions can save images locally or allow downloading.

  
Original file is located at
    https://colab.research.google.com/drive/18-qZl8JNj0DdqsFRZ-wkSyl-TuEXG_lw


Made with ❤️ for quick GenAI experiments.
