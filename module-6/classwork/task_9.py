clients = [
    (1, "111", "a@x.com"),
    (2, "111", "b@x.com"),
    (3, "222", "c@x.com"),
    (4, "333", "c@x.com"),
    (5, "444", "d@x.com")
]

phones_duble = {}
emails_duble = {}

for id, phone, email in clients:
    phones_duble.setdefault(phone, set()).add(id)
    emails_duble.setdefault(email, set()).add(id)

duble = []
for o in (phones_duble, emails_duble):
    for ids in o.values():
        if len(ids) > 1:
            duble.append(ids)

duble_ids = set()
for n in duble:
    duble_ids |= n

clin_clients = []
for id, phone, email in clients:
    if id not in duble_ids:
        clin_clients.append(id)

count_clin_clients = len(clin_clients)
        

print(duble, clin_clients, count_clin_clients)