import time


class User:
    nickname: str = None
    password: int = None
    age: int = None

    def __init__(self, nickname: str, password: int, age: int):
        self.age = age
        self.nickname = nickname
        self.password = password

    def __str__(self) -> str:
        return self.nickname

class Video:
    title: str = None
    duration: int = None
    time_now: int = 0
    is_adult_mode: bool = False

    def __init__(self, title: str, duration: int,
                 time_now: int = 0, is_adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.is_adult_mode = is_adult_mode

    def __repr__(self) -> str:
        return self.title

class UrTube:
    users: list[User] = []
    videos: list[Video] = []
    current_user: User | None = None

    def find_user_by_nickname(self, nickname: str) -> User | None:
        for user in self.users:
            if user.nickname == nickname:
                return user
        return None

    def log_in(self, nickname: str, password: str) -> None:
        possible_user: User = self.find_user_by_nickname(nickname)
        if possible_user == None:
            return
        hash_password: int = len(password)
        if possible_user.password == hash_password:
            self.current_user = possible_user

    def register(self, nickname: str, password: str, age: int) -> None:
        if self.find_user_by_nickname(nickname) != None:
            print(f"Пользователь {nickname} уже существует")
            return
        new_user: User = User(nickname, len(password), age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self) -> None:
        self.current_user = None

    def add(self, *videos: Video) -> None:
        for new_video in videos:
            is_already_added: bool = False
            for video in self.videos:
                if new_video.title == video.title:
                    is_already_added = True
            if not is_already_added:
                self.videos.append(new_video)

    def get_videos(self, query: str) -> list[Video]:
        found_videos: list[Video] = []
        for video in self.videos:
            if video.title.lower().count(query.lower()) > 0:
                found_videos.append(video)
        return found_videos

    def watch_video(self, title: str) -> None:
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        current_video: Video = None
        for video in self.videos:
            if video.title == title:
                current_video = video
                break
        if current_video == None:
            return
        adult_age = 18
        if self.current_user.age < adult_age and current_video.is_adult_mode:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        while current_video.time_now < current_video.duration:
            time.sleep(1)
            current_video.time_now += 1
            print(current_video.time_now, end=" ")
        current_video.time_now = 0
        print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, is_adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')