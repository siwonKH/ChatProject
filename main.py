import ServerV2
from youtube_search import YoutubeSearch
import json

title = ["123", "sf", "sdf"]
yt = YoutubeSearch("La campanella", max_results=3).to_json()
for i in range(0, 3):
    title[i] = str(json.loads(yt)['videos'][i]['title']).split(" ")

string = " "
for i in range(0, 3):
    for j in title[i]:
        j = j.lower()
        string += j + " "
print(string)
big = 0
for i in range(0, 3):
    for j in title[i]:
        j = j.lower()
        print(j)
        val = string.count(" " + j)
        # print(val)
        if val > big:
            big = val
print("\n\n\n")
for i in range(0, 3):
    for j in title[i]:
        j = j.lower()
        val = string.count(" " + j)
        # print(val)
        if val == big:
            print(j)
# import ServerV2
