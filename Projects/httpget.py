import urllib.request
import json


def getPayload(city, page):
    return(json.loads(urllib.request.urlopen(f"https://jsonmock.hackerrank.com/api/food_outlets?city={city}&page={page}").read()))


def getTopRatedFoodOutlets(city):
    output = []
    ratings = {}
    max_rating = float(0)
    page = 1
    j = getPayload(city, page)
    total_pages = j['total_pages']
    jData = []

    for p in range(total_pages):
        page = p + 1
        jData.append(getPayload(city, page))

    for x in jData:
        i = 0
        obj = x['data']
        for y in obj:
            o = obj[i]
            name = o['name']
            r = o['user_rating']['average_rating']
            update = {name:r}
            ratings.update(update)
            i += 1

    for k in ratings:
        r = ratings[k]
        if r > max_rating:
            max_rating = r

    for k in ratings:
        r = ratings[k]
        if r == max_rating:
            output.append(k)

    return(output)


getTopRatedFoodOutlets("Denver")