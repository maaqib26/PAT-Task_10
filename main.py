import random

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = None

    def rate_audio(self, user, rating):
        if 1 <= rating <= 5:
            self.rating = rating
            user.add_rating(rating)
            print(f"Rating {rating} added to {self.name}")
        else:
            print("Invalid rating. Please provide a rating between 1 and 5.")

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audio_files = []
        self.ratings = []

    def add_audio(self, audio):
        self.audio_files.append(audio)
        print(f"Audio '{audio.name}' added to playlist '{self.name}'")

    def rate_playlist(self, user, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            user.add_rating(rating)
            print(f"Rating {rating} added to playlist {self.name}")
        else:
            print("Invalid rating. Please provide a rating between 1 and 5.")

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class User:
    def __init__(self, name):
        self.name = name
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

def main():
    # Create Users
    user1 = User("User1")
    user2 = User("User2")
    user3 = User("User3")

    users = [user1, user2, user3]

    # Create Audio
    audio1 = Audio("Song1", "https://song1.url")
    audio2 = Audio("Song2", "https://song2.url")

    # Create Playlists
    playlist1 = Playlist("Playlist1", "Rock")
    playlist2 = Playlist("Playlist2", "Pop")

    # Add audio to playlists
    playlist1.add_audio(audio1)
    playlist1.add_audio(audio2)
    playlist2.add_audio(audio2)

    # Rate Audio and Playlists randomly
    for user in users:
        for audio in [audio1, audio2]:
            audio.rate_audio(user, random.randint(1, 5))

        playlist1.rate_playlist(user, random.randint(1, 5))
        playlist2.rate_playlist(user, random.randint(1, 5))

    # Display Average Ratings
    print(f"\nAverage Audio Ratings:")
    for audio in [audio1, audio2]:
        average_rating = sum(audio.rating for user in users) / len(users) if audio.rating else 0
        print(f"{audio.name}: {average_rating:.2f}")

    print(f"\nAverage Playlist Ratings:")
    for playlist in [playlist1, playlist2]:
        average_rating = playlist.get_average_rating()
        print(f"{playlist.name}: {average_rating:.2f}")

if __name__ == "__main__":
    main()