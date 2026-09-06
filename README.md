# 🤖 AI Text Generator

A simple web-based **AI Text Generator** built using **Streamlit** and **Hugging Face Transformers**. The application allows users to enter a sentence or short prompt and generates a continuation using a pretrained language model.

---

## 📌 About the Project

This project demonstrates how a pretrained **Transformer-based language model** can be integrated with an interactive Streamlit web application.

Instead of training a language model from scratch, the application uses a pretrained model from Hugging Face. Users can enter a prompt, and the AI generates text based on the provided context.

The project provides a practical introduction to **Generative AI, Natural Language Processing, and Large Language Models**.

---

## ✨ Features

- 📝 Simple text input area
- 🤖 AI-generated text completion
- ✨ Generate Text button
- ⏳ Loading message while generating
- 📄 Separate generated-text output section
- 🧠 Pretrained Transformer model
- ⚡ Model caching for faster interaction
- 🎨 User-friendly Streamlit interface
- ⚠️ Warning message when no input is provided

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| Hugging Face Transformers | AI model integration |
| PyTorch | Model execution |
| GPT-Neo | Text generation |
| GitHub | Project hosting |

---

## 🧠 AI Model

This project uses the following pretrained model:

```text
EleutherAI/gpt-neo-125M

GPT-Neo 125M is a pretrained autoregressive language model developed by EleutherAI. It is designed to predict and generate text based on the context provided by the user.

The model is loaded through the Hugging Face Transformers library and used with the `text-generation` pipeline.

### Model Details

| Property | Details |
|---|---|
| Model | GPT-Neo 125M |
| Model ID | `EleutherAI/gpt-neo-125M` |
| Provider | Hugging Face |
| Task | Text Generation |
| Model Type | Autoregressive Language Model |
| Library | Transformers |
| Programming Language | Python |

---

## 🔄 How It Works

The application follows a simple five-step process:

```text
User Input
    ↓
Streamlit Application
    ↓
Hugging Face Transformers
    ↓
GPT-Neo 125M
    ↓
Generated Text
    ↓
Output Display

---

## 1️⃣ User Input

The user enters a sentence or short prompt into the text area.

For example:

```text
Artificial intelligence is changing the way we live and work by

a powerful technology that can understand and generate human-like text.
It can be used for writing, learning, communication, and many other applications.

---

## 2️⃣ Streamlit Application

The Streamlit application receives the user's prompt when the **Generate Text** button is clicked.

The application is responsible for:

- Accepting the user's input
- Sending the prompt to the AI model
- Processing the generated result
- Displaying the generated text

---

## 3️⃣ Hugging Face Transformers

The project uses the Hugging Face `transformers` library to load and use the pretrained language model.

The text-generation pipeline makes it easier to perform text generation without building the complete AI model from scratch.

```python
from transformers import pipeline

---

## 4️⃣ GPT-Neo 125M Processing

The application uses the **GPT-Neo 125M** model to process the text entered by the user.

The model is loaded using the Hugging Face text-generation pipeline:

```python
generator = pipeline(
    "text-generation",
    model="EleutherAI/gpt-neo-125M"
)

---

### Model Processing Steps

The GPT-Neo model performs the following steps:

1. Receives the user's prompt.
2. Processes the input context.
3. Predicts the next tokens.
4. Generates a continuation of the prompt.
5. Returns the generated text to the application.

---

## 5️⃣ Text Generation

Once the prompt is received, the application sends it to the GPT-Neo model for text generation.

```python
result = generator(
    prompt,
    max_length=60,
    num_return_sequences=1
)
### Parameters Used

| Parameter | Description |
|---|---|
| `prompt` | The text entered by the user |
| `max_length` | Defines the maximum length of the generated sequence |
| `num_return_sequences` | Specifies the number of generated text sequences |

The generated result is stored in the `result` variable and can then be displayed to the user.

---

## 6️⃣ Output Display

After the model finishes generating the text, the application extracts the generated content from the result.

```python
generated_text = result[0]["generated_text"]
---

## 7️⃣ User Interaction

The application allows users to interact with the AI model through a simple Streamlit interface.

### User Steps

1. Enter a sentence or prompt in the text box.
2. Click the **Generate Text** button.
3. The application sends the prompt to GPT-Neo.
4. GPT-Neo generates a continuation.
5. The generated text is displayed on the screen.

---

## 8️⃣ Example of Text Generation

### Input Prompt

```text
Artificial Intelligence is

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

---

## 📸 Application Preview

<img width="1517" height="811" alt="Screenshot 2026-09-06 190212" src="https://github.com/user-attachments/assets/dcd3a8b6-9862-495e-bf69-6c85f053029c" />


---

## 🧪 Example

### Input

```text
Artificial Intelligence is

### Generated Output

```text
Artificial Intelligence is transforming the way people
learn, work, communicate, and solve problems using
advanced technologies and intelligent systems.

## 🔄 How It Works

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/fb4d88a6-45a8-4c67-affa-f5bd81c35c9b" />

##🔹 Workflow Steps
1.User Input – The user enters a text prompt.
2.Streamlit Application – The application receives the prompt.
3.Hugging Face Pipeline – The prompt is passed to the text-generation pipeline.
4.GPT-Neo 125M – The pretrained model processes the input.
5.Text Generation – The model generates the continuation text.
6.Generated Output – The generated text is displayed to the user.

##🛠️ Technologies Used
| Technology                | Purpose                             |
| ------------------------- | ----------------------------------- |
| Python                    | Application development             |
| Streamlit                 | Web application interface           |
| Hugging Face Transformers | Text generation                     |
| PyTorch                   | Deep learning framework             |
| GPT-Neo 125M              | AI text generation                  |
| GitHub                    | Version control and project hosting |

##⚙️ Installation
*Clone the Repository
  git clone https://github.com/manishadharani1305-glitch/AI-Text-Generator.git
cd AI-Text-Generator
*Install Required Libraries
pip install -r requirements.txt
*Run the Application
streamlit run app.py

##📁 Project Structure
AI-Text-Generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
