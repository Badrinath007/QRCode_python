import pyqrcode
import png
import webbrowser
from pyqrcode import QRCode
s="url to be embedded "
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png('myqr.png',scale=8)
