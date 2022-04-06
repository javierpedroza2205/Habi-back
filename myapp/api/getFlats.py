# -*- coding: utf-8 -*-
from myapp.models import Flat
from django.http import JsonResponse
import http


def getFlats(request):
    """ Get all flats

                 Parameters
                 ----------


                Returns
                -------
                    httpresponse : `json`
                        json response with 200 code and flats list.

                    if the model is empty the message is "empty model"

                Notes
                -----

    """
    flats = Flat.objects.all()
    response_list = []
    for flat in flats:
        data = {
            'id': flat.pk,
            'owner': flat.owner.name,
            'building': flat.building.address,
            'department_number': flat.department_number
        }
        response_list.append(data)

    if len(response_list) == 0:
        return JsonResponse({"message": "empty model"}, status=http.HTTPStatus.ACCEPTED, safe=False)
    else:
        return JsonResponse(response_list, status=http.HTTPStatus.ACCEPTED, safe=False)