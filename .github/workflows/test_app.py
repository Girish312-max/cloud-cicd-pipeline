from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Cloud-Based CI/CD Pipeline" in response.data
    assert b"Application is Running" in response.data