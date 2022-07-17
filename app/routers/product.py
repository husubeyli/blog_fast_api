from itertools import product
from fastapi import APIRouter, Depends, Response

from db.databse import get_db


router = APIRouter(
    prefix="/products",
    tags=["products"],
)


products = ['wathc', 'camera', 'phone']

@router.get('/all')
async def get_all_products():
    data = ' '.join(products)
    return Response(content=data, media_type='text/plain')