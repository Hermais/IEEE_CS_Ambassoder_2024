input()


socks = list(map(int, input().split()))

socks_on_table = set()

socks_on_table_count = 0

for sock in socks:
    if sock in socks_on_table:
        socks_on_table.remove(sock)
    else:
        socks_on_table.add(sock)
        if socks_on_table_count < len(socks_on_table):
            socks_on_table_count = len(socks_on_table)

print(socks_on_table_count)

