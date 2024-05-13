import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from tqdm import tqdm
import time

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("400x300")
        self.root.configure(bg='#333333')  # Set background color to black

        self.loading_screen = tk.Label(self.root, text="Predictra Downloader is loading", bg='#333333', fg='white')
        self.loading_screen.pack(expand=True)

        self.root.after(5000, self.show_main_window)  # Show main window after 5 seconds

    def show_main_window(self):
        self.loading_screen.destroy()  # Remove loading screen

        self.url_label = tk.Label(self.root, text="Enter YouTube URL:", bg='#333333', fg='white')
        self.url_label.pack()

        self.url_entry = tk.Entry(self.root, width=40)
        self.url_entry.pack()

        self.download_option_label = tk.Label(self.root, text="Select Download Option:", bg='#333333', fg='white')
        self.download_option_label.pack()

        self.download_option_var = tk.StringVar(self.root)
        self.download_option_var.set("Video")  # Default option
        self.download_option_menu = tk.OptionMenu(self.root, self.download_option_var, "Video", "Audio")
        self.download_option_menu.pack()

        self.quality_label = tk.Label(self.root, text="Select Quality/Bitrate:", bg='#333333', fg='white')
        self.quality_label.pack()

        self.quality_var = tk.StringVar(self.root)
        self.quality_var.set("360p")  # Default quality
        self.quality_options = ["44.1Kbps", "128Kbps", "256Kbps", "384Kbps", "512Kbps", "720p", "1080p", "1440p", "2160p"]
        self.quality_menu = tk.OptionMenu(self.root, self.quality_var, *self.quality_options)
        self.quality_menu.pack()

        self.download_button = tk.Button(self.root, text="Download", command=self.download_media, bg='#660000', fg='white')
        self.download_button.pack(pady=10)

    def download_media(self):
        download_option = self.download_option_var.get()
        media_url = self.url_entry.get()
        quality = self.quality_var.get()

        try:
            yt = YouTube(media_url)
            if download_option == "Audio" and quality.endswith("Kbps"):
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_stream.download(filename=f"{yt.title}.mp3")
                messagebox.showinfo("Download Complete", "Audio downloaded successfully!")
            elif download_option == "Video":
                if quality.endswith("Kbps"):
                    messagebox.showerror("Error", "Please select a video quality for video download.")
                else:
                    stream = yt.streams.filter(res=quality).first()
                    with tqdm(total=stream.filesize, unit='B', unit_scale=True, desc=f'Downloading {yt.title}', ascii=True) as progress_bar:
                        stream.download(output_path='.', filename=f"{yt.title}.mp4", filename_prefix='tmp')
                        progress_bar.update(stream.filesize)
                    messagebox.showinfo("Download Complete", "Video downloaded successfully!")
            else:
                messagebox.showerror("Error", "Invalid download option selected.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
