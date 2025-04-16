import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..main import app
from ..dependencies.database import get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_example(test_db):
    response = client.post(
        "/examples/",
        json={"name": "Test", "description": "Test description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test"
    assert "id" in data

def test_get_example(test_db):
    # First create an example
    create_response = client.post(
        "/examples/",
        json={"name": "Test Get", "description": "Test get description"}
    )
    example_id = create_response.json()["id"]
    
    # Then get it
    response = client.get(f"/examples/{example_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == example_id
    assert data["name"] == "Test Get"