from requests import get, post, delete

print(get('http://localhost:5000/api/v2/jobs').json())
print(post('http://localhost:5000/api/v2/jobs',
           json={
               'team_leader': 1,
               'job': 'researching of hecliptic rules',
               'work_size': 15,
               'collaborators': '1, 2, 3',
               'is_finished': True
           }).json())
print(get('http://localhost:5000/api/v2/jobs/6').json())
print(delete('http://localhost:5000/api/v2/jobs/6').json())
print(delete('http://localhost:5000/api/v2/jobs/sdf').json())
print(delete('http://localhost:5000/api/v2/jobs/63434').json())
print(get('http://localhost:5000/api/v2/jobs/633434').json())
print(get('http://localhost:5000/api/v2/jobs/dsf').json())
