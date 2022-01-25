import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
import time
import threading

class Application(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        
        self.master.geometry("550x150")
        self.master.title("youtubeDL")
        self.widget()
        self.pack()

    def widget(self):

        self.text = ttk.Label(self, text='youtube URL')
        self.inpu = ttk.Entry(self, width=60)
        self.label = ttk.Label(self, text='')
        self.but = ttk.Button(self, text='実行', command=self._start_thread)
        # self.but = ttk.Button(self, text='実行', command=lambda:self.dl(self.inpu.get(), self.label))
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=286, mode = 'determinate')
        self.progress_bar.grid(column=1, row=3, padx=20, pady=12, sticky=tk.W + tk.E)

        self.text.grid(row=0, column=0, pady=3, padx=3)
        self.inpu.grid(row=0, column=1, pady=3, padx=3)
        self.but.grid(row=1, column=1, pady=3, padx=3)
        self.label.grid(row=2, column=1, pady=3, padx=3)
    
    def dl(self, url, label):
        # print(url)
        try:
            y_url = url
            yt = YouTube(y_url)
            label['text'] = "ダウンロードに5~10分かかる場合があります"
            yt.streams.filter(progressive=True, subtype='mp4').get_highest_resolution().download()

            self.progress_bar["maximum"] = 100

            for i in range(101):
                time.sleep(0.05)
                self.progress_bar["value"] = i
                self.progress_bar.update()
            self.progress_bar["value"] = 0
            self.progress_bar.update()

            label['text'] = "ダウンロード完了"
        except:
            messagebox.showerror('url error', 'youtube動画ではありませんでした。')
        time.sleep(3)
        label['text'] = ""
        self.inpu.delete(0, tk.END)


    def _start_thread(self):
        # self.thread_main = threading.Thread(target = self.dl)
        self.thread_main = threading.Thread(target = self._main_func)
        self.thread_main.start()
        print(self.thread_main)

    def _main_func(self):
        self.dl(self.inpu.get(), self.label)

def main():
    root = tk.Tk()
    app = Application(master=root)#Inheritクラスの継承！
    app.mainloop()

if __name__ == "__main__":
    main()
    
# © 2020 massao000