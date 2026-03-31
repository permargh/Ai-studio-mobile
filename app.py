import os
import gradio as gr

def greet(name):
    return f"Hello {name}! Welcome to AI Studio Mobile"

def process_input(text):
    return f"Processed: {text}"

# Create Gradio interface
with gr.Blocks(title="AI Studio Mobile") as demo:
    gr.Markdown("# AI Studio Mobile Application")
    
    with gr.Tab("Greeting"):
        name_input = gr.Textbox(label="Enter your name")
        greet_btn = gr.Button("Greet")
        greet_output = gr.Textbox(label="Response")
        greet_btn.click(greet, inputs=name_input, outputs=greet_output)
    
    with gr.Tab("Process"):
        text_input = gr.Textbox(label="Enter text")
        process_btn = gr.Button("Process")
        process_output = gr.Textbox(label="Result")
        process_btn.click(process_input, inputs=text_input, outputs=process_output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)