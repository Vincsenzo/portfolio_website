i = 1

while i < 33:
    # text = f'<img src="/thumbnails/{i}.jpg" class="hover thumbnail" onclick="openPopup({i})">'
    text = f'''
<div class="mItem">
    <img src="/thumbnails/{i}.jpg" />
</div>">
'''
    print(text)
    i += 1