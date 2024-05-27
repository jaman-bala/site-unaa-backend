from typing import List
from ninja import Router

from backend.apps.license.models import License, Documents, DocumentsNPA
from backend.apps.license.schemas import LicenseOUT, PdfOUT, DocumentsOUT, DocumentsNPAOUT
from backend.apps.license.pdf import PdfGet

router = Router()


@router.get("/", response=List[DocumentsOUT])
def get_documents(request):
    qs = Documents.objects.all()
    return qs


@router.get("/sample", response=List[PdfOUT])
def get_pdf(request):
    qs = PdfGet.objects.all()
    return qs


@router.get("/npa", response=List[DocumentsNPAOUT])
def get_documents_npa(request):
    qs = DocumentsNPA.objects.all()
    return qs


@router.get("/car", response=List[LicenseOUT])
def get_license(request):
    qs = License.objects.all()
    return qs




