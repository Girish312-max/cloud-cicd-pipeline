from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Cloud-Based CI/CD Pipeline" in response.data
    assert b"Application is Running" in response.data


def test_health_check():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "Cloud-Based CI/CD Pipeline"
    assert data["version"] == "2.0"