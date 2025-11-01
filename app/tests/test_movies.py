import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def client():
    """Creates a new database and FastAPI test client for each test function."""
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)


def create_movie(client):
    """Creates a sample movie and returns the API response (POST /movies/)."""
    response = client.post(
        "/movies/",
        json={
            "title": "Star Wars V: O Império Contra-Ataca",
            "director": "George Lucas",
            "release_year": 1980,
            "genre": "Fantasia",
            "rating": 9.1,
        },
    )

    return response


def test_create_movie(client):
    """Tests successful movie creation (POST /movies/)."""
    response = create_movie(client)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Star Wars V: O Império Contra-Ataca"
    assert data["director"] == "George Lucas"
    assert data["release_year"] == 1980
    assert data["genre"] == "Fantasia"
    assert data["rating"] == 9.1


def test_read_movies_empty_list(client):
    """Tests that the movies list is empty initially (GET /movies/)."""
    response = client.get("/movies/")

    assert response.status_code == 200
    assert response.json() == []


def test_read_movie_after_creation(client):
    """Tests that the movies list returns the created movie (GET /movies/)."""
    create_movie(client)

    response = client.get("/movies/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Star Wars V: O Império Contra-Ataca"


def test_read_movie_by_id(client):
    """Tests retrieving a movie by its ID (GET /movies/{id})."""
    create_response = create_movie(client)
    movie_id = create_response.json()["id"]

    response = client.get(f"/movies/{movie_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Star Wars V: O Império Contra-Ataca"
    assert data["id"] == movie_id


def test_read_movie_not_found(client):
    """Tests retrieving a non-existent movie returns 404 (GET /movies/{id})."""
    response = client.get("/movies/9999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Movie not found"}


def test_update_movie(client):
    """Tests a full movie update (PUT /movies/{id})."""
    create_response = create_movie(client)
    movie_id = create_response.json()["id"]

    update_response = client.put(
        f"/movies/{movie_id}",
        json={
            "title": "Exterminador do Futuro 2: O Julgamento Final",
            "director": "James Cameron",
            "release_year": 1991,
            "genre": "Ficção Científica",
            "rating": 8.9,
        },
    )

    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Exterminador do Futuro 2: O Julgamento Final"
    assert data["release_year"] == 1991
    assert data["rating"] == 8.9


def test_patch_movie(client):
    """Tests a partial movie update (PATCH /movies/{id})."""
    create_response = create_movie(client)
    movie_id = create_response.json()["id"]

    patch_response = client.patch(
        f"/movies/{movie_id}",
        json={
            "rating": 9.0,
        },
    )

    assert patch_response.status_code == 200
    data = patch_response.json()
    assert data["title"] == "Star Wars V: O Império Contra-Ataca"
    assert data["rating"] == 9.0


def test_delete_movie_not_implemented(client):
    """Tests that the movie deletion endpoint works (DELETE /movies/{id})."""
    create_response = create_movie(client)
    movie_id = create_response.json()["id"]

    delete_response = client.delete(f"/movies/{movie_id}")

    assert delete_response.status_code == 204
