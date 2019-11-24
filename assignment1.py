"""
Name: Nguyen Van Phuong
Date started: 24 November 2019
GitHub URL: https://github.com/robert09021998
"""


def main():
    # Load file and get data
    print("Movies To Watch 1.0 - by Nguyen Van Phuong")
    in_file = open('movies.csv', 'r+')
    data = in_file.readlines()
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
            # Join the data from list
            join_data = ''.join(data)
            # Seek to the beginning of the file
            in_file.seek(0)
            in_file.write(join_data)
            print('{} movies saved to movies.csv'.format(len(data)))
            break
        else:
            print('Invalid menu choice')
    
    # Close file
    in_file.close()

# ===============
# SHOW MOVIE LIST
# ===============
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
        mark = '*' if 'u' in splited_data[3] else ''
        title = splited_data[0]
        year = splited_data[1]
        genre = splited_data[2]
        print('{0:<2} {1:<{2}} - {3:<4} ({4})'.format(mark, title, longest_title ,year, genre))

        # If mark == '' then increment watch_count
        if not mark:
            watch_count += 1
    
    unwatch_count = len(raw_data) - watch_count
    print('{} movies watched, {} movies still to watch'.format(watch_count, unwatch_count))
        

# =========
# ADD MOVIE
# =========
def add_movies(data):
    # User input
    def functionA():
        return
    title = text_handler('Title: ')
    year = year_handler()
    genre = text_handler('Category: ')

    
    # Save to data
    data_to_save = '\n{},{},{},u'.format(title, year, genre)
    data.append(data_to_save)
    # join_data = ''.join(data)
    # print(join_data)

# Text handler
def text_handler(input_name):
    user_input = input(input_name)
    while not user_input.strip():
        print('Input cannot be blank')
        user_input = input(input_name)

    return user_input
    
# Year handler
def year_handler():
    while True:
        try:
            year_input = int(input('Year: '))
            if year_input <= 0:
                raise Exception('YearError')
            break
        except ValueError:
            print('Invalid input, enter a valid number')
        except Exception:
            print('Your number must be more than 0')
    
    return year_input

            
    


# ===========
# WATCH MOVIE
# ===========
def watch_movie(data):
    return

# ==========
# SAVE MOVIE
# ==========
def save_data(data):
    return

# ========
# RUN MAIN
# ========
if __name__ == '__main__':
    main()
