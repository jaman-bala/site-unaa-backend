from typing import List
from ninja import Router

from backend.apps.license.models import License, Documents, DocumentsNPA
from backend.apps.license.file import PDF
from backend.apps.license.schemas import LicenseOUT, DocumentsOUT, DocumentsNPAOUT, PDFOut

router = Router()


@router.get("/", response=List[DocumentsOUT])
def get_documents(request):
    qs = Documents.objects.all()
    return qs


@router.get("/sample", response=List[PDFOut])
def get_pdf(request):
    qs = PDF.objects.all()
    return qs


@router.get("/npa", response=List[DocumentsNPAOUT])
def get_documents_npa(request):
    qs = DocumentsNPA.objects.all()
    return qs


@router.get("/car", response=List[LicenseOUT])
def get_license(request):
    qs = License.objects.all()
    return qs




