from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

print("Image Caption Generator")

image_path = input("Enter image path: ")

image = Image.open(image_path)

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

inputs = processor(images=image, return_tensors="pt")

output = model.generate(**inputs, max_length=30)

caption = processor.decode(output[0], skip_special_tokens=True)

print("Generated Caption:", caption)