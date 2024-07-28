from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def convert_image_size(image_file,w_ratio,h_ratio):
    with Image.open(image_file) as img:
        # Original dimensions
        original_width, original_height = img.size
        
        # Desired aspect ratio
        target_aspect_ratio = w_ratio / h_ratio
        
        # Calculate new dimensions
        original_aspect_ratio = original_width / original_height
        if original_aspect_ratio > target_aspect_ratio:
            # Width needs to be cropped
            new_width = int(original_height * target_aspect_ratio)
            new_height = original_height
            crop_width = (original_width - new_width) // 2
            crop_height = 0
        else:
            # Height needs to be cropped
            new_width = original_width
            new_height = int(original_width / target_aspect_ratio)
            crop_width = 0
            crop_height = (original_height - new_height) // 2

        # Crop and resize
        img_cropped = img.crop((crop_width, crop_height, crop_width + new_width, crop_height + new_height))
        img_resized = img_cropped.resize((new_width, new_height), Image.LANCZOS)
        
        # Save the image to a BytesIO object
        img_io = BytesIO()
        img_resized.save(img_io, format='JPEG')
        img_io.seek(0)
        
        # Create a new InMemoryUploadedFile object
        converted_image_file = InMemoryUploadedFile(
            img_io,
            None,
            f"product_{image_file.name}",
            'image/jpeg',
            img_io.tell(),
            None
        )
        
        return converted_image_file