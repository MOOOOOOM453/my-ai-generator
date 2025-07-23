import openai 
import gradio as gr 

openai.api_key = "вставь_сюда_свой_API_ключ" 

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
