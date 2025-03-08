import base64
from groq import Groq

code_str= "ZGVmIGdldF9wcl9pbmZvKHJlcG9fdXJsLCBwcl9udW1iZXIsIGdpdGh1Yl90\nb2tlbik6CiAgICAiIiIKICAgIEEgZHVtbXkgZnVuY3Rpb24gdGhhdCByZXR1\ncm5zIGR1bW15IGRhdGEKICAgICIiIgogICAgcmV0dXJuIHsKICAgICAgICAn\ndGl0bGUnOiAnRHVtbXkgUFIgdGl0bGUnLAogICAgICAgICdib2R5JzogJ0R1\nbW15IFBSIGJvZHknLAogICAgICAgICdhdXRob3InOiAnRHVtbXkgYXV0aG9y\nJywKICAgICAgICAnbGFiZWxzJzogWydkdW1teS1sYWJlbCddLAogICAgICAg\nICdzdGF0ZSc6ICdvcGVuJwogICAgfQo=\n"
key = "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"




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
            {
                "role" : "user",
                "content" : prompt
            }
        ],
        temperature=1,
        top_p=1   
    )


    print(completion.choices[0].message.content)



analyze_code_with_llm(base64.b64decode(code_str).decode(), "test.py")

