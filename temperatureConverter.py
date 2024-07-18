import tkinter as tk

bg_color = '#f0f8ff'  
entry_bg_color = '#ffffff'  
radio_fg_color = '#e0f7fa'  
button_bg_color = '#e6e6fa'  
result_color = '#00796b'  


root = tk.Tk()
root.title('Temperature Converter')
root.geometry('500x500')
root.resizable(0, 0)
root.config(bg=bg_color)

vars = tk.IntVar()

def convert():
    temperature = float(entry.get())

    if vars.get() == 1:
        converted_temp = (temperature * 9/5) + 32
        result_label.config(text=f"{converted_temp:.2f} °F")

    elif vars.get() == 2:
        converted_temp = (temperature - 32) * 5/9
        result_label.config(text=f"{converted_temp:.2f} °C")


main_label = tk.Label(root, text='Temperature Converter', font=('Helvetica', 18, 'bold'))
main_label.pack(pady=20)

entry_label = tk.Label(root, text='Enter Temperature', font=('Helvetica', 14, 'bold'), bg=bg_color)
entry_label.pack()

entry = tk.Entry(root, font=('Helvetica', 14))
entry.pack(pady=15)

# Create a frame for radio buttons
frame = tk.Frame(root, bg=bg_color)
frame.pack(pady=15)

c_to_f = tk.Radiobutton(frame, text='Celsius to Fahrenheit', variable=vars, value=1, font=('Helvetica', 12), bg=bg_color, activeforeground=radio_fg_color)
c_to_f.grid(row=0, column=0)

f_to_c = tk.Radiobutton(frame, text='Fahrenheit to Celsius', variable=vars, value=2, font=('Helvetica', 12), bg=bg_color, activeforeground=radio_fg_color)
f_to_c.grid(row=1, column=0)

convert_button = tk.Button(root, text='Convert', font=('Helvetica', 14), bg=bg_color, command=convert)
convert_button.pack()

result_label = tk.Label(root, text="", font=('Helvetica', 18, 'bold'), bg=bg_color, fg=result_color)
result_label.pack(pady=14)

root.mainloop()
