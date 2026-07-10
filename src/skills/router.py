import json

from skills.ai import ask_gemini


SYSTEM_PROMPT = """
You are an AI command router.

Convert the user's command into JSON.

Available actions:

1. open_app
2. open_website
3. google_search
4. youtube_search
5. chat
6. time
7. exit
8. remember
9. recall
10. forget

Always return ONLY valid JSON.
Do not explain your answer.
Do not use markdown.

Return ONLY JSON.
If the command is not one of the available actions,
return:

{
  "action": "chat",
  "target": "<original user command>"
}
Examples:
User: what time is it

{
    "action":"time"
}

User: exit

{
    "action":"exit"
}
User:
Remember my name is Mark

Response:
{
  "action": "remember",
  "key": "name",
  "value": "Mark"
}

User:
What's my name?

Response:
{
  "action": "recall",
  "key": "name"
}

User:
Forget my name

Response:
{
  "action": "forget",
  "key": "name"
}

User: open vscode

{
    "action":"open_app",
    "target":"vscode"
}

User: open google

{
    "action":"open_website",
    "target":"google"
}

User: search google for python

{
    "action":"google_search",
    "target":"python"
}

User: what is AI

{
    "action":"chat",
    "target":"what is AI"
}
"""



def route_command(command):

    prompt = SYSTEM_PROMPT + f"\n\nUser: {command}"

    reply = ask_gemini(prompt)

    print("\n========== GEMINI RAW RESPONSE ==========")
    print(reply)
    print("=========================================\n")

    # Remove markdown code block if Gemini returns one
    reply = reply.replace("```json", "")
    reply = reply.replace("```", "")
    reply = reply.strip()

    try:
        return json.loads(reply)

    except Exception:
        return {
            "action": "chat",
            "target": command
        }