import openai
import os
import dotenv
import json

dotenv.load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_category(item_name):
    # Using function calling to generate a category based on the item name
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Generate a category for the item: {item_name}",
            }
        ],
        functions=[
            {
                "name": "generate_category",
                "description": "Generates a category for a given item name",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category of the item"
                        }
                    },
                    "required": ["category"]
                }
            }
        ],
        function_call={"name": "generate_category"}
    )
    
    return json.loads(response.choices[0].message.function_call.arguments)['category'].strip()