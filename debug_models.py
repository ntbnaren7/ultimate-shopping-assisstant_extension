import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBXVgxeol8dEtLsIlH_B_umVG7ha2oWJqA")

print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error listing models: {e}")
