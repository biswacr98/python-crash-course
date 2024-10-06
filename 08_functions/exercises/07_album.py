# Exercise 7:

# Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

# Use None to add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.

def make_album(artist_name, album_title, number_of_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_tracks:
        album['tracks'] = number_of_tracks
    return album

album_1 = make_album('jimi hendrix', 'are you experienced')
album_2 = make_album('john lee hooker', 'the healer')
album_3 = make_album('johnny cash', 'american iv')

album_4 = make_album('the beatles', 'white album', 30)

print(album_1)
print(album_2)
print(album_3)
print(album_4)

