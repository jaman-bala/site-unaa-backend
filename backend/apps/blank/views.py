from typing import List
from ninja import Router

from backend.apps.blank.documents import VisualDocuments, BusinessContact
from backend.apps.blank.models import PDF, RegionCategories, RatingSchool
from backend.apps.blank.schemas import PDFOut, VisualDocumentsSchemasOUT, BusinessContactSchemasOUT, \
    RegionCategoriesOUT, RatingSchoolOUT

router = Router()


@router.get("/sample", response=List[PDFOut])
def get_pdf(request):
    qs = PDF.objects.all()
    return qs


@router.get("/props", response=List[VisualDocumentsSchemasOUT])
def get_props(request):
    qs = VisualDocuments.objects.all()
    return qs


@router.get("/contact", response=List[BusinessContactSchemasOUT])
def get_contact(request):
    qs = BusinessContact.objects.all()
    return qs


@router.get("/regions", response=List[RegionCategoriesOUT])
def get_region(request):
    qs = RegionCategories.objects.all()
    return qs


@router.get("/rating", response=List[RatingSchoolOUT])
def get_rating(request):
    qs = RatingSchool.objects.all()
    return [RatingSchoolOUT.from_orm(rating) for rating in qs]