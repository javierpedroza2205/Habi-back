# -*- coding: utf-8 -*-
from myapp.models import Flat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import http


@csrf_exempt
def addFlat(request):
    """Add new flat

             Parameters
             ----------
                owner: `int`
                    Identified of the owner to whom it belongs.
                building: `int`
                    Identified of the building to which it belongs.
                department: `String`:
                    Number of flat.
            Returns
            -------
                httpresponse : `json`
                    json response with 200 code and success message.

            Notes
            -----
                All parameter are converted into the desired data type after reading (from request.POST).
    """
    owner = request.POST.get('owner')
    building = request.POST.get('building')
    department = request.POST.get('department')

    flat = Flat(
        owner_id=owner,
        building_id=building,
        department_number=department
    )

    try:
        flat.save()
        return JsonResponse({"message": "success"}, status=http.HTTPStatus.ACCEPTED, safe=False)
    except Exception as e:
        print(str(e))
        return JsonResponse({"message": "error"}, status=http.HTTPStatus.BAD_REQUEST, safe=False)