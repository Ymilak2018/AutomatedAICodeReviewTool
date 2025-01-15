import google.generativeai as genai

genai.configure(api_key='AIzaSyAwHv8up0f33lyJCR5JsxLOz3sFE5l0Vgo')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="This is an Automated AI Code Review Tool , here whatever the code will be posted , verify and review it and provide a better solution if required or asked or else just encourage the fellow programmer ",
)


def ChatBotResponse(message):
  chat_session = model.start_chat(
    history=[]
  )

  response = chat_session.send_message(message)

  model_res = response.text

  return f'{model_res}'





