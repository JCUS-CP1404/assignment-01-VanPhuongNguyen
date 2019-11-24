"""
Name: Nguyen Van Phuong
Date started: 24 November 2019
GitHub URL: https://github.com/robert09021998
"""


def main():
    # Load file and get data
    print("Movies To Watch 1.0 - by Nguyen Van Phuong")
    in_file = open('movies.csv', 'a+')
    data = load_data(in_file)
    print('{} movies loaded'.format(len(data)))

    # Menu lopper
    while True:
        print('\nMenu:')
        print('L - List movies')
        print('A - Add new movie')
        print('W - Watch a movie')
        print('Q - Quit')
        
        # Input choice
        choice = input('>>>').upper()
        if choice == 'L':
            list_movies(data)
        elif choice == 'A':
            add_movies(data)
        elif choice == 'W':
            watch_movie(data)
        elif choice == 'Q':
            save_data(data)
            print('{} movies saved to movies.csv'.format(len(data)))
            break
        else:
            print('Invalid menu choice')
        
    


# Laod file
def load_data(in_file):
    in_file.seek(0)
    data = in_file.readlines()
    return data

# Show list movies
def list_movies(data):
    return

# Add new movie
def add_movies(data):
    return

# Watch a movie
def watch_movie(data):
    return

# Save movies:
def save_data(data):
    return

# Run main funciton
if __name__ == '__main__':
    main()
