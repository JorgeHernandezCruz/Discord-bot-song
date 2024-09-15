import discord
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Configura las credenciales de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="Your Token Client", client_secret="Your Client Secret ID"))

# Obtén una canción aleatoria con su URL
def get_random_song():
    results = sp.recommendations(seed_genres=['pop'], limit=50)
    track = random.choice(results['tracks'])
    song_name = track['name']
    artist_name = track['artists'][0]['name']
    song_url = track['external_urls']['spotify']
    return f"{song_name} - {artist_name}", song_url

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$song'):
            song_info, song_url = get_random_song()
            await message.channel.send(f"Here's a random song for you: {song_info}\nListen here: {song_url}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Your Client Discord ID ')
