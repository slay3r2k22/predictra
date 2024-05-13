import tkinter as tk
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("400x200")

        self.url_label = tk.Label(root, text="Enter YouTube URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.pack()

        self.quality_label = tk.Label(root, text="Select Video Quality:")
        self.quality_label.pack()

        self.quality_var = tk.StringVar(root)
        self.quality_var.set("360p")  # Default quality
        self.quality_options = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p"]
        self.quality_menu = tk.OptionMenu(root, self.quality_var, *self.quality_options)
        self.quality_menu.pack()

        self.download_button = tk.Button(root, text="Download", command=self.download_video)
        self.download_button.pack(pady=10)

    def download_video(self):
        video_url = self.url_entry.get()
        quality = self.quality_var.get()

        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(res=quality).first()
            stream.download()
            tk.messagebox.showinfo("Download Complete", "Video downloaded successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()