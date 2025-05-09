import cv2
import io
from PIL import Image

def convert_to_bytes(img):
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    with io.BytesIO() as output:
        img.save(output, format="PNG")
        return output.getvalue()
