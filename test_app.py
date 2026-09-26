import pytest

from app import app, deployments


@pytest.fixture(autouse=True)
def reset_deployments():
    """Reset in-memory data before and after every test."""
    deployments.clear()
    deployments.append(
        {
            "id": 1,
            "application": "Cloud CI/CD App",
            "environment": "Production",
            "version": "2.0",
            "status": "Deployed",
        }
    )

    yield

    deployments.clear()


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "ok"
    assert "commit" in data


def test_add_deployment():
    client = app.test_client()

    response = client.post(
        "/deployments",
        data={
            "application": "Student Portal",
            "environment": "Staging",
            "version": "2.1",
            "status": "Pending",
        },
    )

    assert response.status_code == 302
    assert len(deployments) == 2

    added = deployments[-1]

    assert added["application"] == "Student Portal"
    assert added["environment"] == "Staging"
    assert added["version"] == "2.1"
    assert added["status"] == "Pending"


def test_invalid_deployment_rejected():
    client = app.test_client()

    response = client.post(
        "/deployments",
        data={
            "application": "Invalid App",
            "environment": "WrongEnvironment",
            "version": "1.0",
            "status": "Pending",
        },
    )

    assert response.status_code == 400
    assert len(deployments) == 1


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Cloud Deployment Tracker" in response.data
    assert b"Add Deployment" in response.data
    assert b"Cloud CI/CD App" in response.data
