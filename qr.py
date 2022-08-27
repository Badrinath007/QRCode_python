import pyqrcode
import png
import webbrowser
from pyqrcode import QRCode
s="https://www.linkedin.com/in/badrinath- ayyamperumal-1b676a19b/ "
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png('myqr.png',scale=8)
