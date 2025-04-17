# --- Part 3: Prediction, Mark Attended, and Export Functions ---

def predict(name, age, health_id, symptoms_input):
    if not name or not symptoms_input:
        return "❌ Please enter name and symptoms.", "", "", None, pd.DataFrame(), gr.update(choices=[]), None, None
    disease = gpt4o_predict(symptoms_input)
    risk_level = ai_assess_risk(symptoms_input, disease, age)
    note = "⚠️ Doctor should confirm the final diagnosis."
    patient_data = {
        "Name": name,
        "Age": age,
        "Health ID": health_id,
        "Symptoms": symptoms_input,
        "Disease": disease,
        "Risk": risk_level,
        "Note": note
    }
    patient_records.append(patient_data)
    df = pd.DataFrame(patient_records)
    dropdown_options = get_patient_options()
    return (
        f"🧠 Final Predicted Disease: {disease}", note, risk_level,
        plot_risk_distribution(), df, gr.update(choices=dropdown_options),
        None, None
    )

def mark_as_attended(selected_option):
    try:
        if not selected_option:
            return gr.update(choices=get_patient_options()), pd.DataFrame(), plot_risk_distribution()
        index = int(selected_option.split(":")[0]) - 1
        if 0 <= index < len(patient_records):
            del patient_records[index]
        df = pd.DataFrame(patient_records)
        return gr.update(choices=get_patient_options(), value=None), df, plot_risk_distribution()
    except:
        return gr.update(choices=get_patient_options(), value=None), pd.DataFrame(), plot_risk_distribution()

def export_csv():
    df = pd.DataFrame(patient_records)
    path = "/tmp/patient_data.csv"
    df.to_csv(path, index=False)
    return path

def export_encrypted_csv():
    df = pd.DataFrame(patient_records)
    path = "/tmp/encrypted_patient_data.csv"
    encrypted_content = fernet.encrypt(df.to_csv(index=False).encode())
    with open(path, "wb") as f:
        f.write(encrypted_content)
    return path