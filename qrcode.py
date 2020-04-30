# python code for the quick response code generation
# For this you should have installed qrcode module in python [ pip install qrcode ] --> Windows

import qrcode

code_input = "https://example.com  (or) some of the data you wanna give to qr code " #This statement is to store the data in the qrcode 
code.qrcode(code_input)  # this is to call the data that u have given to the input
code.save("Example.png") # it'll save as an image file to put output for us
code.show() # to print the output

