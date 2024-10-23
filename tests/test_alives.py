import requests

def test_alives():
    url = "http://127.0.0.1:8002/alives/0"  # Replace with your mock API URL
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200 

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json"

    data = response.json()  
    assert isinstance(data, dict)
    assert "alive_id" in data
    assert "alive" in data