# Exercise 8:

# Start with 07_albums.py. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, number_of_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album

while True:
    print("\nPlease enter the album's artist and title:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)

