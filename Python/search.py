import os

def search_string_in_files(directory, search_string):
    result_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='shift-jis') as file:
                content = file.read()
                if search_string in content:
                    result_files.append(filename)
    return result_files

directory_path = 'C:/Users/BobDi/Documents/Dolphin Emulator/Load/Riivolution/千年之门/patch/files/msg'
search_string = '下と克囚往攘演'
matching_files = search_string_in_files(directory_path, search_string)

print("包含字符串的文件:")
for file in matching_files:
    print(file)
