import pyperclip
import qrcode

def generate_qr_from_clipboard():
    clipboard_content = pyperclip.paste()

    if clipboard_content:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=3,
        )
        qr.add_data(clipboard_content)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.show()
    else:
        exit("Zwischenablage ist leer!")

if __name__ == "__main__":
    generate_qr_from_clipboard()
