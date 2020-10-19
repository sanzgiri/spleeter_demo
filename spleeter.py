#!/usr/bin/env python3
import os
import streamlit as st

def main():
    
    st.title('Audio Separator Demo')
    st.markdown('')
    st.markdown('This app is for demo purposes only. The goal is to test algorithms that separate the vocal track from background music to improve accuracy \
    for speech recognition tasks. It uses the [Spleeter] (https://github.com/deezer/spleeter) library recently open-sourced by [Deezer Research] \
    (https://deezer.io/releasing-spleeter-deezer-r-d-source-separation-engine-2b88985e797e).')
    st.markdown('')
    song = st.text_input('Input song:', '')
    st.markdown('')
    st.markdown('')
    if st.button('Process audio'):
        
        st.markdown('')
        st.write("Obtaining song")

        song2 = 'track.mp3'
        cmd = "youtube-dl -x --postprocessor-args \"-ss 00:00:30.00 -t 00:00:45.00\" --audio-format mp3 \"ytsearch: " + song + "\"  --exec \"mv {} " + song2 + "\""
        #st.write(cmd)
        ret = os.system(cmd)
        
        st.write("Separating vocals from accompanying music")
        cmd = "spleeter separate -i track.mp3 -p spleeter:2stems -o output"
        ret = os.system(cmd)
        st.markdown('')
        
        st.write("Original Track")
        audio_file = open('track.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    
        st.write("Vocals")
        audio_file = open('output/track/vocals.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/wav")
        
        st.write("Accompaniments")            
        audio_file = open('output/track/accompaniment.wav', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/wav")
    
if __name__ == "__main__":
    main()