import pyqrcode
url=input("url giriniz: ")
qr_code=pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=5)