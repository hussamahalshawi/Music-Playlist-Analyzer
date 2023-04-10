'''
The project is a music data analysis tool that loads a set of music data and provides functionality 
to filter and analyze the data. The data is stored in a list of dictionaries, with each dictionary 
representing a single song and containing fields such as the artist, title, genre, year, and duration.
Requirements:
The project must have a function to convert the song durations from seconds to minutes and seconds.
The project must have a function to filter the music data based on a specific genre and/or year.
The project must have a function to analyze the music data by computing the average song duration for each artist.
The project must output the filtered and analyzed data to the console.
The project must use proper function and variable naming conventions to make the code easy to read and understand.
The project must be well-documented using docstrings and comments to explain each function's purpose and inputs/outputs.
The project must be modular, with each function performing a specific task and not exceeding a few dozen lines of code. This will help with maintainability and readability.
The project should handle potential errors such as incorrect or missing input data, file loading errors, and other runtime errors that could occur.
The project must be well-tested to ensure that each function produces the expected results and handles potential errors as expected.

'''

from collections import Counter

def chooses(data_music):
    '''
    chooses:
    1. Load Minutes And Seconds Playlist
    2. View Playlist
    3. Search Playlist
    4. Analyze Playlist
    5. Exit
    Args:
        data_music (dictionary): A dictionary of data to be Music.

    Output:
        return function()
    '''
    while True:
        print("Welcome to the Music Playlist Analyzer! \nchoose:\n1. Load Playlist\n2. View Playlist\n3. Search Playlist\n4. Analyze Playlist\n5. Shut down")
        choose = input("Enter the choose :")
        if choose.isdigit():
            choose = int(choose)
            if choose == 1:
                '''
                function to convert the song durations from
                seconds to minutes and seconds
                '''
                Change_Durations_Playlist(data_music)
            elif choose == 2:
                '''
                View Playlist in data_music
                '''
                View_Playlist(data_music)
            elif choose == 3:
                '''
                function to filter the music data based on a
                specific genre and/or year.
                '''
                Filter_The_Music_Data(data_music)
            elif choose == 4:
                '''
                function to analyze the music data by computing the
                average song duration for each artist and output the 
                filtered and analyzed data to the console.
                '''
                Analyze_Playlist(data_music)
            elif choose == 5:
                quit()
            else:
                print("The choose not range")
        else:
            print("The value not number integer")


def Change_Durations_Playlist(data_music):
    '''
    function to convert the song durations from
    seconds to minutes and seconds
    Args:
        data_music (dictionary): A dictionary of data to be Music.

    Output: 
        dictionary new: convert the song durations from seconds to 
        minutes and seconds

    Returns:
        return function View_Playlist
    '''
    for Title in data_music:
        Time_seconds = data_music[Title]['duration']
        Time_minutes = int(Time_seconds / 60)
        Time_seconds = int(Time_seconds % 60)
        data_music[Title]['duration'] = f"{Time_minutes}:{Time_seconds}"
    print("--- Succssefully convert the song durations from seconds to minutes and seconds. ---")

    return View_Playlist(data_music)


def View_Playlist(data_music):
    '''
    View Playlist in data_music
    Args:
        data_music (dictionary): A dictionary of data to be Music.

    Output: 
        View Playlist in data_music

    Returns:
        return function chooses
    '''

    count = 1
    print("------- Playlist -------")
    # 1. Song Title - Artist Name - Genre Name - Release Year - Length (seconds)
    for Title in data_music:
        print(
            f"{count}. Song: {Title} - Artist: '{data_music[Title]['artist']}' - Genre: '{data_music[Title]['genre']}' - Year: {data_music[Title]['year']} - Duration: {data_music[Title]['duration']}")
        count += 1
    return chooses(data_music)


