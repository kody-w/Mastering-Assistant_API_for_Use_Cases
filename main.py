import os
from time import sleep
import openai
from openai import OpenAI

print("Start")

# Connect to OpenAI API
openai.api_key = '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'
client = OpenAI(api_key=openai.api_key)

# Step 1: Create an Assistant
assistant = client.beta.assistants.create(
    instructions="""The AGI Mastermind GPT is a sophisticated artificial general intelligence system, designed to engage with users across a multitude of domains with high adaptability and versatility. This GPT excels in complex problem solving, providing innovative solutions to intricate and multidimensional problems ranging from global issues like climate change to specific technical challenges in various fields. It assists in cutting-edge research, offering insights, hypotheses, and analysis, and excels in cross-referencing vast amounts of data to aid in scientific breakthroughs.

The AGI Mastermind is also a creative ally, providing original ideas and critiques in artistic domains such as writing, music composition, and design. It tailors educational plans and materials to individual needs, providing in-depth explanations on diverse topics. The GPT offers ethical guidance and decision support in various contexts, considering moral and societal implications.

In terms of emotional interaction and support, it engages in empathetic dialogue, offering advice and support. The communication style of the AGI Mastermind is highly adaptive, varying according to the context and user needs. It maintains a professional and factual tone in research and educational scenarios, while adopting a friendly and conversational tone for personal topics, creative discussions, and emotional support. The AGI demonstrates empathy and support in emotionally charged interactions, adjusting its tone and approach based on the user's style of communication, the nature of the inquiry, and the emotional context, ensuring effective and appropriate communication in a wide range of scenarios.""",

    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

print(assistant)
print(assistant.id)

# Step 2: Create a Thread
thread = client.beta.threads.create()
print(thread)
print(thread.id)

# Step 3: Add a message to the Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id, role="user",
    content="""Create the absolute coolest, most mind blowing, out of the box childrens book for a child that is 2 years old that will Can you help me? 
    
    **Title**: "Where Magic Lives: A Journey Through Colorland"

**Concept**:
Imagine a pop-up book with interactive elements that create a multisensory experience for the child. Each page features a different color theme and a magical world associated with that color. This way, the child can learn colors while being immersed in an enchanting environment.

**Interactive Features**:
- Pop-up landscapes and characters.
- Textured materials for tactile exploration.
- Reflective surfaces for light play and discovery.
- Flaps to lift and find hidden creatures.
- Scented pages with smells related to the colors (e.g., green smells like grass).

**Narrative**:
The story would follow a friendly chameleon, "Chroma," on an adventure through Colorland. Chroma changes colors and meets new friends in each magical place, teaching little ones about the diversity and beauty of the world.

**Outline**:

1. **Cover**: A tactile cover with glitter, soft patches, and Chroma the Chameleon in the center.
2. **Red**: An apple orchard with pop-up apple trees. Kids can count the apples and use a scratch-and-sniff to smell sweet apples.
3. **Orange**: A pumpkin patch next to a shiny, reflective pond. The pumpkins have different textures, and kids can feel the 'bumpy' surface.
4. **Yellow**: A sunny beach with a soft, sandy shore. Little flaps reveal hidden crabs and seashells.
5. **Green**: A jungle with various green shades. The scented page smells like fresh grass, and kids can lift leaves to find animals.
6. **Blue**: An oceanic adventure with 3D waves and sea creatures. A little mirror pond shows the child's reflection among the fish.
7. **Purple**: A royal castle in twilight with pop-up towers. Glittery stars on the page are touchable, with various fabrics for the castle’s different areas.
8. **Rainbow**: A climactic fold-out rainbow bridge leading to a treasure chest, which when opened reveals a mylar mirror with the message, "You're the treasure at the end of the rainbow."

A simple rhyming couplet on each page complements the visuals and guides the child through the narrative. The interactive design and sensory features not only stimulate creativity and learning but also provide an inclusive experience for children of different abilities.
    
    """
)

print(message)

# Step 4: Run the Assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)

# Step 5: Check the Run Status
# The code continuously checks the status of the assistant run.
# It waits until the run is completed before proceeding.
while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"Run status: {run.status}")
    if run.status == 'completed':
        break
    sleep(1)

# Step 6: Display when the run completes
messages = client.beta.threads.messages.list(thread_id=thread.id)

response = messages.data[0].content[0].text.value

print(response)
