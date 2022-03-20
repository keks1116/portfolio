from importlib.resources import path
from sys import float_repr_style
import tkinter
import tkinter.ttk as ttk
from tkinter import filedialog
from pathlib import Path

before=''
def directory_serect():
    file_path=tkinter.filedialog.askdirectory()
    
    global filepath
    filepath=str(file_path)+"/"
    
    input_box.insert(tkinter.END,file_path)
    
def nameChange():
    for f in Path(filepath).rglob(combobox.get()):
        f.rename(filepath+f.stem+combobox2.get())
        
# ウインドウの作成
root = tkinter.Tk()
root.title("Python GUI")
root.geometry("360x240")

# ラベルの作成
input_label = tkinter.Label(text="変更するフォルダorファイル")
input_label.place(x=10, y=20)

# 入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=40)

# ボタンの作成
button = tkinter.Button(text="参照",command=directory_serect)
button.place(x=260, y=36)


# ラベルの作成
input_label2 = tkinter.Label(text="変更するファイル拡張子")
input_label2.place(x=10, y=65)

module = ['.txt', '.png', '.JPEG', "*"]
combobox = ttk.Combobox(root, height=4, width=15, values=module)
combobox.bind(
    nameChange,
)
combobox.place(x=10, y=85)

# ラベルの作成
input_label3 = tkinter.Label(text="変更後のファイル拡張子")
input_label3.place(x=150, y=65)

module = ['.txt', '.png', '.JPEG']
combobox2 = ttk.Combobox(root, height=3, width=15, values=module)
combobox2.bind(
    nameChange,
)
after = str(combobox2)
combobox2.place(x=150, y=85)

# ボタンの作成
button = tkinter.Button(text="実行",command=nameChange)
button.place(x=270, y=85)

# ウインドウの描画
root.mainloop()