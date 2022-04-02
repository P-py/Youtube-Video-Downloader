import os
from tkinter import *
from tkinter import Text, filedialog
from tkinter.messagebox import showwarning
from urllib.parse import parse_qs, urlparse

import googleapiclient.discovery
from pytube import YouTube

path_list = []

#Defining the function of downloading and selecting the path
def download_video():
    if callback == "Single video":
        url = URLEntry.get()
        ytURL = YouTube(url)
        finalYTURL = ytURL.streams.get_highest_resolution()
        try:
            finalYTURL.download(path_list[0])
            showwarning(message='The download was a sucessful!')
        except:
            showwarning(message='The download failed! Please check the input infos.')
    elif callback == "Playlist":
        url = URLEntry.get()
        query = parse_qs(urlparse(url).query, keep_blank_values=True)
        playlist_id = query["list"][0]
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "###API KEY HERE###")
        request = youtube.playlistItems().list(
            part = "snippet",
            playlistId = playlist_id,
            maxResults = 50
        )
        response = request.execute()

        playlist_items = []
        while request is not None:
            response = request.execute()
            playlist_items += response["items"]
            request  = youtube.playlistItems().list_next(request, response)
        
        for vd in playlist_items:
            url = f'https://www.youtube.com/watch?v={vd["snippet"]["resourceId"]["videoId"]}'
            ytURL = YouTube(url)
            finalUrl = ytURL.streams.filter(onyl_audio=True).first()
            outfile = finalUrl.download()
            base, ext = os.path.splittext(outfile)
            new_file = base+".mp3"
            os.rename(outfile, new_file)


def selectpath():
    path = filedialog.askdirectory()
    PathLabel = Label(root, text=f'The selected path is: {path}', font='Arial 11 bold', fg='Green')
    if (len(path) > 1):
        PathLabel.place(rely=.65, relx=.5, anchor=CENTER)
    else:
        PathLabel.grid(text=' ')
    path_list.append(path)

def callback(*args):
    downloadType = optionPlaylistVideo
    return downloadType

optionList = [
    "Playlist",
    "Single video"
]

optionListType = [
    "MP4",
    "MP3"
]

##Defining and configuring root
root = Tk()
root.title('Youtube Video Downloader')
root.geometry('600x450')
#root.iconbitmap('icon.ico') ## PUT YOUR ICON PATH HERE OR USE THE DEFAULT ICON IN THE CODE FOLDER
root.columnconfigure(0, weight=1)

#Canva config
rootCanva = Canvas(root, bg='Light Grey')
rootCanva.place(relwidth=1.0, relheight=1.0)

#Title label config
TitleLabel = Label(rootCanva, bg='Light Grey', text='Youtube Video Downloader - YVD', font='Roboto 16 bold italic underline')
TitleLabel.place(rely=.05, relx=.5, anchor=CENTER)

#URL label, entry and button config
URLEntryLabel = Label(rootCanva, bg='Light Grey', text='1. Enter the URL of the video/playlist', font=('Arial 12 bold'))
URLEntryLabel.place(rely=.15, relx=.5, anchor=CENTER)
URLEntryVar = StringVar()
URLEntry = Entry(rootCanva, width=50, textvariable=URLEntryVar)
URLEntry.place(rely=.2, relx=.5, anchor=CENTER)

optionPlaylistVideo = StringVar(root)
optionPlaylistVideo.set(optionList[0])
opt = OptionMenu(root, optionPlaylistVideo, *optionList)
opt.config(font=('Arial 10'))
opt.place(rely=.27, relx=.5, anchor=CENTER)

#Select the path for the download
SelectPathLabel = Label(rootCanva, bg='Light Grey', text='2. Select the path to save the file', font='Arial 12 bold')
SelectPathLabel.place(rely=.35, relx=.5, anchor=CENTER)
SelectPathButton = Button(rootCanva, height=2, text='Select Path',  font='Arial 10 bold', fg='White', bg='Red', command=selectpath)
SelectPathButton.place(rely=.43, relx=.5, anchor=CENTER)

#Download the video
DownloadVideoLabel = Label(rootCanva, bg='Light Grey', text='3. Download the video', font='Arial 12 bold')
DownloadVideoLabel.place(rely=.55, relx=.5, anchor=CENTER)
DownloadButton = Button(rootCanva, height=2, text='Download', font='Arial 10 bold', bg='red', fg='white', command=download_video)
DownloadButton.place(rely=.63, relx=.5, anchor=CENTER)

#Developed by Text
Developed = Label(rootCanva, text='Vesion: (ALPHA) 0.1 Developed by Pedro S. (p-py) / All rights reserved ©')
Developed.place(relx=.5, rely=.95, anchor=CENTER)


optionPlaylistVideo.trace("w", callback)

root.mainloop()
