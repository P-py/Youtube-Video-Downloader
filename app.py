from pytube import YouTube
from tkinter import *
from tkinter import filedialog, Text
from tkinter.messagebox import showwarning
import os

path_list = []

#Defining the function of downloading and selecting the path
def download_video():
    url = URLEntry.get()
    ytURL = YouTube(url)
    finalYTURL = ytURL.streams.get_highest_resolution()
    try:
        finalYTURL.download(path_list[0])
        #DownloadLabel = Label(text=finalYTURL.title, fg='green', )
        #DownloadLabel.grid()
        showwarning(message='The download was a sucessful!')
    except:
        #FailDownloaadLabel = Label(text='Download failed! Please check the infos', fg='red')
        #FailDownloaadLabel.grid()
        showwarning(message='The download failed! Please check the input infos.')
def selectpath():
    path = filedialog.askdirectory()
    PathLabel = Label(root, text=f'The selected path is: {path}', font='Arial 11 bold', fg='Green')
    if (len(path) > 1):
        PathLabel.place(rely=.65, relx=.5, anchor=CENTER)
    else:
        PathLabel.grid(text=' ')
    path_list.append(path)

##Defining and configuring root
root = Tk()
root.title('Youtube Video Downloader')
root.geometry('600x450')
#root.iconbitmap('(ICON PATH)') ## PUT YOUR ICON PATH HERE
                                        #OR
#root.iconbitmap('icon.ico') ## PUT YOUR ICON PATH HERE

root.columnconfigure(0, weight=1)

#Canva config
rootCanva = Canvas(root, bg='Light Grey')
rootCanva.place(relwidth=1.0, relheight=1.0)

#Title label config
TitleLabel = Label(rootCanva, bg='Light Grey', text='Youtube Video Downloader - YVD', font='Roboto 16 bold italic underline')
TitleLabel.place(rely=.05, relx=.5, anchor=CENTER)

#URL label, entry and button config
URLEntryLabel = Label(rootCanva, bg='Light Grey', text='1. Enter the URL of the video', font=('Arial 12 bold'))
URLEntryLabel.place(rely=.15, relx=.5, anchor=CENTER)
URLEntryVar = StringVar()
URLEntry = Entry(rootCanva, width=50, textvariable=URLEntryVar)
URLEntry.place(rely=.2, relx=.5, anchor=CENTER)

#Select the path for the download
SelectPathLabel = Label(rootCanva, bg='Light Grey', text='2. Select the path to save the file', font='Arial 12 bold')
SelectPathLabel.place(rely=.27, relx=.5, anchor=CENTER)
SelectPathButton = Button(rootCanva, height=2, text='Select Path',  font='Arial 10 bold', fg='White', bg='Red', command=selectpath)
SelectPathButton.place(rely=.35, relx=.5, anchor=CENTER)

#Download the video
DownloadVideoLabel = Label(rootCanva, bg='Light Grey', text='3. Download the video', font='Arial 12 bold')
DownloadVideoLabel.place(rely=.45, relx=.5, anchor=CENTER)
DownloadButton = Button(rootCanva, height=2, text='Download', font='Arial 10 bold', bg='red', fg='white', command=download_video)
DownloadButton.place(rely=.53, relx=.5, anchor=CENTER)

#Developed by Text
Developed = Label(rootCanva, text='Vesion: (ALPHA) 0.1 Developed by Pedro S. (p-py) / All rights reserved ©')
Developed.place(relx=.5, rely=.95, anchor=CENTER)
root.mainloop()
