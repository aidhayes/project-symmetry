from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    # Create a translation client
    client = translate.Client()

    # Translate the text
    result = client.translate(text, target_language=target_language)

    return result["input"], result["translatedText"]

# Example usage
text_to_translate = "Hello, how are you?"
target_language = "fr"  # Replace with your target language code

input_text, translated_text = translate_text(text_to_translate, target_language)
print(f"Input: {input_text}")
print(f"Translation: {translated_text}")
