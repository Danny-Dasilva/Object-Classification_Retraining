from PIL import Image
import io

im = Image.open('index.jpeg')
im_resize = im.resize((500, 500))
buf = io.BytesIO()
im_resize.save(buf, format='JPEG')
byte_im = buf.getvalue()
print(byte_im)