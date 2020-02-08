from django.shortcuts import render


def ticket_list(request, *args, **kwargs):
    if request.method == 'GET':
        if request.user.is_authenticated:
            tickets = request.user.support_tickets.all()
            context = {
                'tickets': tickets
            }
            return render(request, 'support_ticket/account-tickets.html', context)
