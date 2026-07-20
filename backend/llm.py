from ollama import chat
import json


def explain_recommendations(selected_movie, recommendations):

    prompt = f"""
You are an expert movie recommendation assistant.

Selected movie:
{selected_movie}

Recommended movies:
{json.dumps(recommendations, indent=2)}

Explain why each movie was recommended.

Return ONLY a JSON array like:

[
  {{
    "title": "Movie Name",
    "reason": "Reason"
  }}
]
"""

    try:
        response = chat(
            model="minimax-m3:cloud",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.message.content.strip()

        # Remove Markdown code fences if present
        if content.startswith("```"):
            lines = content.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            content = "\n".join(lines)

        return json.loads(content)

    except Exception as e:
        print("LLM Error:", e)

        return []