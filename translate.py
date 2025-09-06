from litellm import completion
from config import PROVIDER_MODEL as MODEL

def translate(text, target_lang):
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"You are a professional translator to {target_lang}. Keep tone & meaning."},
            {"role":"user","content":text}
        ],
        temperature=0.2, max_tokens=220,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    #print(translate("Hello, how are you today?", "French"))
    print(translate("Am I a cow?", "Cow"))
