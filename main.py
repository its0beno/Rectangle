from fastapi import FastAPI, HTTPException, Depends
from typing import List
from models import Rectangle
from database import get_db
from sqlalchemy.orm import Session
from schemas import Segment
from sqlalchemy import and_, or_

app = FastAPI()


@app.post("/intersect/", response_model=List[Segment])
async def intersect_segments(
    segment: Segment, db: Session = Depends(get_db)
) -> List[Rectangle]:
    try:
        # Define conditions for intersection along x-axis and y-axis
        x_condition = or_(
            and_(Rectangle.x1 <= segment.x1, Rectangle.x2 >= segment.x1),
            and_(Rectangle.x1 <= segment.x2, Rectangle.x2 >= segment.x2),
        )
        y_condition = or_(
            and_(Rectangle.y1 <= segment.y1, Rectangle.y2 >= segment.y1),
            and_(Rectangle.y1 <= segment.y2, Rectangle.y2 >= segment.y2),
        )

        # Combine x-axis and y-axis conditions using AND operator
        intersection_condition = and_(x_condition, y_condition)

        # Query rectangles intersecting the input segment by any of the edges
        intersecting_rectangles = (
            db.query(Rectangle).filter(intersection_condition).all()
        )

        return intersecting_rectangles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
