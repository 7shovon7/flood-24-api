# # pip install Pillow

# from io import BytesIO
# import sys
# from PIL import Image
# from django.core.files.uploadedfile import InMemoryUploadedFile


# def optimize_image(img, desired_height=800):
#     im = Image.open(img)
#     im_format = im.format
#     w, h = im.size
#     if h > desired_height:
#         aspect_ratio = round(w / h)
#         w = desired_height * aspect_ratio
#         h = desired_height
#     im = im.resize((w, h))
#     output = BytesIO()
    
#     # if im_format == 'JPEG':
#     #     im = im.convert('RGB')
        
#     # if im_format == 'JPEG':
#     im.save(output, format=im_format, quality=50)
#     # else:
#     #     im.save(output, format=im_format, optimize=True)
        
#     output.seek(0)
    
#     modified_file = InMemoryUploadedFile(
#         file=output,
#         field_name='ImageField',
#         name=img.name,
#         content_type=f'image/{im_format}',
#         size=sys.getsizeof(output),
#         charset=None,
#     )
    
#     return modified_file
