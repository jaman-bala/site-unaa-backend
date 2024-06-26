from typing import List
from ninja import Router

from backend.apps.rating.models import RegionCategories, RatingSchool
from backend.apps.rating.schemas import RegionCategoriesOUT, RatingSchoolOUT

router = Router()


@router.get("/regions", response=List[RegionCategoriesOUT])
def get_region(request):
    qs = RegionCategories.objects.all()
    return qs


@router.get("/rating", response=List[RatingSchoolOUT])
def get_rating(request):
    qs = RatingSchool.objects.all()
    return qs
