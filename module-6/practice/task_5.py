network = {
    "Me": {"Alice", "Bob"},
    "Alice": {"Me", "Charlie", "Bob"},
    "Bob": {"Me", "David", "Eve"},
    "Charlie": {"Alice"},
    "David": {"Alice", "Bob"},
    "Eva": {"Bob"}
}

user = "Me"

friend_me = network[user]
friend_global = set()

for name in friend_me:
    friend_global.update(network[name])

friend_global.discard("Me")
dif_friend = friend_global - friend_me
    
print(dif_friend)