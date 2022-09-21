from django.shortcuts import render
from .models import EventTicket

def all_events(request):
    """ A view to return all events """
    events = EventTicket.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)
