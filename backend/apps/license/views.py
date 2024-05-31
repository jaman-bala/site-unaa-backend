from typing import List
from ninja import Router

from backend.apps.license.models import License
from backend.apps.license.models import Documents
from backend.apps.license.models import DocumentsNPA
from backend.apps.license.models import DopDoc
from backend.apps.license.models import RegionCategories
from backend.apps.license.models import RatingSchool
from backend.apps.license.documents import VisualDocuments
from backend.apps.license.documents import BusinessContact

from backend.apps.license.schemas import LicenseOUT
from backend.apps.license.schemas import DocumentsOUT
from backend.apps.license.schemas import DocumentsNPAOUT
from backend.apps.license.schemas import DopDocSchemasOUT
from backend.apps.license.schemas import RegionCategoriesOUT
from backend.apps.license.schemas import RatingSchoolOUT
from backend.apps.license.schemas import VisualDocumentsSchemasOUT
from backend.apps.license.schemas import BusinessContactSchemasOUT


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


@router.get("/props", response=List[VisualDocumentsSchemasOUT])
def get_props(request):
    qs = VisualDocuments.objects.all()
    return qs


@router.get("/contact", response=List[BusinessContactSchemasOUT])
def get_contact(request):
    qs = BusinessContact.objects.all()
    return qs

