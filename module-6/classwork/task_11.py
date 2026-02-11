# НЕОБХОДИМО РЕАЛИЗОВАТЬ:

# 1. Посчитать количество сообщений каждого пользователя.
#    Результат сохранить в словарь вида:
#    {
#        "Алиса": 3,
#        "Боб": 2
#    }

# 2. Для каждого пользователя:
#    2.1 Найти множество уникальных слов, которые он использовал
#        (слова разделяются методом split()).
#    2.2 Найти самое частое слово пользователя.
#        Если самых частых слов несколько — можно выбрать любое.

# 3. Найти пользователя с самым большим словарным запасом,
#    где словарный запас — это количество уникальных слов,
#    использованных пользователем.

# 4. Найти множество слов, которые использовали ВСЕ пользователи
#    (пересечение множеств слов пользователей).

# 5. Для каждого пользователя определить максимальный перерыв
#    между его сообщениями:
#    - перерыв = разница между timestamp текущего и предыдущего сообщения
#    - найти пользователя с самым большим таким перерывом

messages = [
    {"user": "Алиса", "text": "привет здравствуй", "timestamp": 1},
    {"user": "Боб", "text": "здравствуй", "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя", "timestamp": 3},
    {"user": "Боб", "text": "привет Алиса", "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб", "text": "пока Алиса", "timestamp": 20},
    ]

count_messages = {}
unique_word = {}
max_count_word = {}
all_unique_word = set()

for message in messages:
    user = message["user"]
    text = message["text"]
    timestamp = message["timestamp"]

    count_messages[user] = count_messages.get(user, 0) + 1
        
    unique_word.setdefault(user, set()).update(text.split())

for user_name in unique_word:
    count_word = {}
    for message in messages:
        if message["user"] == user_name:
            for word in message["text"].split():
                count_word[word] = count_word.get(word, 0) + 1

    max_word = None
    max_count = 0
    for word, count in count_word.items():
        if count > max_count:
            max_word = word
            max_count = count
    max_count_word[user_name] = max_word, max_count

max_unique_word = None
max_count_unique_word = 0
for user, word in unique_word.items():
    if len(word) > max_count_unique_word:
        max_unique_word = user
        max_count_unique_word = len(word)

print(count_messages, unique_word, max_count_word, max_unique_word, all_unique_word)

