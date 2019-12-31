def my_mp3_playlist(file_path):
    with open(file_path, 'r') as f:
        temp += f.read().split(';')
        print(temp)

file_path = r'C:\src\first\songs.txt
  def my_mp3_playlist(file_path):
    temp = []
    with open(file_path, 'r') as f:
        for line in f:
            
            temp.append(line.split('\n'))
    print(temp[0])
my_mp3_playlist(r'C:\src\first\songs.txt')
f = open("c:\myCD.txt", "r")
cd_data = f.read()
cd_splitted_lines = cd_data.split("\n")
cd_items = []
for element in cd_splitted_lines:
    cd_items.append(element.split(":"))
my_cd_dict = {}
for item in cd_items:
    my_cd_dict[item[0]] = item[1]
f.close()
print(my_cd_dict)
