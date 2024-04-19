import os
from google.cloud import translate_v2 as translate

def upload_and_translate(input_dir, output_dir, source_language, target_language, api_key):
    # Set up Google Translate client with API key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_key
    client = translate.Client()

    # Get a list of all the files in the input directory
    files = os.listdir(input_dir)

    # Iterate over the files and upload them to Google Translate
    for file in files:
        with open(os.path.join(input_dir, file), "rb") as f:
            # Upload the image to Google Translate
            response = client.translate_image(
                f,
                source_language=source_language,
                target_language=target_language,
            )

            # Download the translated image
            with open(os.path.join(output_dir, file), "wb") as f:
                f.write(response.translated_image)

# Example usage
if __name__ == "__main__":
    input_dir = "C:/Users/ghuan/Downloads/RJ01156500-1-compressed (1)"
    output_dir = "C:/Users/ghuan/Downloads/RJ01156500-1-compressed"
    source_language = "ja"  # Japanese
    target_language = "zh-TW"  # Traditional Chinese
    api_key = "AIzaSyAqkCzH5tDSeYxx6LdzG2ntIUaQyvXJWeM"  # Replace with your actual API key
    upload_and_translate(input_dir, output_dir, source_language, target_language, api_key)
