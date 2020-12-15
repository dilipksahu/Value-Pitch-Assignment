import json

moviesdata = []
with open('curiosity_data.json') as f:
    movies = json.load(f)

for cat in movies[0]['data']:
    for subcat in cat['subcategories']:
        movie = {
            'Category':cat['name'],
            'Sub-Category': subcat['name'],
            'Image-title': cat.get('image_label')
        }
        moviesdata.append(movie)

print(moviesdata)