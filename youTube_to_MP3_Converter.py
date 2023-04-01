import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import *

class YoutubeToMp3Converter:
    def __init__(self, master):
        self.master = master
        master.title("YouTube to MP3 Converter")
        master.configure(bg='#aaccbb')

        self.url_label_1 = tk.Label(master, text="URL do vídeo 1:", bg='#aaccbb')
        self.url_label_1.grid(row=0, column=0)

        self.url_entry_1 = tk.Entry(master, width=50)
        self.url_entry_1.grid(row=0, column=1)

        self.url_label_2 = tk.Label(master, text="URL do vídeo 2:", bg='#aaccbb')
        self.url_label_2.grid(row=1, column=0)

        self.url_entry_2 = tk.Entry(master, width=50)
        self.url_entry_2.grid(row=1, column=1)

        self.url_label_3 = tk.Label(master, text="URL do vídeo 3:", bg='#aaccbb')
        self.url_label_3.grid(row=2, column=0)

        self.url_entry_3 = tk.Entry(master, width=50)
        self.url_entry_3.grid(row=2, column=1)

        self.convert_button = tk.Button(master, text="Converter", command=self.convert_to_mp3)
        self.convert_button.configure(bg='#fff', fg='#333', bd=2, relief='raised', font=('calibri', 10, 'bold'))
        self.convert_button.grid(row=3, column=1)

    def convert_to_mp3(self):
        youtube_urls = [self.url_entry_1.get(), self.url_entry_2.get(), self.url_entry_3.get()]

        for url in youtube_urls:
            if url:
                # Cria uma instância do objeto YouTube
                yt = YouTube(url)

                # Extrai o arquivo de áudio do vídeo usando o MoviePy
                audio_file = yt.streams.filter(only_audio=True).first().download()
                audio = AudioFileClip(audio_file)

                # Define a qualidade do arquivo de saída
                bitrate = "320k"

                # Pede para o usuário escolher um local para salvar o arquivo de saída
                save_path = filedialog.asksaveasfilename(defaultextension=".mp3", initialfile=yt.title)

                # Salva o arquivo de áudio como um arquivo mp3 com qualidade de 320kbps
                audio.write_audiofile(save_path, bitrate=bitrate)

                # Remove o arquivo de áudio original
                os.remove(audio_file)

        # Mostra uma mensagem informando que a conversão foi concluída
        messagebox.showinfo(title="Conversão concluída", message="A conversão foi concluída com sucesso!")

root = tk.Tk()
converter = YoutubeToMp3Converter(root)
root.mainloop()