def Filter_The_Music_Data(data_music):
    '''
    function to filter the music data based on a
    specific genre and/or year.
    Args:
        data_music (dictionary): A dictionary of data to be Music.

    Output:
        output print filter the music data based on a 
        specific genre and/or year

    Returns:
        return function chooses
    '''
    dicti = {}
    lis_revers = []
    lis_search = []
    cuont = 1
    lis = input("Enter The Search:")
    lis = lis.split(" ")
    # filter Artist, Genre and Year
    for i in lis:
        if i.isdigit():
            i = int(i)
            lis_search.append(i)
        else:
            i = i.upper()
            lis_search.append(i)
    
    for Title in data_music:
        for Type in data_music[Title]:
            for search in lis_search:
                if type(data_music[Title][Type]) == str :
                    lis_str = data_music[Title][Type].split(" ")
                    for string in lis_str:
                        str_upper = string.upper()
                        if str_upper == search:
                            dicti[Title] = cuont
                            cuont += 1
                else:
                    if data_music[Title][Type] == search:
                        dicti[Title] = cuont
                        cuont += 1
        cuont = 1
    # Arrangement of items
    dicti = sorted(dicti.items(), key=lambda x: x[1])
    dicti = dict(dicti)
    for dicti_revers in reversed(dicti):
        lis_revers.append(dicti_revers)
    # View Playlist in Search
    num = 1
    print("------- Search Playlist -------")
    for i in lis_revers:
        for Title in data_music:
            if Title == i:
                print(
                    f"{num}. Song: {Title} - Artist: '{data_music[Title]['artist']}' - Genre: '{data_music[Title]['genre']}' - Year: {data_music[Title]['year']} - Duration: {data_music[Title]['duration']}")
                num += 1
    return chooses(data_music)


def Analyze_Playlist(data_music):
    '''
    function to analyze the music data by computing the
    average song duration for each artist and output the 
    filtered and analyzed data to the console.
    Args:
        data_music (dictionary): A dictionary of data to be Music.

    Output:
        output the filtered and analyzed data to the console.

    Returns:
        return function chooses
    '''

    sum_duration = 0
    lis_year = []
    lis_artist = []
    for Title in data_music:
        if type(data_music[Title]['duration']) == int:
            sum_duration += data_music[Title]['duration']
        else:
            mint = (data_music[Title]['duration']).split(":")
            Time_minutes = int(mint[0])
            Time_seconds = int(mint[1])
            sum_duration += (Time_minutes * 60) + Time_seconds

        lis_artist.append(data_music[Title]['artist'])

        lis_year.append(data_music[Title]['year'])

    # string = lis_artist.split()
    Artist_Name = Counter(lis_artist)
    Newest_song = max(lis_year)
    Oldest_song = min(lis_year)
    Average = sum_duration / len(data_music)
    # ----------------print the value--------------------
    print(f"------- Analyze Playlist -------\nTotal number of songs: {len(data_music)}")
    print(f"Total playlist length (seconds): {sum_duration}")
    print(f"Average song length (seconds): {Average}")
    for Title in data_music:
        if data_music[Title]['year'] == Newest_song:
            print(f"------- Newest Song -------\nSong: {Title} - Artist: '{data_music[Title]['artist']}' - Genre: '{data_music[Title]['genre']}' - Year: {data_music[Title]['year']} - Duration: {data_music[Title]['duration']}")
        if data_music[Title]['year'] == Oldest_song:
            print(f"------- Oldest Song -------\nSong: {Title} - Artist: '{data_music[Title]['artist']}' - Genre: '{data_music[Title]['genre']}' - Year: {data_music[Title]['year']} - Duration: {data_music[Title]['duration']}")
    print(f"Most common artist: {Artist_Name}")
    return chooses(data_music)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_music = {
        "Bohemian Rhapsody": {"artist": "Queen", "genre": "Rock", "year": 1975, "duration": 355},
        "Stairway to Heaven": {"artist": "Led Zeppelin", "genre": "Rock", "year": 1971, "duration": 482},
        "Hotel California": {"artist": "The Eagles", "genre": "Rock", "year": 1977, "duration": 390},
        "Back in Black": {"artist": "AC/DC", "genre": "Rock", "year": 1980, "duration": 255},
        "The Chain": {"artist": "Fleetwood Mac", "genre": "Rock", "year": 1977, "duration": 288},
        "Highway to Hell": {"artist": "AC/DC", "genre": "Rock", "year": 1979, "duration": 208},
        "Don't Stop Believin": {"artist": "Journey", "genre": "Rock", "year": 1981, "duration": 249},
        "Smells Like Teen Spirit": {"artist": "Nirvana", "genre": "Grunge", "year": 1991, "duration": 301},
        "Enter Sandman": {"artist": "Metallica", "genre": "Metal", "year": 1991, "duration": 332},
        "November Rain": {"artist": "Guns N Roses", "genre": "Rock", "year": 1991, "duration": 537},
    }
    chooses(data_music)
