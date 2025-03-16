i = 1

while i < 33:
    text = f'<img src="/thumbnails/{i}.jpg" class="hover thumbnail" onclick="openPopup({i})">'
    print(text)
    i += 1