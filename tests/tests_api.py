from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_health():
    response =  client.get('/health') 
    assert response.json() == {"status": "ok"}
    
def test_get_exercises():
    response =  client.get('/exercises') 
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_post_exercise():
    e = 'Rosca Martelo'
    response =  client.post(f'/exercises', json={'name': e}) 
    assert response.status_code in [200, 400]