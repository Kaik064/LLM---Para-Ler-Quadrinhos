from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

load_dotenv()

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = os.environ.get("MINHA_APY_KEY")
)
#Prompt para IA analisar o quadrinho

with open ("prompt.txt","r",encoding="utf-8") as arquivo:
    prompt = arquivo.read()

def analisarQuadrinho(imagem):
    image_base64 = base64.b64encode(
        imagem.read()
    ).decode("utf-8")

    response = client.chat.completions.create(
         model = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        messages=[
            {
                "role": "user",
                "content":[
                     {
                        "type" : "text",
                        "text" : prompt
                        
                    },
                    {
                        "type" : "image_url",
                         "image_url" : {
                        "url" : f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    return (response.choices[0].message.content)