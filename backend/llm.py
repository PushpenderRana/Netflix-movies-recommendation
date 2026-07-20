from ollama import chat
import json
import traceback

MODELS = [
    "minimax-m3:cloud",
    "nemotron-3-super:cloud"
]


def explain_recommendations(selected_movie, recommendations):

    selected = {
        "title": selected_movie["title"],
        "genres": selected_movie["genres"],
        "overview": selected_movie["overview"]
    }

    movies = []

    for movie in recommendations:
        movies.append({
            "title": movie["title"],
            "genres": movie["genres"],
            "overview": movie["overview"]
        })

    prompt = f"""
You are an expert movie recommendation assistant.

Selected Movie:

{json.dumps(selected, indent=2)}

Recommended Movies:

{json.dumps(movies, indent=2)}

Task:
Explain why each recommended movie is similar to the selected movie.

Rules:
1. Write 2-3 complete sentences.
2. Around 50-80 words.
3. Mention:
   - Common genres
   - Similar themes
   - Main characters (if applicable)
   - Franchise relationship (if applicable)
   - Why someone who liked the selected movie would enjoy it.
4. Do NOT invent facts.
5. Return ONLY valid JSON.

Example:

[
    {{
        "title": "Spider-Man 2",
        "reason": "Spider-Man 2 continues Peter Parker's journey in the same trilogy..."
    }}
]
"""

    # Try every model until one succeeds
    for model in MODELS:

        try:

            print(f"Trying model: {model}")

            response = chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            if response is None or response.message is None:
                print(f"{model} returned no response.")
                continue

            content = response.message.content.strip()

            if not content:
                print(f"{model} returned empty content.")
                continue

            # Remove markdown code block
            if content.startswith("```"):

                lines = content.splitlines()

                if lines[0].startswith("```"):
                    lines = lines[1:]

                if len(lines) > 0 and lines[-1].startswith("```"):
                    lines = lines[:-1]

                content = "\n".join(lines)

            parsed = json.loads(content)

            print(f"Success with {model}")

            return parsed

        except Exception as e:

            print(f"{model} failed")

            traceback.print_exc()

            continue

    print("All LLM models failed.")

    return []