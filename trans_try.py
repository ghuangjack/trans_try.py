from google.cloud import vision
from google.cloud import translate_v2 as translate
from PIL import Image

# Set Google Cloud API credentials environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'my_API' #the 'my_API' is my API key

# Initialize Google Cloud Vision and Translate clients
vision_client = vision.ImageAnnotatorClient()
translate_client = translate.Client()

def detect_and_translate_text(image_path, target_language='zh-TW'):
    # Read image file
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Perform text detection using Google Cloud Vision API
    image = vision.Image(content=content)
    response = vision_client.text_detection(image=image, image_context={"language_hints": ["ja"]})
    texts = response.text_annotations

    if texts:
        # Extract detected text
        detected_text = texts[0].description

        # Translate text to target language using Google Cloud Translation API
        translation = translate_client.translate(detected_text, target_language=target_language)

        return translation['translatedText']
    else:
        return None

def translate_and_save_image(input_folder, output_folder, target_language='zh-TW'):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # Detect and translate text in image
                translated_text = detect_and_translate_text(input_path, target_language=target_language)

                if translated_text:
                    # Create blank image with translated text
                    translated_img = Image.new('RGB', (1, 1), color='white')
                    translated_img.save(output_path)
                    print(f'Translated and saved: {filename}')
                else:
                    print(f'No text detected in {filename}')
            except Exception as e:
                print(f'Error processing {filename}: {e}')

# Specify input and output folders
input_folder = 'C://input_folder'
output_folder = 'C://output_folder'

# Call the function to translate and save images
translate_and_save_image(input_folder, output_folder)
