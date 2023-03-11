import easyocr
import cv2

receiverRect = (180, 370, 247, 80)
addressRect = (72, 447, 436, 123)

def box(image, rect):
    x, y, w, h = rect
    return image[y:y+h, x:x+w]

def parseLabel():
    image = cv2.imread('shipping-label-example.jpeg')

    addrBox = box(image, addressRect)
    receiverBox = box(image, receiverRect)

    cv2.imwrite('rect_addr.png', addrBox)
    cv2.imwrite('rect_receiver.png', receiverBox)

    reader = easyocr.Reader(['id'], gpu=False, verbose=True)
    text_addr = reader.readtext(addrBox, detail = 0)
    text_receiver = reader.readtext(receiverBox, detail = 0)

    address = (" ".join(text_addr))
    return {
        "shipping_name": text_receiver[0],
        "shipping_address": address,
        "shipping_phone": text_receiver[-1]
    }

if __name__ == '__main__':
    label = parseLabel()
    print(f"result: {label}\n")
    print(f"Receiver : {label['shipping_name']}")
    print(f"Phone : {label['shipping_phone']}")
    print(f"Address : {label['shipping_address']}")