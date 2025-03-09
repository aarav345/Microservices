from groq import Groq

key = "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"
from .prompts import system_prompt


def analyze_code_with_llm(file_content, file_path):
    prompt = f"""
        Analyze the following code for:
        - Code style and formatting issues
        - Potential bugs or error
        - Performance improvements
        - Best practices

    File: {file_path}
    Content: {file_content}

    Provide a detailed JSON output with the structure"
    {{
    
        "issues": [
            {{
                "type": "<style| bugs| performance| best_practice>",
                "line": <line_number>,
                "description" : "<description>"
                "suggestion": "<suggestion>"
            }}
        ]
    }}

    ```json
    """

    client = Groq(api_key=key)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages= [
            {"role" : "system", "content" : system_prompt},
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        temperature=1,
        top_p=1   
    )

    return completion.choices[0].message.content