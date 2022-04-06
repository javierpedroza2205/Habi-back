# -*- coding: utf-8 -*-
from myapp.models import Building, Flat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import http


@csrf_exempt
def deleteBuilding(request):
    """Delete building by id, if the building has flats those will also be eliminated

         Parameters
         ----------
            building_id: `string`
                Building identifiquer.

        Returns
        -------
            httpresponse : `json`
                json response with 200 code and success message

        Notes
        -----
            All parameter are converted into the desired data type after reading (from request.POST).
        """

    building_id = request.POST.get('building_id')
    try:
        building = Building.objects.get(pk=building_id)
        flats = Flat.objects.filter(building=building)
        effected_flats = len(flats)
    except Exception as e:
        print(str(e))
        if str(e) == "Building matching query does not exist.":
            return JsonResponse({"message": "Building doesnt exist"}, status=http.HTTPStatus.BAD_REQUEST, safe=False)

    try:
        building.delete()
        return JsonResponse({"message": "Flats delete " + str(effected_flats)},
                            status=http.HTTPStatus.ACCEPTED, safe=False)
    except Exception as e:
        print(str(e))
        return JsonResponse({"message": "error"}, status=http.HTTPStatus.BAD_REQUEST, safe=False)
