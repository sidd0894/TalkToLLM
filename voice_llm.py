from ollama import chat
from speech_utils.speech_converter import SpeechToSpeech

system_prompt = input('System Prompt: ').strip()
# systemPrompt = "Talk like a human. Do not answer too much long. Do not use any emojis. Do not answer in multiple paragraphs. Do not use asterisk anywhere in the answer."
# systemPrompt = "Your name is Mark. Talk like a human. Do not respond too much long. Do not use any emojis. Do not respond in bullet points or points. Do not use asterisk anywhere in the response."

conversation_context = [{"role": "system", "content": system_prompt}]


def generateResponse(prompt):
    global conversation_context

    userMessage = {"role": "user", "content": prompt}
    conversation_context.append(userMessage)

    # response = chat(model="gemma3:1b", messages=conversation_context)
    response = chat(model="llama3.2:1b", messages=conversation_context)
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
        response = generateResponse(prompt=user_prompt)
        print(f'Response: {response}')
        speech.text_to_speech(response, speech_rate=145, voice_index=1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboard interruption. Exiting...')