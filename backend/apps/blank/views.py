from typing import List
from ninja import Router

from backend.apps.blank.documents import VisualDocuments, BusinessContact
from backend.apps.blank.models import PDF
from backend.apps.blank.schemas import PDFOut, VisualDocumentsSchemasOUT, BusinessContactSchemasOUT

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

