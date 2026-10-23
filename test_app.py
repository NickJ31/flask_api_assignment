from app import app


def test_home():
    tester = app.test_client()
    response = tester.get("/")

    assert response.status_code == 200
    assert b"My Flask API is working!" in response.data


def test_hello_default():
    tester = app.test_client()
    response = tester.get("/hello")

    assert response.status_code == 200
    assert b"Hello, World!" in response.data


def test_hello_with_name():
    tester = app.test_client()
    response = tester.get("/hello?name=Nicholas")

    assert response.status_code == 200
    assert b"Hello, Nicholas!" in response.data


def test_sum_success():
    tester = app.test_client()

    response = tester.post(
        "/sum",
        json={
            "numbers": [
                1,
                2,
                3,
                4,
                5,
            ]
        },
    )

    assert response.status_code == 200
    assert response.get_json() == {"sum": 15}

    def test_sum_missing_numbers():
        tester = app.test_client()

        response = tester.post("/sum", json={})

        assert response.status_code == 400
        assert response.get_json() == {"error": "Numbers must be a list"}

    def test_sum_invalid_numbers():
        tester = app.test_client()

        response = tester.post("/sum", json={"numbers": [1, "two", 3]})

        assert response.status_code == 400


def test_sum_missing_numbers():
    tester = app.test_client()
    response = tester.post("/sum", json={})

    assert response.status_code == 400


def test_sum_invalid_numbers():
    tester = app.test_client()
    response = tester.post("/sum", json={"numbers": [1, "two", 3]})

    assert response.status_code == 400
