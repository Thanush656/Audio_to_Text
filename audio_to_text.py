
import streamlit as st
import whisper

st.title("Audio to Text Converter")

# Load the Whisper model
model = whisper.load_model("base")

audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3", "m4a", "ogg"])

if audio_file is not None:
    st.write("File uploaded successfully!")

    # Save uploaded file temporarily
    with open("audio_temp.wav", "wb") as f:
        f.write(audio_file.getbuffer())

    # Play audio in Streamlit
    st.audio(audio_file)

    # Transcribe the audio file using Whisper
    with st.spinner("Converting to text..."):
        result = model.transcribe("audio_temp.wav")

    # Display the detected language and the transcription
    st.write("Detected Language:", result["language"])
    st.write("Transcription:")
    st.write(result["text"])
