
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()


def classify_with_llm(log_message):
    prompt = f'''classify the log message into one of these categories:
    (1)Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category , return "Unclassified".
    Only return the category name.No preamble.
    loG MESSAGE: {log_message}'''

    # Create Groq client (API key is read from GROQ_API_KEY env var)
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    test_logs = [
        "Case escalation for ticket ID 7324 failed because the assigned support agent",
        "Invoice generation process aborted for order ID 8910 due to invalid tax calculation",
        "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' instead.",
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate"
    ]

    for log in test_logs:
        classification = classify_with_llm(log)
        print(f"Log: {log}\nClassification: {classification}\n")