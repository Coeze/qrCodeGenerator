from tkinter import *
import qrcode

window = Tk()
window.config(width=600, height=600, bg="blue")
window.resizable(False, False)
window.title("QR Code Generator")

name = Entry(width=50)
name.insert(END, "New File")
name.place(x=180, y=100)

link = Entry(width=50)
link.insert(END, "Enter URL")
link.place(x=180, y=150)


def generate_qr():
    file_name = name.get()
    qr_link = link.get()
    code = qrcode.make(qr_link)
    code.save(f"{file_name}.png")

    code_image = PhotoImage(file=f"{file_name}.png")
    displayCode.config(image=code_image)

displayCode = Label(window)
displayCode.place(x=200, y=250)
displayCode.config(bg="blue")


generate = Button(width=25, text="Generate", bg="#e0fbfc", command=generate_qr)
generate.place(x=225, y=200)


window.mainloop()