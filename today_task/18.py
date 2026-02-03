'''18. Safe File Open
        Input: read_file("no_file.txt")
        Output: FileNotFoundError caught -> "File does not exist!"'''

with open('text.txt', 'r') as f:
    reader = f.read()
    