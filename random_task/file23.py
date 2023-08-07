movies = [
    {"name": "Zack", "yearOfBirth": 2018},
    {"name": "Zack", "yearOfBirth": 2017},
    {"name": "Zack", "yearOfBirth": 2016},
    {"name": "Zack", "yearOfBirth": 2015},
    {"name": "Zack", "yearOfBirth": 2014},
    {"name": "Zack", "yearOfBirth": 2013}
]


movies.sort(key=lambda movie: movie['yearOfBirth'])
print(movies)