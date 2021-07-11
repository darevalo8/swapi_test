# SW API GraphQL

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/gustav0/swapi.git
```

Move into de repo and install dependencies
```
pip install -r requirements.txt
```

Run migrations and load fixtures
```
python manage.py migrate
python manage.py load_fixtures
```

### Running the server
```
python manage.py runserver
```
If you want to check it out, access the graphi explorer here: `127.0.0.1:8000/explore`.

The service should be available in the URL: `127.0.0.1:8000/graphql`.

### Runing the tests
```
python manage.py test
```
### Algunos ejemplos de querys

```
//Listado de los personajes
query{
  allPeople{
    edges{
      node{
        id
        name
        hairColor
        skinColor
        eyeColor
        homeWorld{
          id
          name
        }
      }
    }
  }
}
```
```
// Añadir y actualizar personaje

mutation{
  addPeople(input:{name:"Daniel", gender:"male", 
    planetName: "Naboo", hairColor: "blond", skinColor:"fair", 
    eyeColor: "yellow", height: "1.80", mass:"67", birthYear: "08-04-1995"}){
    people{
      name
      eyeColor
      hairColor
      homeWorld{
        name
      }
    }
  }
}

mutation{
  addPeople(input:{name:"Daniel Alejandro", gender:"male", 
    planetName: "Naboo", hairColor: "blond", skinColor:"fair", 
    eyeColor: "yellow", height: "1.80", mass:"67", birthYear: "08-04-1995", id: "UGVvcGxlVHlwZTo4OQ=="}){
    people{
      name
      eyeColor
      hairColor
      homeWorld{
        name
      }
    }
  }
}
```

### Variables de entorno

hay un archivo env.example el cual contiene el nombre de
la variable para el secret key es renombrar de .env.example a .env y asigna un codigo seguro