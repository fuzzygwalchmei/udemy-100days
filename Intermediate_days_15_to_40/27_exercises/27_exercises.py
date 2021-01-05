import tkinter as tk

window = tk.Tk()
window.title("My App")
window.config(padx=10, pady=10)

# label_1 = tk.Label(text="This is Label 1", font=("Arial",24,"italic"))
# label_1.grid(row=0, column=0)

# def clicked():
#     label_1.config(text=input_1.get())

# button_1 = tk.Button(text = "Click Me", command = clicked)
# button_1.grid(row=1, column=1)


# input_1 = tk.Entry()
# input_1.grid(row=0, column=2)

# input_2 = tk.Text()
# input_2.grid(row=2, column=3)

def calc():
    km_calc_labal.config(text=int(miles_entry.get())*1.6)

miles_entry = tk.Entry()
miles_entry.grid(row=0, column=1)
miles_label = tk.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
km_calc_labal = tk.Label()
km_calc_labal.grid(row=1, column=1)
km_label = tk.Label(text="Km")
km_label.grid(row=1, column=2)
calc_button = tk.Button(text="Calculate", command=calc)
calc_button.grid(row=2, column=1)

window.mainloop()

