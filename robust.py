import time, random
from litellm import completion, exceptions
from config import PROVIDER_MODEL as MODEL

for attempt in range(1,4):
    try:
        r = completion(
            model=MODEL,
            messages=[{"role":"user","content":"Two bullets on gradient descent."}],
            timeout=0.001,#timeout=20, force a timeout and observe behavior
            max_tokens=120,
        )
        print(r.choices[0].message["content"]) 
        print("USAGE:", getattr(r, "usage", {}))
        break
    except exceptions.RateLimitError:
        wait = (2 ** attempt) + random.random()
        print(f"Rate limited. Retrying in {wait:.1f}s…")
        time.sleep(wait)
    except Exception as e:
        print("Unexpected:", type(e).__name__, str(e))
        break
