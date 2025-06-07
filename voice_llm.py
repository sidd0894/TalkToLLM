from ollama import chat
from speech_utils.speech_converter import SpeechToSpeech
import argparse
import os
import json
import time


conversation_context = None

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--load-session', type=str, help='json file path to load previous session', metavar='')
    parser.add_argument('--save-session', type=str, help='directory path to save the current session', metavar='')
    parser.add_argument('--model', type=str, required=True, help='provide the ollama model name', metavar='')
    args = parser.parse_args()

    if args.load_session is not None and not os.path.exists(args.load_session):
        parser.error('[ERROR] Invalid session path given.')
    if args.save_session is not None and not os.path.exists(args.save_session):
        parser.error('[ERROR] Invalid path for saving session.')
    if args.model is None or args.model.strip() == '':
        parser.error('[ERROR] Enter a valid ollama model name.')
    
    return (args.load_session, args.save_session, args.model)


def construct_filename():
    ct = time.localtime()
    year = ct.tm_year
    month = ct.tm_mon
    date = ct.tm_mday
    hour = ct.tm_hour
    minute = ct.tm_min
    second = ct.tm_sec
    return f'session_{year}{month}{date}_{hour}{minute}{second}.json'


def generateResponse(prompt, model_name):
    userMessage = {"role": "user", "content": prompt}
    conversation_context.append(userMessage)
    response = chat(model=model_name, messages=conversation_context)
    reply = response.message.content.strip().replace('*', '')
    modelMesage = {"role": "assistant", "content": reply}
    conversation_context.append(modelMesage)
    return reply


def main():
    global conversation_context

    load_session_path, save_session_path, model = getArguments()
    if load_session_path is None:
        system_prompt = input('System Prompt: ').strip()
        conversation_context = [{"role": "system", "content": system_prompt}]
    else:
        with open(load_session_path, 'r', encoding='utf-8') as file:
            conversation_context = json.load(file)
        
    speech = SpeechToSpeech()
    while True:
        input('Hit enter to speak\n')
        user_prompt = speech.speech_to_text()
        if user_prompt.lower() in ['goodbye', 'bye']:
            break
        elif user_prompt == 'save this session':
            filename = construct_filename()
            file_path = os.path.join(save_session_path, filename) if save_session_path is not None else filename
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(conversation_context, file, indent=4)
            
            print('[INFO] Session saved.')
            continue

        print(f'Prompt: {user_prompt}')
        response = generateResponse(prompt=user_prompt, model_name=model)
        print(f'Response: {response}')
        speech.text_to_speech(response, speech_rate=145, voice_index=1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nKeyboard interruption. Exiting...')