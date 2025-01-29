from transformers import pipeline

pipe = pipeline("text-generation", model="varma007ut/Indian_Legal_Assitant")

prompt = "Summarize the key points of the Indian Contract Act, 1872:"
result = pipe(prompt, max_length=200)
print(result[0]['generated_text'])
