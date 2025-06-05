# brew install tcl-tk
# export TK_SILENCE_DEPRECATION=1 ----- tarminal e export korta hobe
# pip install googletrans==4.0.0-rc1
#pyenv install 3.11.9
# pyenv global 3.11.9
from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


root = Tk()
root.title("Google Translator by Sazidul islam") # Set on title
root.geometry("650x300") # Set on window size
# root.config(bg="gray")

# lab_tx= Label(root, text="Google Translator", font=("Arial", 20, "bold"), bg="green", fg="white")
# lab_tx.place(x=200, y=10, width=250, height=50)

frame =Frame(root).pack(side=BOTTOM)

sort_txt=Text(frame, font=("inter", 20,"bold"), bg="green", fg="black",wrap=WORD)
sort_txt.place(x=10, y=40, width=630, height=100)

list_text= list(LANGUAGES.values())

comb_sor =ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10, y=10, width=100, height=30)
comb_sor.set("English")

button_change = Button(frame, text="Translate", relief=RAISED, command=translate_text)
button_change.place(x=200,y=10,width=100,height=30)

comb_dest =ttk.Combobox(frame,value=list_text)
comb_dest.place(x=400, y=10, width=100, height=30)
comb_dest.set("Bangla")

dest_txt=Text(frame, font=("inter",20,"bold"), bg="green",fg="black",wrap=WORD)
dest_txt.place(x=10, y=150, width=630, height=100)

def translate_text():
    try:
        src_lang = comb_sor.get().lower()
        dest_lang = comb_dest.get().lower()
        text_to_translate = sort_txt.get(1.0, END).strip()
        if text_to_translate:
            translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text_to_translate)
            dest_txt.delete(1.0, END)
            dest_txt.insert(END, translated)
    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, f"Error: {str(e)}")



root.mainloop()