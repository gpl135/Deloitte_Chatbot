from langsmith import Client
from dotenv import load_dotenv
load_dotenv()


client = Client()

dataset = client.create_dataset(
    dataset_name="chatbot-bot-dataset",
    description="Test dataset for chatbot evaluation"
)

# Correct format
client.create_example(
    inputs={"input": "What is AI?"},
    outputs={"output": "Artificial Intelligence"},
    dataset_id=dataset.id
)

client.create_example(
    inputs={"input": "Who are you?"},
    outputs={"output": "assistant"},
    dataset_id=dataset.id
)