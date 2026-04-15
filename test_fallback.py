import os
import resend
from dotenv import load_dotenv

dotenv_path = r"c:\Users\bhalo\PromptX\backend\.env"
load_dotenv(dotenv_path=dotenv_path)

resend.api_key = os.getenv("RESEND_API_KEY")
test_email = "bhalo@gmail.com" # I'll use a placeholder or ask the user

print(f"Testing Resend with key: {resend.api_key[:10]}...")

try:
    response = resend.Emails.send({
        "from": "auth@janhelps.in",
        "to": "kartikresumes@gmail.com", # Change this to the user's actual email if possible
        "subject": "Resend Test",
        "html": "<strong>Testing Resend and API Key.</strong>"
    })
    print("Success! Response:", response)
except Exception as e:
    print("FAILED! Error details:", str(e))
