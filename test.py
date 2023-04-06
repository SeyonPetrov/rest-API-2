from requests import get, post, delete

print(get('http://localhost:5000/api/v2/users').json())
print(post('http://localhost:5000/api/v2/users',
           json={
               'surname': 'Lord',
               'name': 'Drol',
               'age': 34,
               'position': 'locomotive',
               'speciality': 'scientist',
               'address': 'module_4',
               'email': 'roma@mail.tu',
               'hashed_password': 'dmwjknedkwndkwnkfbwefb'
           }).json())
print(get('http://localhost:5000/api/v2/users/1').json())
print(get('http://localhost:5000/api/v2/users/tt').json())
print(get('http://localhost:5000/api/v2/users/343434').json())
print(delete('http://localhost:5000/api/v2/users/1').json())
print(delete('http://localhost:5000/api/v2/users/tt').json())
print(delete('http://localhost:5000/api/v2/users/143634').json())
