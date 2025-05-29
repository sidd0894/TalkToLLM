# Voice Chat with Ollama LLM

## Introduction

This project allows you to interact with a locally running large language model (LLM) through voice. It uses speech recognition to capture spoken input, sends it to an LLM served by [Ollama](https://ollama.com/), and then converts the model's response back to speech. The conversation maintains context for multi-turn dialogues, creating a more natural interaction experience.


## Project Setup

### 1. Install and Run Ollama

Before running this project, you **must have Ollama installed and running** on your system.

**Download Ollama:**

Visit the official website to install Ollama for your platform:

👉 [https://ollama.com/download](https://ollama.com/download)

### 2. Verify Ollama Installation

After installation, run the following command in your terminal to verify that Ollama is installed correctly:

```bash
ollama
```

If installed properly, this command will display a list of available Ollama commands (like `run`, `pull`, `list`, etc.).

If you see a "command not found" or similar error, ensure that:
- Ollama is successfully installed
- The binary is added to your system’s PATH

### 3. Download an LLM Model

To download a supported model (e.g., llama3, Mistral), use:

```bash
ollama run <model_name>
```

You only need to download the model once — Ollama caches it locally.

Check available models: [https://ollama.com/library](https://ollama.com/library)

For example:

```bash
ollama run gemma3:1b
```

### 4. Install Python Dependencies

Install the required Python packages using `pip`:

#### Option 1: Direct installation

```bash
pip install ollama
```

Additionally, install dependencies used in `speech_utils`, such as:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

#### Option 2: Using `requirements.txt`

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Program

### 1. Start the Ollama Server

In a new terminal window, start the Ollama server by running:

```bash
ollama serve
```

This command launches the Ollama backend, which is required for processing requests from the Python script.


### 2. Run the Python Program

Once the server is running, open another terminal window and run the Python script:

```bash
python voice_llm.py
```

You will be prompted to enter the model name and system prompt.


### 3. Enter the Model Name

When prompted:

```
Ollama model name:
```

Enter the **exact model name** you downloaded or used previously via Ollama (e.g., `llama3`, `mistral`, `codellama`, etc.).


### 4. Enter the System Prompt

After that, you’ll be asked:

```
System Prompt:
```

This is used to set the assistant’s behavior or personality.
For example, entering:

```
You are a helpful and friendly assistant.
```

will guide the model to respond in that tone throughout the conversation.


### 5. Start Speaking

After setup:

* Press the **Enter** key each time you want to speak.
* The program will capture your voice, convert it to text, and send it to the model.
* The LLM's response will be spoken back to you using text-to-speech.


### 6. End the Chat

To stop the conversation, simply **say**:

```
bye
```

or

```
goodbye
```

The program will detect this and exit the loop gracefully.


## How It Works

1. **Voice Input (Speech-to-Text)**
   When you press the **Enter** key, the program records your voice using the `SpeechRecognition` module. It processes the audio and converts it into text using a speech recognition engine (typically Google Web Speech API).

2. **Maintaining Conversation Context**
   The recognized text is appended to a conversation history list. This context is maintained across multiple turns so the LLM can respond appropriately in an ongoing dialogue.

3. **Generating Responses with Ollama**
   The user’s text input, along with the existing conversation history and the initial system prompt, is sent to a locally hosted LLM via the `ollama` Python package. The model processes the input and returns a relevant, contextual response.

4. **Voice Output (Text-to-Speech)**
   The response from the LLM is then converted into spoken audio using the `pyttsx3` text-to-speech module, allowing the assistant to "speak" the reply aloud.

5. **Interaction Loop**
   After each response, the program waits for you to press **Enter** again to speak the next prompt. This loop continues until you say `"bye"` or `"goodbye"`, which ends the session.
