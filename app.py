import tkinter as tk
from master_cipher import MasterCypher
print('All modules imported in app')

def initialize():
    pincode = ent_keys.get()
    script = txt_text.get(1.0, tk.END)
    mode = mode_variable.get()
    wheel_num = sl_wheels.get()

    cypher = MasterCypher(script, pincode, wheel_num)
    result_cipher = cypher.write(mode)
    
    lbl_answer.delete(1.0, tk.END)
    lbl_answer.insert(1.0, result_cipher)



window = tk.Tk()
window.title('MasterCypher')

window.rowconfigure([i for i in range(10)], weight=1, minsize=150)
window.columnconfigure([i for i in range(6)], weight=1, minsize=250)
window.configure(bg='#23272a')

lbl_title = tk.Label(window, text='Key format should be {1, 2, 3, 23, 21}', font=24, relief=tk.FLAT, fg='#99aab5' ,bd=7, bg='#2c2a41')
lbl_title.grid(row=0, column=0, columnspan=5, sticky='ew', padx=25, pady=25)


lbl_wheels = tk.Label(window, text='Wheels: ', fg='#99aab5', bg='#2c2f55')
lbl_wheels.grid(row=1, column=0, sticky='ew', padx=25, pady=5)
sl_wheels = tk.Scale(window, bd=3, from_=1, to=10, orient=tk.HORIZONTAL, relief=tk.RAISED,
                     tickinterval=1, bg='#2c2f33', fg='#99aab5', activebackground='#aaaaaa',)
sl_wheels.grid(row=1, column=1,columnspan=4, sticky='ew', padx=25, pady=25)

lbl_keys = tk.Label(window, text='Keys: {eg: 1,2,3..}', fg='#99aab5',  bg='#2c2f55')
lbl_keys.grid(row=2, column=0, sticky='ew', padx=25, pady=5)
ent_keys = tk.Entry(window, text='example: 1, 2, 3, 4, 5, 6', bd=3, bg='#2c2f33', fg='#99aab5')
ent_keys.grid(row=2, column=1, columnspan=2, sticky='ew', padx=25, pady=25)

mode_variable = tk.StringVar(window)
btn_encode = tk.Radiobutton(window, text='Encode', bg='#2c2f33', fg='#99aab5', value='encode',
                            relief=tk.RAISED, bd=3, variable=mode_variable, indicator=0)
btn_encode.grid(row=2, column=3, sticky='ew')
btn_decode = tk.Radiobutton(window, text='Decode', bg='#2c2f33', fg='#99aab5',
                            relief=tk.RAISED, bd=3, value='decode', variable=mode_variable, indicator=0)
btn_decode.grid(row=2, column=4, sticky='ew')

lbl_text = tk.Label(window, text='Message: ', fg='#99aab5', bg='#2c2f55')
lbl_text.grid(row=3, column=0, sticky='ew', padx=25, pady= 5, ipadx=5, ipady=5)
txt_text = tk.Text(window, bg='#2c2f33', bd=7, fg='#99aab5', relief=tk.SUNKEN)
txt_text.grid(row=3, column=1, columnspan=3, sticky='nsew', padx=25, pady=25)
btn_cypher = tk.Button(window, text='Cypher!', bg='#2c2f33', fg='#99aab5', bd=3,command=initialize)
btn_cypher.grid(row=3, column=4, sticky='ew', padx=25, pady=25)
btn_cypher.bind('<Button-2>', initialize)

lbl_cipher = tk.Label(window, text='Answer: ', fg='#99aab5', bg='#2c2f55')
lbl_cipher.grid(row=4, column=0, sticky='ew', padx=25, pady=25)

lbl_answer = tk.Text(window, fg='#99aab5', bg='#2c2f33', bd=7, font=24, relief=tk.SUNKEN)
lbl_answer.grid(row=4, column=1, columnspan=4, sticky='nsew', padx=25, pady=25)



window.mainloop()
