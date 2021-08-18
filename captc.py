#Created by NSIS

###Libraries###
import string
import random
from PIL.Image import Image
from captcha.image import ImageCaptcha

###Captcha Length###
S = 8

###Random Strings Creator###
x = "".join(random.choices(string.ascii_uppercase + string.digits, k=S))

###Image Width and Height###
image = ImageCaptcha(width=250, height=110)
captcha_text = x

###Image Location###
data = image.generate(captcha_text)
image.write(captcha_text, "CAPTCHA.png")
