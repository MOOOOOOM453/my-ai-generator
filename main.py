import openai 
import gradio as gr 

openai.api_key = "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" 

def chat_with_gpt(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # можно заменить на gpt-4, если есть доступ
    messages=[{"role": "user", "content": prompt}]
  )
  return response.choices[0].message.content
  
  iface = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(lines=2, label="Спроси что угодно"),
    outputs=gr.Textbox(label="Ответ от ИИ"),
    title="Мой ИИ чат"
  )
  
  
  iface.launch()
