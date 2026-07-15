import gradio as gr
import requests
import os

# Your Render backend URL
BACKEND_URL = "https://sql-query-backend-1.onrender.com/generate-sql"

def generate_sql(question):
    if not question.strip():
        return "Please enter a question."

    try:
        response = requests.post(
            BACKEND_URL,
            json={"question": question},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("sql", "No SQL query returned.")

        return f"Backend Error ({response.status_code}): {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Connection Error: {str(e)}"

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
    title="AI SQL Query Generator",
    description="Enter a natural language question and generate a MySQL query using Gemini AI."
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
