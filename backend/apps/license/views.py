from typing import List
from ninja import Router

from backend.apps.license.models import License, Documents, DocumentsNPA, DopDoc, RegionCategories, RatingSchool
from backend.apps.license.schemas import LicenseOUT, DocumentsOUT, DocumentsNPAOUT, DopDocSchemasOUT, RegionCategoriesOUT, RatingSchoolOUT

router = Router()


@router.get("/", response=List[DocumentsOUT])
def get_documents(request):
    qs = Documents.objects.all()
    return qs


@router.get("/npa", response=List[DocumentsNPAOUT])
def get_documents_npa(request):
    qs = DocumentsNPA.objects.all()
    return qs


@router.get("/car", response=List[LicenseOUT])
def get_license(request):
    qs = License.objects.all()
    return qs


@router.get("/regions", response=List[RegionCategoriesOUT])
def get_region(request):
    qs = RegionCategories.objects.all()
    return qs


@router.get("/doc/req", response=List[DopDocSchemasOUT])
def get_dop(request):
    qs = DopDoc.objects.all()
    return qs


@router.get("/rating", response=List[RatingSchoolOUT])
def get_rating(request):
    qs = RatingSchool.objects.all()
    return qs
