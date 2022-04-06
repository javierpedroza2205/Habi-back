# -*- coding: utf-8 -*-
from myapp.models import Building
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import http


@csrf_exempt
def addBuilding(request):
    """Add new building

         Parameters
         ----------
            area: `float`
                Area in meters that make up a building.
            number_rooms: `float`
                Number of rooms in a building.
            price: `float`:
                price of a building.
            address: `String`
                Address of the building.
            town: `String`
                Town of the building.
        Returns
        -------
            httpresponse : `json`
                json response with 200 code and success message.

        Notes
        -----
            All parameter are converted into the desired data type after reading (from request.POST).
    """

    area = request.POST.get('area')
    number_rooms = request.POST.get('number_rooms')
    price = request.POST.get('price')
    address = request.POST.get('address')
    town = request.POST.get('town')

    building = Building(
        area=area,
        number_rooms=number_rooms,
        price=price,
        address=address,
        town=town
    )

    try:
        building.save()
        return JsonResponse({"message": "success"}, status=http.HTTPStatus.ACCEPTED, safe=False)
    except Exception as e:
        print(str(e))
        return JsonResponse({"message": "error"}, status=http.HTTPStatus.BAD_REQUEST, safe=False)
