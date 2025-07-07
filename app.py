import gradio as gr
from db import insert_data, fetch_data
from logic import analyze_behavior, calculate_risk_score, calculate_premium, generate_feedback
import pandas as pd

def process_inputs(driver_id, speed, acceleration, braking, distance):
    behavior = analyze_behavior(speed, acceleration, braking)
    risk = calculate_risk_score(behavior)
    premium = calculate_premium(risk)
    feedback = generate_feedback(risk)

    insert_data(driver_id, speed, acceleration, braking, distance, behavior, risk, premium, feedback)

    result = {
        "Behavior Score": round(behavior, 2),
        "Risk Score": risk,
        "Premium": premium,
        "Feedback": feedback
    }
    return result

def view_data():
    data = fetch_data()
    df = pd.DataFrame(data)
    return df

with gr.Blocks() as app:
    gr.Markdown("## 🚗 Telematics-Based Usage Insurance System (Gradio + MySQL)")

    with gr.Row():
        driver_id = gr.Number(label="Driver ID", value=1)
        speed = gr.Number(label="Speed (km/h)", value=60)
        acceleration = gr.Number(label="Acceleration (m/s²)", value=2.0)
        braking = gr.Number(label="Braking (m/s²)", value=1.5)
        distance = gr.Number(label="Distance Travelled (km)", value=30)

    submit_btn = gr.Button("Submit & Analyze")
    result_output = gr.JSON(label="Result Summary")

    submit_btn.click(
        process_inputs,
        inputs=[driver_id, speed, acceleration, braking, distance],
        outputs=result_output
    )

    gr.Markdown("---")
    gr.Markdown("### 📊 View All Driver Records")

    refresh_btn = gr.Button("Refresh Table")
    table_output = gr.Dataframe()

    refresh_btn.click(fn=view_data, inputs=[], outputs=table_output)

app.launch()
