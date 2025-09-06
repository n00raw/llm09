from litellm import completion
from config import PROVIDER_MODEL as MODEL

prompt = "Give 3 creative names in Thai for a smart water bottle."
for temp in [0.0, 0.5, 1.0]:
    r = completion(
        model=MODEL,
        messages=[{"role":"user","content":prompt}],
        temperature=temp,
        top_p=1.0, #top_p=0.6,
        max_tokens=150,
    )
    print("--- temperature =", temp)
    print(r.choices[0].message["content"]) 
