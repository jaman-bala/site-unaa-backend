from typing import List
from ninja import Router

from backend.apps.blank.models import PDF
from backend.apps.blank.schemas import PDFOut

router = Router()


@router.get("/sample", response=List[PDFOut])
def get_pdf(request):
    qs = PDF.objects.all()
    return qs
