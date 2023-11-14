import time
import threading
import os
import openai

# Initialize OpenAI client with API key
client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


def get_last_assistant_message(thread_id):
    try:
        messages_response = client.beta.threads.messages.list(
            thread_id=thread_id)
        messages = messages_response.data
        for message in messages:
            if message.role == 'assistant':
                return " ".join(content.text.value for content in message.content if hasattr(content, 'text')).strip()
    except Exception as e:
        print(f"Error fetching messages: {e}")
    return ""


def converse(assistant_1_params, assistant_2_params, topic, message_count):
    print(f"Starting conversation on: {topic}\n")
    try:
        assistant_1 = client.beta.assistants.create(**assistant_1_params)
        assistant_2 = client.beta.assistants.create(**assistant_2_params)
        thread_1 = client.beta.threads.create()
        thread_2 = client.beta.threads.create()

        def assistant_conversation(start_message, assistant_a, thread_a, assistant_b, thread_b, msg_limit):
            message_content = start_message
            for i in range(msg_limit):
                # Change here: Accessing the name of the assistant
                assistant_name = assistant_a['name'] if isinstance(
                    assistant_a, dict) else assistant_a.name
                print(f"Turn {i + 1}: {assistant_name} speaking...")
                # ... rest of the function
                try:
                    client.beta.threads.messages.create(
                        thread_id=thread_a.id, role="user", content=message_content)
                    run = client.beta.threads.runs.create(
                        thread_id=thread_a.id, assistant_id=assistant_a.id)
                    while True:
                        run_status = client.beta.threads.runs.retrieve(
                            thread_id=thread_a.id, run_id=run.id)
                        if run_status.status == 'completed':
                            break
                        time.sleep(1)
                    message_content = get_last_assistant_message(thread_a.id)
                    print(message_content + "\n")
                    assistant_a, assistant_b = assistant_b, assistant_a
                    thread_a, thread_b = thread_b, thread_a
                except Exception as e:
                    print(f"Error during conversation: {e}")
                    break

        conversation_thread = threading.Thread(target=assistant_conversation, args=(
            f"Let's discuss {topic}", assistant_1, thread_1, assistant_2, thread_2, message_count))
        conversation_thread.start()
        conversation_thread.join()
    except Exception as e:
        print(f"Error initializing conversation: {e}")

# Define the parameters for the two assistants (example parameters provided)
# ...

# Start the conversation
# converse(assistant_1_params, assistant_2_params, "a children's book about global warming. Output story at the end of each turns output text.", 50)


# Define the parameters for the first assistant
assistant_1_params = {
    "name": "Writer",
    "instructions": "As 'Writer', your role is to create engaging and informative content. Utilize your internet browsing capability for research and staying current with trends. Use DALL-E 3 to generate images that complement your written work.",
    "tools": [
        {"type": "code_interpreter"}
    ],
    "model": "gpt-4-1106-preview"
}


# Define the parameters for the second assistant
assistant_2_params = {
    "name": "Editor",
    "instructions": "Your role as 'Editor' is to refine and enhance content. Use your internet browsing tool for fact-checking and gathering contextual information. Employ DALL-E 3 to suggest improvements or replacements for associated visual content.",
    "tools": [
        {"type": "code_interpreter"}
    ],
    "model": "gpt-4-1106-preview"
}


# Start the conversation
converse(
    assistant_1_params,
    assistant_2_params,
    "a children's book about global warming. Output story at the end of each turn's output text.",
    50
)
