from django.shortcuts import render
from typing import List
from ninja import Router
from backend.apps.job.models import Job
from backend.apps.job.schemas import JobOUT


router = Router()


@router.get("/jobs", response=List[JobOUT])
def get_job(request):
    qs = Job.objects.all()
    return qs