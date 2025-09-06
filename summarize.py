from litellm import completion
from config import PROVIDER_MODEL as MODEL

def summarize(text, length="brief"):
    lengths = {"brief":"in 1–2 sentences","medium":"in 3–4 sentences","detailed":"in 5–6 sentences with key points"}
    r = completion(
        model=MODEL,
        messages=[
            {"role":"system","content":f"You are an expert summarizer. Summarize {lengths.get(length,'in 2–3 sentences')}"},
            {"role":"user","content":text}
        ],
        temperature=0.3, max_tokens=70,
    )
    return r.choices[0].message["content"].strip()

if __name__ == "__main__":
    sample = """What is a banana? 
    A banana is an elongated, edible, yellow-skinned fruit, technically a berry, that grows in bunches on a large, herbaceous flowering plant of the genus Musa. Native to Southeast Asia, it is a globally popular and nutritious food, rich in carbohydrates, fiber, potassium, and vitamins B6 and C. While most people refer to sweet, soft dessert bananas like the Cavendish, other varieties called plantains are starchier and must be cooked before consumption."""
    print(summarize(sample, "brief"))