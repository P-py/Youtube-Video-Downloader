from pytube import YouTube
import tkinter
import customtkinter
from tkinter import messagebox

def StartDownload():
    progressBar.set(0)
    progressLabel.configure(text="")
    resultLabel.configure(text="")
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=downloadProgress)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        resultLabel.configure(text="Download successful!", text_color="green")
        messagebox.showwarning(message="Download successful!")
        progressLabel.configure(text_color="green")
    except:
        resultLabel.configure(text="Unsuccessful download.", text_color="red")

def downloadProgress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage = (bytes_download/total_size)*100
    progressBar.set(float(percentage/100))
    progressBar.update()
    progressLabel.configure(text=str(int(percentage))+"%")
    progressLabel.update()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")
title = customtkinter.CTkLabel(app, text="Insert your YouTube video link below")
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
resultLabel = customtkinter.CTkLabel(app, text="")
download = customtkinter.CTkButton(app, text="Download video", command=StartDownload)
progressLabel = customtkinter.CTkLabel(app, text="")
progressBar = customtkinter.CTkProgressBar(app, width=400)

title.pack(pady=10)
link.pack()
resultLabel.pack(pady=10)
download.pack(pady=10)
progressLabel.pack(pady=10)
progressBar.pack(pady=10)
progressBar.set(0)
app.mainloop()