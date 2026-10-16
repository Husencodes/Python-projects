import qrcode

#taking UPI id as a input

UPI_id=input("Enter your UPI ID = ")

#upi:pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=massege
#you can modify the URLs based on payment app

phonepe_url=f'upi://pay?pa={UPI_id}&pn=Recipent%20Name&mc=1234'
paytm_url=f'upi://pay?pa={UPI_id}&pn=Recipent%20Name&mc=1234'
gpay_url=f'upi://pay?pa={UPI_id}&pn=Recipent%20Name&mc=1234'

#Creating qr code

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
gpay_qr=qrcode.make(gpay_url)

# save the QR code to image file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
gpay_qr.save('gpay_qr.png')

#Display the qr codes using Pillow library
phonepe_qr.show()
paytm_qr.show()
gpay_qr.show()