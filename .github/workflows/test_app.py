
import app


def test_home():
    client = app.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Welcome to ShopEase!"


def test_prices():
    client = app.app.test_client()
    response = client.get("/prices")

    assert response.status_code == 200

    prices = response.get_json()
    assert "laptop" in prices
    assert "headphones" in prices
    assert "keyboard" in prices


def test_health():
    client = app.app.test_client()
    response = client.get("/health")

    assert response.status_code in (200, 503)
