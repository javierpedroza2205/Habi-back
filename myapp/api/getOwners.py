# -*- coding: utf-8 -*-
from myapp.models import Owner
from django.http import JsonResponse
import http


def getOwners(request):
    """ Get all owners

             Parameters
             ----------


            Returns
            -------
                httpresponse : `json`
                    json response with 200 code and owners list.

                if the model is empty the message is "empty model"

            Notes
            -----

    """
    owners = Owner.objects.all()
    response_list = []
    for owner in owners:
        data = {
            'id': owner.pk,
            'name': owner.name,
            'phone': owner.phone,
            'email': owner.email
        }
        response_list.append(data)
    if len(response_list) == 0:
        return JsonResponse({"message": "empty model"}, status=http.HTTPStatus.ACCEPTED, safe=False)
    else:
        return JsonResponse(response_list, status=http.HTTPStatus.ACCEPTED, safe=False)