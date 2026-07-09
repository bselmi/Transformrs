from transformers import pipeline

print("Loading model... (this may take a few minutes the first time)")

generator = pipeline(
    task="text-generation",
    model="Qwen/Qwen2.5-1.5B"
)

print("Model loaded successfully!\n")

prompt = input("Enter your prompt: ")

result = generator(
    prompt,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7
)

print("\nResponse:\n")
print(result[0]["generated_text"])
