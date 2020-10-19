import tkinter as tk
root = tk.Tk()
root.geometry('1280x800')
root.configure(background="Orange")
# use opacity alpha values from 0.0 to 1.0
# opacity/tranparency applies to image and frame
root.wm_attributes("-transparentcolor") 
# use a GIF image you have in the working directory
# or give full path
photo = tk.PhotoImage(file="2.gif")
tk.Button(root, image=photo).pack()
root.mainloop()