import random

import openai


def get_answer_with_history(message_list, api_key):
    openai.api_key = api_key
    temperature = random.randint(0, 100) / 100
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature=temperature,
        messages=message_list,
        stream=True
    )
    # create variables to collect the stream of chunks
    collected_chunks = []
    collected_messages = []

    for chunk in response:
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        collected_messages.append(chunk_message)  # save the message

    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    print(f"Full conversation received: {full_reply_content}")
    print('Temperature: ' + str(temperature))
    # print('Generated answer: ' + full_reply_content)
    return full_reply_content
