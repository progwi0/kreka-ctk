from customtkinter import *
from tkinter import messagebox as dialogus
from tkinterweb import HtmlFrame

app = CTk()
app.title("Kreka (CTk)")

def search():
    query = adress.get()
    web.load_website(f"https://www.google.com/search?q={query}")

def goto():
    query = adress.get()
    web.load_website(f"https://{query}")

top = CTkFrame(app)
top.pack(fill="x", pady="2", padx="2")

home = CTkButton(top, text = "🏠", width=1, command = lambda:web.load_website("https://progwi0.github.io/"))
home.pack(side="left", padx="2")

back = CTkButton(top, text = "←", width=1, command = lambda:web.back())
back.pack(side="left", padx="2")

forward = CTkButton(top, text = "→", width=1, command = lambda:web.forward())
forward.pack(side="left", padx="2")

adress = CTkEntry(top)
adress.pack(side="left", fill="both", expand=True)

refresh = CTkButton(top, text = "🔄", width=1, command = lambda:web.reload())
refresh.pack(side="left", padx="2")

search = CTkButton(top, text = "🔍", width=1, command=search)
search.pack(side="left", padx="2")

goto = CTkButton(top, text = "➡️", width=1, command=goto)
goto.pack(side="left", padx="2")

mps = CTkFrame(app)
mps.pack(fill="x", pady="2", padx="2")

kreka = CTkButton(mps, text = "🍪", width=1, command = lambda:dialogus.showinfo("🍪", "Kreka 1.0\nCreated in 2025 by progwi0."))
kreka.pack(side="left", padx="2")

google = CTkButton(mps, text = "Google", command = lambda:web.load_website("https://www.google.com/"))
google.pack(side="left", padx="2", fill="x", expand=True)

facebook = CTkButton(mps, text = "Facebook", command = lambda:web.load_website("https://www.facebook.com/"))
facebook.pack(side="left", padx="2", fill="x", expand=True)

ddg = CTkButton(mps, text = "DuckDuckGo", command = lambda:web.load_website("https://www.duckduckgo.com/"))
ddg.pack(side="left", padx="2", fill="x", expand=True)

youtube = CTkButton(mps, text = "YouTube", command = lambda:web.load_website("https://www.youtube.com/"))
youtube.pack(side="left", padx="2", fill="x", expand=True)

web = HtmlFrame(app)
web.load_website("https://progwi0.github.io/")

web.pack(fill="both", expand=True)

app.mainloop()
