import whisper
import yt_dlp as youtube_dl
import speech_recognition as sr

def download_audio_from_youtube(video_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': output_path
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f'Áudio baixado e salvo em {output_path}')

def transcribe_audio(audio_path):
    # Inicializa o reconhecedor de fala
    recognizer = sr.Recognizer()

    # Usa um arquivo de áudio como entrada (substitua 'audio.wav' pelo seu arquivo de áudio)
    audio_file = f"E:\\workspace\\palestra_117\\{audio_path}"

    model = whisper.load_model("turbo")
    result = model.transcribe(audio_file)
    return result['text']

    # print(audio_file)
    #
    # with sr.AudioFile(audio_file) as source:
    #     # Ajusta o recognizer para o nível de ruído do ambiente e captura o áudio do arquivo
    #     # recognizer.adjust_for_ambient_noise(source)
    #     audio_data = recognizer.record(source)
    #     text = recognizer.recognize_sphinx(audio_data)
    #
    # # print("Sphinx thinks you said " + recognizer.recognize_sphinx(audio_data))
    #
    # try:
    #     # Tenta reconhecer o áudio usando o mecanismo de reconhecimento de fala do Google
    #     # text = recognizer.recognize_google(audio_data, language='pt-BR')
    #     # print(f"Texto reconhecido: {text}")
    #     return text
    # except sr.UnknownValueError:
    #     print("Não foi possível entender o áudio")
    # except sr.RequestError as e:
    #     print(f"Um erro ocorreu ao solicitar o serviço de reconhecimento de fala: {e}")

if __name__ == "__main__":
    # video_url = "https://youtu.be/O68y0yRZL1Y" # Fabio Akita
    # video_url = "https://youtu.be/aircAruvnKk?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi"
    # video_url = "https://youtu.be/aircAruvnKk?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi"
    # video_url = "https://youtu.be/IHZwWFHWa-w"
    video_url = "https://www.youtube.com/watch?v=d14TUNcbn1k" # Lecture 4 | Introduction to Neural Networks




    output_audio_path = 'downloaded_audio'

    download_audio_from_youtube(video_url,output_audio_path )
    transcribed_text = transcribe_audio(f"{output_audio_path}.wav")

    print("Transcrição:")
    print(transcribed_text)

    #Salva a transcrição em um arquivo de texto
    with open("transcricao.txt", "w") as file:
        file.write(transcribed_text)

    print("Transcrição salva no arquivo transcricao.txt")