from typing import List
from django.shortcuts import get_object_or_404
from ninja import Router

from backend.apps.about.schemas import HistorySchemOUT, ManagementOUT, ContactOUT
from backend.apps.about.models import History, Management, Contact

router = Router()


@router.get("/history", response=List[HistorySchemOUT])
def get_all_history(request):
    qs = History.objects.all()
    return [HistorySchemOUT.from_orm(history).dict() for history in qs]


@router.get("/management", response=List[ManagementOUT])
def get_all_management(request):
    qs = Management.objects.all()
    return [ManagementOUT.from_orm(management).dict() for management in qs]


@router.get("/contact", response=List[ContactOUT])
def get_all_contact(request):
    qs = Contact.objects.all()
    return qs


@router.get("/contact/{contact_pk}", response=ContactOUT)
def get_contact_pk(request, contact_pk: int):
    qs = get_object_or_404(Contact, id=contact_pk)
    return qs
