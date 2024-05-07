from typing import List
from ninja import Router

from backend.apps.license.models import License
from backend.apps.license.schemas import LicenseOUT

router = Router()


@router.get("/", response=List[LicenseOUT])
def get_license(request):
    qs = License.objects.all()
    return qs
