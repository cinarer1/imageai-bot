import requests
import requests
url = 'https://github.com/OlafenwaMoses/ImageAT/releases/download/3.0.0-pretrained/yolov3.pt'
r = requests.get(url,allow_redirects=True)
open ('yolov3.pt', 'wb') .write(r.content)