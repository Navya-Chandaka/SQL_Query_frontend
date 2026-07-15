import gradio as gr
import requests

backend_url = "https://sql-query-backend-1.onrender.com"

def generate_sql(question):

    response = requests.post(
        backend_url,
        json={"question": question}
    )

    if response.status_code == 200:
        return response.json()["sql"]
    else:
        return "Error connecting to backend."

demo = gr.Interface(
    fn=generate_sql,
    inputs=gr.Textbox(
        label="Enter English Description",
        placeholder="Example: Show all students from CSE with marks above 80",
        lines=4
    ),
    outputs=gr.Textbox(
        label="Generated SQL Query",
        lines=8
    ),
    title="AI SQL Query Generator"
)

demo.launch()