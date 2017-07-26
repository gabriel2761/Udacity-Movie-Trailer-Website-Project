import media
import fresh_tomatoes

lost_in_translation = media.Movie('Lost in translation',
        'A lonely aging movie star meets a newlywed woman in Tokyo',
        'https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg',
        'https://www.youtube.com/watch?v=sU0oZsqeG_s')

whiplash = media.Movie('Whiplash',
        'An ambitious young jazz drummer, in pursuit of rising to the top of his elite music conservatory',
        'http://t3.gstatic.com/images?q=tbn:ANd9GcS_IwW5-_mWA1PXiPG4qEhLC6Q3vntQd7Bzgs_YE7HHFifItn2T',
        'https://www.youtube.com/watch?v=7d_jQycdQGo')

spirited_away = media.Movie('Spirited Away',
        '10-year-old Chihiro and her parents stumble upon a seemingly abandoned amusement park',
        'http://t1.gstatic.com/images?q=tbn:ANd9GcS6MveoDoJOg9-wMvtHE4ak_-HDZeYS1egb9PwRcf8lhrtcppMc',
        'https://www.youtube.com/watch?v=ByXuk9QqQkk')

movies = [lost_in_translation, whiplash, spirited_away]
fresh_tomatoes.open_movies_page(movies)
