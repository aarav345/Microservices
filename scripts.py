import base64
from groq import Groq

code_str= "aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBiYXNlNjQKCgoKCiMgaHR0cHM6Ly9h\ncGkuZ2l0aHViLmNvbS9yZXBvcy9hYXJhdjM0NS9NaWNyb3NlcnZpY2VzL3B1\nbGxzLzEvZmlsZXMKCgpkZWYgZ2V0X293bmVyX3JlcG8ocmVwb191cmwpOgog\nICAgdXJsX2xpc3QgPSBsaXN0KGZpbHRlcihsYW1iZGEgeDogeC5zdHJpcCgp\nLCByZXBvX3VybC5zcGxpdCgiLyIpKSkKICAgIGlmIGxlbih1cmxfbGlzdCkg\nPj0gMjoKICAgICAgICByZXR1cm4gdXJsX2xpc3RbLTJdLCB1cmxfbGlzdFst\nMV0KICAgIHJldHVybiBOb25lLCBOb25lCgoKCmRlZiBmZXRjaF9wcl9maWxl\ncyhyZXBvX3VybCwgcHJfbnVtYmVyLCBnaXRodWJfdG9rZW4pOgogICAgb3du\nZXIsIHJlcG8gPSBnZXRfb3duZXJfcmVwbyhyZXBvX3VybCkKICAgIHVybCA9\nIGYiaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy97b3duZXJ9L3tyZXBv\nfS9wdWxscy97cHJfbnVtYmVyfS9maWxlcyIKICAgIGhlYWRlcnMgPSB7CiAg\nICAgICAgIkF1dGhvcml6YXRpb24iIDogZiJ0b2tlbiB7Z2l0aHViX3Rva2Vu\nfSIKICAgIH0gaWYgZ2l0aHViX3Rva2VuIGVsc2Uge30KICAgIHJlc3BvbnNl\nID0gcmVxdWVzdHMuZ2V0KHVybD11cmwsIGhlYWRlcnM9aGVhZGVycykKICAg\nIHJlc3BvbnNlLnJhaXNlX2Zvcl9zdGF0dXMoKSAjaGFuZGxlcyBlcnJvcgog\nICAgcmV0dXJuIHJlc3BvbnNlLmpzb24oKQoKCgpkZWYgZmV0Y2hfZmlsZV9j\nb250ZW50KHJlcG9fdXJsLCBmaWxlX3BhdGgsIGdpdGh1Yl90b2tlbik6CiAg\nICBvd25lciwgcmVwbyA9IGdldF9vd25lcl9yZXBvKHJlcG9fdXJsKQogICAg\ndXJsID0gZiJodHRwczovL2FwaS5naXRodWIuY29tL3JlcG9zL3tvd25lcn0v\ne3JlcG99L2NvbnRlbnRzL3tmaWxlX3BhdGh9IgogICAgaGVhZGVycyA9IHsK\nICAgICAgICAiQXV0aG9yaXphdGlvbiIgOiBmInRva2VuIHtnaXRodWJfdG9r\nZW59IgogICAgfSBpZiBnaXRodWJfdG9rZW4gZWxzZSB7fQogICAgcmVzcG9u\nc2UgPSByZXF1ZXN0cy5nZXQodXJsPXVybCwgaGVhZGVycz1oZWFkZXJzKQog\nICAgcmVzcG9uc2UucmFpc2VfZm9yX3N0YXR1cygpICNoYW5kbGVzIGVycm9y\nCiAgICBjb250ZW50ID0gcmVzcG9uc2UuanNvbigpWydjb250ZW50J10KICAg\nIHJldHVybiBiYXNlNjQuYjY0ZGVjb2RlKGNvbnRlbnQpLmRlY29kZSgpCgoK\nCg==\n"
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

