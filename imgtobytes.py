from PIL import Image
import io

im = Image.open('test.png')
im_resize = im.resize((500, 500))
buf = io.BytesIO()
im.save(buf, format='PNG')
byte_im = buf.getvalue()
print(len(byte_im))


from PIL import Image
import io
print(len(byte_im))
stream = io.BytesIO(byte_im)
img = Image.open(stream)
img.save("a_test.png")