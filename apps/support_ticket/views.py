from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from constants import SUPPORT_TICKET_PRIORITY, SUPPORT_TICKET_TYPE, SUPPORT_TICKET_STATUS
from .models import SupportTicket


@login_required()
def ticket_list(request, *args, **kwargs):
        if request.method == 'GET':
                tickets = request.user.support_tickets.all()
                context = {
                    'tickets': tickets,
                    'ticket_priority': SUPPORT_TICKET_PRIORITY,
                    'ticket_type': SUPPORT_TICKET_TYPE
                }
                return render(request, 'support_ticket/account-tickets.html', context)
        elif request.method == 'POST':
            data = dict(request.POST)
            data.pop('csrfmiddlewaretoken')
            ticket = SupportTicket.objects.create()
            for key, value in data.items():
                ticket.__setattr__(key, value[0])
            ticket.save()
            message = 'Ticket was successfully submitted'
            return redirect(request.META.get('HTTP_REFERER'), ticket=ticket, message=message)
