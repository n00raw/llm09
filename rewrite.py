from litellm import completion
from config import PROVIDER_MODEL as MODEL

def rewrite(text, style):
    styles = {
        "formal":"formal, business‑appropriate",
        "casual":"friendly, conversational",
        "technical":"precise technical writing",
        "marketing":"persuasive, benefits‑led"
    }
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"Rewrite in {styles.get(style,'clear and concise')} style while preserving meaning."},
            {"role":"user","content":text}
        ],
        temperature=0.4, max_tokens=200,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    print(rewrite("Bananas are typically curved and elongated, with a smooth peel that is yellow when ripe, though other colors are possible.", "marketing"))
