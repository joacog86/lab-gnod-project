
import streamlit as st
import pandas as pd

df = pd.read_csv("df.csv")

def recommender():
    song_name = st.text_input("Search a song")

    if any(c.isalpha() for c in song_name) and any(c.isalnum() for c in song_name):
        song_name = song_name.lower()

        matching_songs = df[df['title'].str.lower().str.contains(song_name) | df['artist'].str.lower().str.contains(song_name)]

        if not matching_songs.empty:
            cluster = matching_songs.iloc[0]['cluster']
            h_songs = df[(df['cluster'] == cluster) & (df['H_or_N'] == 'H')].sample(5)
            n_songs = df[(df['cluster'] == cluster) & (df['H_or_N'] == 'N')].sample(5)

            if matching_songs.iloc[0]['H_or_N'] == 'H':
                st.write("Yeah, popular song! Good choice.")
                st.write(f"Start with your song '{matching_songs.iloc[0]['title']}' by '{matching_songs.iloc[0]['artist']}'")
                st.image('hot_song.gif')
                st.write("Here are some other hot songs:")
                for i, row in h_songs.iterrows():
                    st.write(f"- '{row['title']}' by '{row['artist']}'")

            else:
                st.write("Old school, bro! Classics never die.")
                st.write(f"Start with your song '{matching_songs.iloc[0]['title']}' by '{matching_songs.iloc[0]['artist']}'")
                st.image('classic_song.gif')
                st.write("Be cool and discover Here some hot songs:")
                for i, row in n_songs.iterrows():
                    st.write(f"- '{row['title']}' by '{row['artist']}'")

        else:
            st.write("No match found yet, try another song :)")
            st.image('not_found.gif')
    else:
        st.write("What? Does a cat walk on your keyboard? Tell him to enter a song name containing letters and/or numbers.")

recommender()