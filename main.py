
import pyperclip

def collect_songs():
    print("This is what's in your clipboard:")
    clip_board_songs = pyperclip.paste()
    songs_list = clip_board_songs.split("\n")
    print(songs_list)

def main():
    print("Welcome to Copify")
    collect_songs()


main()