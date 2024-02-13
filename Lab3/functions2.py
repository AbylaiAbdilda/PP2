# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# ex 1
def score(x):
    if movies[x]["imdb"] > 5.5:
        return True
    else:
        return False
num = int(input())
print(score(num))

# ex 2

def List():
    i = 0
    lis1 = []
    while i < len(movies):
        if int(movies[i]["imdb"]) > 5.5:
            lis1.append(movies[i]["name"])
        i +=1
    print(lis1)
List() 

# ex 3

def ctr(a):
    List = []
    for x in movies:
        if x["category"]==a:
            List.append(x["name"])
    print(List)

a = str(input())
ctr(a)

# ex 4

def avr():
    sum = 0 
    for x in movies:
        sum+=x['imdb']
    print(sum/len(movies))

avr()

# ex 5

def avr(a):
    sum = 0
    i = 0 
    for x in movies:
        if x["category"]== a:
            sum+=x['imdb']
            i+=1
    print(sum/i)
    
a=str(input())
avr(a)