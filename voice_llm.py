from ollama import chat
from speech_utils.speech_converter import SpeechToSpeech

model = input('Ollama model name: ').strip()
system_prompt = input('System Prompt: ').strip()
conversation_context = [{"role": "system", "content": system_prompt}]


def generateResponse(prompt, model_name):
    global conversation_context

    userMessage = {"role": "user", "content": prompt}
    conversation_context.append(userMessage)

    response = chat(model=model_name, messages=conversation_context)
    reply = response.message.content.strip().replace('*', '')
    modelMesage = {"role": "assistant", "content": reply}
    conversation_context.append(modelMesage)

    return reply


def main():
    speech = SpeechToSpeech()
    while True:
        input('Hit enter to speak\n')
        user_prompt = speech.speech_to_text()
        if user_prompt.lower() in ['goodbye', 'bye']:
            break

        print(f'Prompt: {user_prompt}')
        response = generateResponse(prompt=user_prompt, model_name=model)
        print(f'Response: {response}')
        speech.text_to_speech(response, speech_rate=145, voice_index=1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboard interruption. Exiting...')