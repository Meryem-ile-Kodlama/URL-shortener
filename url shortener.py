# URL shortener by Meryem ile Kodlama on YouTube

from tkinter import *
import pyshorteners #pip install pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(longurl_e.get())
    shorturl_o.insert(0, short_url)

root = Tk()
root.title("URL shortener")
root.geometry("300x150")

longurl_l = Label(root, text="Enter long URL")
longurl_e = Entry(root)
shorturl_l = Label(root, text="Shortened URL")
shorturl_o = Entry(root)
shorten_b = Button(root, text="Shorten URL", command=shorten)

longurl_l.pack()
longurl_e.pack()
shorturl_l.pack()
shorturl_o.pack()
shorten_b.pack(pady=20)

root.mainloop()