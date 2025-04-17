# --- Part 2: AI and Risk Functions ---

def gpt4o_predict(symptoms_text):
    try:
        prompt = f"You are a medical assistant. Based on the symptoms provided, give the most likely disease.\nSymptoms: {symptoms_text}\nRespond only with the disease name."
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are a helpful medical assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except:
        return "Error"

def ai_assess_risk(symptoms_text, disease, age):
    if disease.lower() in ["common cold", "cold", "mild allergy"]:
        return "Low"
    prompt = f"Given the patient's age and symptoms, classify the risk as High, Medium, or Low.\nAge: {age}\nSymptoms: {symptoms_text}\nDisease: {disease}\nRespond with only one word: High, Medium, or Low."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are a triage assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.3,
        )
        risk = response.choices[0].message.content.strip().capitalize()
        return risk if risk in ["High", "Medium", "Low"] else "Medium"
    except:
        return "Medium"

def plot_risk_distribution():
    df = pd.DataFrame(patient_records)
    risk_counts = df['Risk'].value_counts()
    colors = {'High': 'red', 'Medium': 'blue', 'Low': 'green'}
    bar_colors = [colors.get(risk, 'gray') for risk in risk_counts.index]
    plt.figure(figsize=(5, 3))
    bars = plt.bar(risk_counts.index, risk_counts.values, color=bar_colors)
    plt.title("Risk Level Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Patients")
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.1, yval + 0.1, int(yval))
    plt.tight_layout()
    return plt

def get_patient_options():
    return [f"{i+1}: {p['Name']}" for i, p in enumerate(patient_records)]

def transcribe_audio(file):
    if file is None:
        return ""
    result = model.transcribe(file)
    return result['text']