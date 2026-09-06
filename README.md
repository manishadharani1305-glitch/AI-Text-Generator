# 🤖 AI Text Generator

An AI-powered web application that generates text from user-provided prompts using **GPT-Neo 125M**, **Hugging Face Transformers**, and **Streamlit**.

The project demonstrates how a pretrained language model can be integrated into an interactive application for automatic text generation.

---

## 📌 About the Project

The **AI Text Generator** allows users to enter a text prompt and generate meaningful text using a pretrained Transformer-based language model.

The application provides a simple and user-friendly interface where users can enter a sentence, click the **Generate Text** button, and view the AI-generated continuation.

---

## ✨ Features

- 📝 User-friendly text input
- 🤖 AI-powered text generation
- 🧠 Uses pretrained GPT-Neo 125M
- ⚡ Fast and simple generation
- 🖥️ Interactive Streamlit interface
- 🔄 Generates text based on user prompts
- 📊 Displays generated output clearly
- 🚫 Shows a warning when no input is provided
- 💾 Supports model loading and reuse

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| Hugging Face Transformers | AI model and text generation |
| PyTorch | Deep learning framework |
| GPT-Neo 125M | Text generation |
| GitHub | Version control and project hosting |

---

## 🧠 AI Model

This project uses the pretrained language model:

**EleutherAI/gpt-neo-125M**

### Model Details

| Parameter | Details |
|---|---|
| Model | GPT-Neo 125M |
| Developer | EleutherAI |
| Architecture | Transformer |
| Parameters | 125 Million |
| Task | Text Generation |
| Library | Hugging Face Transformers |

---

## 🔄 How It Works

The application follows a simple AI text-generation workflow:

```text
User Input
    ↓
Streamlit Application
    ↓
Hugging Face Pipeline
    ↓
GPT-Neo 125M
    ↓
Text Generation
    ↓
Generated Output
    ↓
Display to User
```

---

## 📸 Application Preview

<img width="1517" height="811" alt="AI Text Generator Application" src="https://github.com/user-attachments/assets/dcd3a8b6-9862-495e-bf69-6c85f053029c" />

---

## 🧪 Example

### Input

```text
Artificial Intelligence is
```

### Generated Output

```text
Artificial Intelligence is transforming the way people
learn, work, communicate, and solve problems using
advanced technologies and intelligent systems.
```

---

## 🔄 How It Works

<img width="1536" height="1024" alt="AI Text Generator Workflow" src="https://github.com/user-attachments/assets/fb4d88a6-45a8-4c67-affa-f5bd81c35c9b" />

### 🔹 Workflow Steps

1. **User Input** – The user enters a text prompt.
2. **Streamlit Application** – The application receives the prompt.
3. **Hugging Face Pipeline** – The prompt is passed to the text-generation pipeline.
4. **GPT-Neo 125M** – The pretrained model processes the input.
5. **Text Generation** – The model generates the continuation text.
6. **Generated Output** – The generated text is displayed to the user.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manishadharani1305-glitch/AI-Text-Generator.git
cd AI-Text-Generator
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
AI-Text-Generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

