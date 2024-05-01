from google.cloud import dialogflow_v2beta1
from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
import google



# Set the project and location IDs for your Dialogflow CX project
project_id =  "interviewer-bot-421804"
location_id = "global"
agent_id = "610c58b1-0902-4072-a4c3-97207b471846"
agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
parent = f"projects/{project_id}/locations/{location_id}"

agent_components = AgentsClient.parse_agent_path(agent)

location_id = agent_components["location"]

if location_id == "global":
    api_endpoint = "global-dialogflow.googleapis.com:443"
    print(f"API Endpoint: {api_endpoint}\n")
    client_options = {"api_endpoint": api_endpoint}

# Set up the Dialogflow CX client
client = dialogflow_v2beta1.ConversationsClient(client_options=client_options)

# Use the API to retrieve a list of all the conversations in the project
conversations = client.list_conversations(
    parent=f"projects/{project_id}/locations/{location_id}",
)

print(conversations)


# Print the list of conversations
for conversation in conversations:
   
    print(conversation)

# Select the conversation for which you want to fetch the transcript
conversation_id = "eb6e5a-cfc-260-574-93669354a"




 

# Use the API to retrieve the full conversation history

messages = client.list_messages(
    parent=f"projects/{project_id}/locations/{location_id}/conversations/{conversation_id}"
)
  # Process conversation messages here



# Format the conversation history into a transcript
transcript = ""
for message in messages:
    # Add the message text and timestamp to the transcript
    transcript += f"{message.content} ({message.create_time})\n"

# Print the transcript
print(transcript)