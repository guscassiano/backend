from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import movie as models
from ..schemas import movie as schemas

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.MovieBase)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.get("/", response_model=list[schemas.MovieBase])
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(models.Movie).all()
    return movies

@router.get("/{movie_id}", response_model=schemas.MovieBase)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/{movie_id}", response_model=schemas.MovieBase)
def update_movie(movie_id: int, movie_update: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    for key, value in movie_update.model_dump().items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.patch("/{movie_id}", response_model=schemas.MovieBase)
def patch_movie(movie_id: int, movie_update: schemas.MovieUpdate, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = movie_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_movie, key, value)

    db.commit()
    db.refresh(db_movie)
    return db_movie

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    del_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if del_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(del_movie)
    db.commit()