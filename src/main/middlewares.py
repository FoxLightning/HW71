import datetime
from time import time


from .models import GoogleLead, Logger


class GoogleLeadMid:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        gclid = request.GET.get('gclid')
        if gclid is not None:
            qset = GoogleLead.objects.filter(value=gclid)
            if not qset.exists():
                GoogleLead.objects.create(value=gclid)
            else:
                qset.update(updated_at=datetime.datetime.now())

        response = self.get_response(request)
        return response


class LoggerSave:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        r_time = time() - start

        Logger.objects.create(
            method=request.method,
            path=request.path,
            response_time=r_time
        )
        return response
