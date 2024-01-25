import tkinter
import requests
import platform
host_windows = r"C:\Windows\System32\drivers\etc\hosts"
host_linux = r"/etc/hosts"
root = tkinter.Tk()
label = tkinter.Label(root, text = "服务器地址：")
link = tkinter.Entry(root)
label1 = tkinter.Label(root, text = "要获取的域名：")
add = tkinter.Entry(root)
var = tkinter.StringVar()
label2 = tkinter.Label(root, textvariable = var)
def callback():
    params = {
        'get': add.get()
    }
    res = requests.get(link.get(), params = params)
    if res.status_code == 200:
        if platform.system() == 'Windows':
            with open(host_windows, 'a+') as f:
                f.write(res.text)
        else:
            with open(host_linux, 'a+') as f:
                f.write(res.text)
        var.set('添加成功！')
    else:
        var.set(res.text)
button = tkinter.Button(root, text = " 添加 ", command = callback, fg = "green")
label.pack()
link.pack()
label1.pack()
add.pack()
button.pack(side = tkinter.TOP)
label2.pack()
root.mainloop()