import re

image_score = "Reasoning: Based on the provided documents, the certificate from 'WKF WORLD HEAD OFFICE' is for a 'Kru Muaythai Trainer'. This is a specialized certification for a martial arts coach, not a general personal trainer. The institutions identified as valid sources from the related documents (e.g., IntensivePT, International Sports Sciences Association, National Academy of Sports Medicine) issue certificates with titles like \"Certified Personal Trainer\" or \"International Personal Trainer,\" which cover broader fitness principles. This certificate's focus on a specific combat sport makes it different from a standard personal trainer certification.\nScore: 4"

raw_text = image_score.content.strip() if hasattr(image_score, "content") else str(image_score)
print(f"Raw LLM response: {raw_text}")

# Step 5: Parse Reasoning and Score
reasoning_match = re.search(r"Reasoning:\s*(.+?)(?:\n|$)", raw_text, re.DOTALL)
score_match = re.search(r"Score:\s*([\d.]+)", raw_text)

reasoning = reasoning_match.group(1).strip() if reasoning_match else "No reasoning found."
score = float(score_match.group(1)) if score_match else 0.0

print(type(reasoning), type(score))
print(reasoning, score)