# --- Part 4: Gradio GUI ---

with gr.Blocks() as demo:
    gr.Markdown("## 🧪 Smart AI Triage System (GPT-4o + Whisper + Risk + CSV)")

    with gr.Row():
        name = gr.Textbox(label="Patient Name")
        age = gr.Number(label="Age", precision=0)
        health_id = gr.Textbox(label="Health ID (Optional)")

    with gr.Row():
        symptoms = gr.Textbox(label="Symptoms", placeholder="Type symptoms here...")
        with gr.Column(scale=1):
            audio_input = gr.Audio(label="🎤 Speak Symptoms", type="filepath")
            transcribe_btn = gr.Button("🎙️ Transcribe Audio")

    transcribe_btn.click(fn=transcribe_audio, inputs=[audio_input], outputs=[symptoms])

    predict_btn = gr.Button("Predict")
    disease_output = gr.Textbox(label="Disease Prediction")
    note_output = gr.Textbox(label="Note")
    risk_output = gr.Textbox(label="Risk Level")
    graph_output = gr.Plot(label="Risk Distribution")
    table_output = gr.Dataframe(label="Patient Records")

    with gr.Row():
        patient_selector = gr.Dropdown(label="Mark Patient as Attended", choices=[], interactive=True)
        mark_btn = gr.Button("Mark as Attended")

    with gr.Row():
        export_btn = gr.Button("Export CSV")
        export_enc_btn = gr.Button("Export Encrypted CSV")
        csv_file = gr.File(label="Download CSV")
        enc_file = gr.File(label="Download Encrypted CSV")

    predict_btn.click(fn=predict, inputs=[name, age, health_id, symptoms],
                      outputs=[disease_output, note_output, risk_output, graph_output,
                               table_output, patient_selector, csv_file, enc_file])

    mark_btn.click(fn=mark_as_attended, inputs=[patient_selector],
                   outputs=[patient_selector, table_output, graph_output])

    export_btn.click(fn=export_csv, outputs=[csv_file])
    export_enc_btn.click(fn=export_encrypted_csv, outputs=[enc_file])

demo.launch()