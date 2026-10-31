import pyqrcode

url= input("Enter url here")
qrcode= pyqrcode.create(url)
qrcode.png('qrcode.png',scale=100)