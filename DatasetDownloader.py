#Note: The Dataset taken from the simple_image library is usually best used to identify popular people / subjects only
from simple_image_download import simple_image_download as smp

response = smp.simple_image_download

keywords = ["hello hand sign", "hi hand sign", "yes hand sign", "no hand sign", "thanks hand sign", "thank you hand sign", "i love you hand sign"]

for kw in keywords:
    response().download(kw, 100)