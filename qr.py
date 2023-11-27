#Before compiling and executing the below code, Don't forget to install the required packages using pip command.

import pyqrcode #importing pyqrcode,png,webbrowser
import png
import webbrowser
from pyqrcode import QRCode
s="url to be embedded " #The url is stored in the variable s
url=pyqrcode.create(s)
url.svg("myqr.svg",scale=8)
url.png('myqr.png',scale=8)
