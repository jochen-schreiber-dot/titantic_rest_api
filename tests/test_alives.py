import requests

def test_alives():
    url = "http://127.0.0.1:8002/alives/0"
    response = requests.get(url)
    
    assert response.status_code == 200 
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()  
    assert isinstance(data, dict)
    assert "alive_id" in data
    assert "alive" in data