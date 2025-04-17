# --- Part 1: Imports, Model Load, and Encryption Setup ---
import gradio as gr
import openai
import pickle
import json
import pandas as pd
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet
import whisper

openai.api_key = "openaikey"  # Replace with your key
model = whisper.load_model("base")

# Load ML Model
with open("symptom_disease_model.pkl", "rb") as f:
    clf = pickle.load(f)

with open("symptom_names.json", "r") as f:
    symptom_names = json.load(f)

# Encryption Setup
fernet_key = Fernet.generate_key()
fernet = Fernet(fernet_key)

# Data Store
patient_records = []