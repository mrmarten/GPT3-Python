import os
import openai
openai.organization = "org-"
openai.api_key = "sk-"
pres = openai.Engine("davinci").search(
  documents=["White House", "hospital", "school"],
  query="the president"
)
print(pres)