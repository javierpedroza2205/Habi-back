# -*- coding: utf-8 -*-
from myapp.models import Building
from django.http import JsonResponse
import http


def getBuildings(request, **Karws):
    """ Get all Buildings

        Parameters
        ----------
            descending: `int = 1 or 0`
                If the value is 1: descending is true then order is Z-A or by old created date.
                else: descending is true then order is A-Z or by the most recently created.
            number_rooms: `string = town or created`
                If the value is = town: take value by order town's name.
                else: value is created: take value by order created date.

        Returns
        -------
            httpresponse : `json`
                json response with 200 code and flats list.
                if the model is empty the message is "empty model"

        Notes
        -----
            All parameter are converted into the parmas by get request.
    """
    # validate filters
    order_parameter = request.GET['order']
    if int(request.GET['descending']) == 1:
        order_parameter = "-" + order_parameter
    buildings = Building.objects.all().order_by(order_parameter)
    response_list = []
    for building in buildings:
        data = {
            'id': building.pk,
            'area': building.area,
            'number_rooms': building.number_rooms,
            'price': building.price,
            'address': building.address,
            'created': building.created,
            'town': building.town
        }
        response_list.append(data)
    if len(response_list) == 0:
        return JsonResponse({"message": "empty model"}, status=http.HTTPStatus.ACCEPTED, safe=False)
    else:
        return JsonResponse(response_list, status=http.HTTPStatus.ACCEPTED, safe=False)







