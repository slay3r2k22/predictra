import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("400x250")

        self.url_label = tk.Label(root, text="Enter YouTube URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.pack()

        self.download_option_label = tk.Label(root, text="Select Download Option:")
        self.download_option_label.pack()

        self.download_option_var = tk.StringVar(root)
        self.download_option_var.set("Video")  # Default option
        self.download_option_menu = tk.OptionMenu(root, self.download_option_var, "Video", "Audio")
        self.download_option_menu.pack()

        self.quality_label = tk.Label(root, text="Select Quality/Bitrate:")
        self.quality_label.pack()

        self.quality_var = tk.StringVar(root)
        self.quality_var.set("360p")  # Default quality
        self.quality_options = ["44.1Kbps", "128Kbps", "256Kbps", "384Kbps", "512Kbps", "720p", "1080p", "1440p", "4K"]
        self.quality_menu = tk.OptionMenu(root, self.quality_var, *self.quality_options)
        self.quality_menu.pack()

        self.download_button = tk.Button(root, text="Download", command=self.download_media)
        self.download_button.pack(pady=10)

    def download_media(self):
        download_option = self.download_option_var.get()
        media_url = self.url_entry.get()
        quality = self.quality_var.get()

        try:
            yt = YouTube(media_url)
            if download_option == "Audio" and quality.endswith("Kbps"):
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_stream = audio_stream.download(filename=f"{yt.title}.mp3")
                messagebox.showinfo("Download Complete", "Audio downloaded successfully!")
            elif download_option == "Video":
                if quality.endswith("Kbps"):
                    messagebox.showerror("Error", "Please select a video quality for video download.")
                else:
                    stream = yt.streams.filter(res=quality).first()
                    stream.download()
                    messagebox.showinfo("Download Complete", "Video downloaded successfully!")
            else:
                messagebox.showerror("Error", "Invalid download option selected.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()