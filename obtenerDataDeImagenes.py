from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open('./Assets/EjercicioDatos.png')

# comprobar que la imagen se abra correctamente
# img.show()

# convertir la imagen a texto
text = pytesseract.image_to_string(img)

print(text)