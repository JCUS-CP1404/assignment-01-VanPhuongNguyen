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
        choice = input('>>> ').upper()
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
    # Find the max length of titles
    longest_title = find_longest_title(data)
    # Print out list of movie based on raw data
    show_movie(data, longest_title)
        
# Find longest title
def find_longest_title(data):
    longest_title = 0
    for movie in data:
        splited_data = movie.split(',')
        longest_title = len(splited_data[0]) if longest_title < len(splited_data[0]) else longest_title
    
    return longest_title

# Show movie based on raw data
def show_movie(raw_data, longest_title):
    watch_count = 0
    # Looping over raw data
    for movie in raw_data:
        # Split data by ','
        splited_data = movie.split(',')
        title_max_length = 0
        mark = '*' if 'u' in splited_data[3] else ''
        title = splited_data[0]
        title_max_length = len(title) if len(title) > title_max_length else title_max_length
        year = splited_data[1]
        genre = splited_data[2]
        print('{0:<2} {1:<{2}} - {3:<4} ({4})'.format(mark, title, longest_title ,year, genre))

        # If mark == '' then increment watch_count
        if not mark:
            watch_count += 1
    
    unwatch_count = len(raw_data) - watch_count
    print('{} movies watched, {} movies still to watch'.format(watch_count, unwatch_count))

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
