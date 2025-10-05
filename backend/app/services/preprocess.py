import json
import re

# this returns the json format
def preprocess_image(context, llm): # context is certification information extracted by one certificate

  Json_format = {
      "certificate_title": "...",
      "recipient_name": "...",
      "institution_name": "...",
      "issue_date": "YYYY-MM-DD",
      "certificate_id": "...",
      "other_details": ""
  }

  prompt = f"""
  You are a text preprocessing assistant.
  You will receive raw OCR text extracted from a certificate.
  The OCR text may contain errors, extra characters, or misrecognized words.
  Your task is to:
  1. Correct obvious OCR errors and remove meaningless characters.
  2. Extract and structure the certificate information into the following JSON format:
  {Json_format}
  3. If some fields are missing, leave them as null instead of guessing.
  4. Preserve original meaning and wording wherever possible.

  Input OCR text: {context}
  """

  cleaned_data = llm.invoke(prompt).content
  cleaned_data = re.sub(r"^```json\s*|\s*```$", "", cleaned_data.strip())
  cleaned_data_json = json.loads(cleaned_data)
  return cleaned_data_json