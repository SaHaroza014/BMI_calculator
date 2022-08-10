import tkinter
import pandas

file = pandas.read_csv('BMI_list.csv')
new_dict = file.bmi.to_dict()

calculator = tkinter.Tk()
calculator.title('Body Mass Index calculator')
calculator.config(height=150, width=150)
calculator.config(padx=20, pady=20)

# 'Enter Your Mass' label
mass_label = tkinter.Label(text='Enter your mass: ')
mass_label.grid(row=0, column=0)

# Mass entry
mass_entry = tkinter.Entry()
mass_entry.grid(row=0, column=1)
mass_entry.config(width=10)

# kg label
mass_kg_label = tkinter.Label(text='kg')
mass_kg_label.grid(row=0, column=2)

# 'Enter your height' label
height_label = tkinter.Label(text='Enter your height: ')
height_label.grid(row=1, column=0)

# height_entry
height_entry = tkinter.Entry()
height_entry.grid(row=1, column=1)
height_entry.config(width=10)

# cm label
cm_label = tkinter.Label(text='cm')
cm_label.grid(row=1, column=2)

# Result Label _pre
result_bmi = tkinter.Label(text='BMI= ')
result_bmi.grid(row=3, column=0)

# result label _post
bmi = tkinter.Label(text='0')
bmi.grid(row=3, column=1)

# comment bmi
comment_bmi = tkinter.Label(text='')
comment_bmi.grid(row=5, column=0)


# button Calculate BMI
def calculate():
    mass = float(mass_entry.get())
    height = float(height_entry.get())
    height /= 100
    height *= height
    final_m_h = mass / height
    if final_m_h < 16:
        comment_bmi.config(text=new_dict[0], font=("Calibre", 14, 'bold'))
    elif 16 <= final_m_h <= 17:
        comment_bmi.config(text=new_dict[1], font=("Calibre", 14, 'bold'))
    elif 17 < final_m_h <= 18.5:
        comment_bmi.config(text=new_dict[2], font=("Calibre", 14, 'bold'))
    elif 18.5 < final_m_h <= 25:
        comment_bmi.config(text=new_dict[3], font=("Calibre", 14, 'bold'))
    elif 25 < final_m_h <= 30:
        comment_bmi.config(text=new_dict[4], font=("Calibre", 14, 'bold'))
    elif 30 < final_m_h <= 35:
        comment_bmi.config(text=new_dict[5], font=("Calibre", 14, 'bold'))
    elif 35 < final_m_h <= 40:
        comment_bmi.config(text=new_dict[6], font=("Calibre", 14, 'bold'))
    else:
        comment_bmi.config(text=new_dict[7], font=("Calibre", 14, 'bold'))

    bmi.config(text=round(final_m_h, 1))


calculate_button = tkinter.Button(text='Calculate', command=calculate)
calculate_button.grid(row=4, column=1)

calculator.mainloop()
