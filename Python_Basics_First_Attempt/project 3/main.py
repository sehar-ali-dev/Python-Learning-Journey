# tect editor app mtlb k note pad bnana h 
# tkinter module and liberary
# module means single python file 
# liberary means  is a collection of  modules etc
# tkinter means both a liberary and modeules
# import tikinter  for creating GUI apps
# GUI means grapical user interface
import tkinter as tk


from tkinter import filedialog, messagebox
# main window code
root= tk.Tk()
root.title("text editor")
root.geometry("800x600")
# creat text area
text= tk.Text(
    root,
    wrap=tk.WORD,
    font= ("Helvetica", 18)
    )
text.pack(expand=True,fill=tk.BOTH)


# ab main logic ho ga shuru 

# Function 1 - to creat a new file
def new_file():
    text.delete(1.0, tk.END)
# function 2 - to open a new file
def open_file():
    # open file dilogue
    file_Path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_Path:
        # open selected file
        with open(file_Path, "r") as file:
            # clear old text
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
# function 3  save the file
def save_file():
    # open save file dialoge
    file_Path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text File", "*.txt")] # *.text ko *.txt kiya taake standard file bane
    )
    if file_Path:
        with open(file_Path, "w") as file:
            file.write(text.get(1.0, tk.END))
    
    messagebox.showinfo("Info", "File save successfully")
    # menu
menu= tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)
# new, openfile,save, exit
# add file menu to menubar
menu.add_cascade(label="file", menu=file_menu)



file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)





# jb bhi tikinter apps GUI ki madad sy bna ry hon gay tw ye line lazmi likhni h 
# starts and keeps the window open

root.mainloop()