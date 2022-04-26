from tkinter import *

font_size = ("Arial", 12, "bold")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=20)
label_1 = Label(text="miles", font=font_size)
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=font_size)
label_2.grid(column=0, row=1)

label_3 = Label(text="km", font=font_size)
label_3.grid(column=2, row=1)

label_4 = Label(text=0, font=font_size)
label_4.grid(column=1, row=1)

miles_input = Entry(width=5, font=("10"))
miles_input.grid(column=1, row=0)

def calculate_km():
    answer = 0
    miles = miles_input.get()
    total = round(float(miles) * 1.609, 1)
    answer += total
    label_4.config(text=answer)

calculate_button = Button(text="Calculate", command= calculate_km, font=("10"))
calculate_button.grid(column=1, row=2)

window.mainloop()
