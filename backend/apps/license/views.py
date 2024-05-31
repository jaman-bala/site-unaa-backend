from typing import List
from ninja import Router

from backend.apps.license.models import License
from backend.apps.license.models import Documents
from backend.apps.license.models import DocumentsNPA
from backend.apps.license.models import DopDoc
from backend.apps.license.models import RegionCategories
from backend.apps.license.models import RatingSchool

from backend.apps.license.schemas import LicenseOUT
from backend.apps.license.schemas import DocumentsOUT
from backend.apps.license.schemas import DocumentsNPAOUT
from backend.apps.license.schemas import DopDocSchemasOUT
from backend.apps.license.schemas import RegionCategoriesOUT
from backend.apps.license.schemas import RatingSchoolOUT


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
def get_rating():
    qs = RatingSchool.objects.all()
    return [RatingSchoolOUT.from_orm(rating) for rating in qs]

