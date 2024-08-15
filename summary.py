from transformers import PegasusForConditionalGeneration, PegasusTokenizer


def generate_summary(text):
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-multi_news")
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-multi_news")

    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

    # Move tensors to the same device as the model
    device = model.device
    tokens = {k: v.to(device) for k, v in tokens.items()}

    # Generate summary
    summary_ids = model.generate(
        **tokens,
        max_length=150,  # Adjust as needed
        min_length=50,  # Adjust as needed
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    # Decode summary
    decoded_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return decoded_summary
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


text = read_file("transcription.txt")
summary = generate_summary(text)
print(summary)