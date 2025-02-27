from openai import OpenAI
client = OpenAI()

def obtenerRespuesta(promptDeDesarrollo: str, promptDeUsuario: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": promptDeDesarrollo},
            {"role": "user", "content": promptDeUsuario}
        ],
        max_tokens=500
    )

    output: str = completion.choices[0].message.content
    return output