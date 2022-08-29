import tkinter
window = tkinter.Tk()
click_count = 0
button = tkinter.Button(window, fg='blue', highlightbackground='wheat', text="Press for more RAM!", width=90, font=('Arial', 50))
button.pack(padx=10, pady=10)

def on_click(event):
    global click_count
    click_count +=1
    if click_count == 1:
        button.configure(text="HaHa! You fell for it! Now press for more RAM!", fg='red', highlightbackground='yellow')
    elif click_count == 2:
        button.configure(text="My god! You fell for it again! You know what, if you press again, no more free RAM!", fg='indigo', highlightbackground='lime green', font = ('Arial', 30))
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", on_click)
window.mainloop()
