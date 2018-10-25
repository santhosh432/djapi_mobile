from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def homepage(request):

    response = {"users": [
        {
            "CustomerPhoneNumber": "812934", "Channel": "Mail", "CreatedDate": "2018-10-23 10:50", "Status": "Pending",
            "CustomerEmail": "IBSDepTest G<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "No Action",
            "Intent": "Retroclaim",
            "Prompted": "false"
        },
        {
            "CustomerPhoneNumber": "8129342", "Channel": "Mail2", "CreatedDate": "2018-10-23 10:50",
            "Status": "Pending", "CustomerEmail": "IBSDepTestA<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "book again",
            "Intent": "Retroclaim",
            "Prompted": "false"
        },
        {
            "CustomerPhoneNumber": "81293423", "Channel": "Mail3", "CreatedDate": "2018-10-23 10:50",
            "Status": "Pending", "CustomerEmail": "IBSDepTest B<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "wait for 10minutes",
            "Intent": "Retroclaim",
            "Prompted": "false"
        },
        {
            "CustomerPhoneNumber": "81293425", "Channel": "Mail5", "CreatedDate": "2018-10-23 10:50",
            "Status": "Pending", "CustomerEmail": "IBSDepTest C<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "payment to be made",
            "Intent": "Retroclaim",
            "Prompted": "false"
        },
        {
            "CustomerPhoneNumber": "8129346", "Channel": "Mail6", "CreatedDate": "2018-10-23 10:50",
            "Status": "Pending", "CustomerEmail": "IBSDepTest D<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "No Action required",
            "Intent": "Retroclaim",
            "Prompted": "false"
        },
        {
            "CustomerPhoneNumber": "81293427", "Channel": "Mail7", "CreatedDate": "2018-10-23 10:50",
            "Status": "Pending", "CustomerEmail": "IBSDepTest E<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "try again",
            "Intent": "Retroclaim",
            "Prompted": "false"
        },
        {
            "CustomerPhoneNumber": "81293427", "Channel": "Mail7", "CreatedDate": "2018-10-23 10:50",
            "Status": "Pending", "CustomerEmail": "IBSDepTest E<ibsdeptest@gmail.com>",
            "IntentDescription": "Retroclaim Missed Points Request", "StatusDescription": "description",
            "IntentInputs": [{"Source": "HND", "Destination": "SYD", "Date": "05-Apr-2019"}],
            "CustomerName": "MailbotAdmin", "UpdatedDate": "2018-10-23 10:50", "Action": "try again",
            "Intent": "Retroclaim",
            "Prompted": "false"
        }
    ]}
    args = {}
    ctx = {}
    li  = []
    if 'submit' in request.GET:
        args['contents'] = response
        mob = request.GET.get('mob')
        # print(args)
        for k, l in list(args['contents'].items()):
            for s in l:
                if (s['CustomerPhoneNumber'] == mob):
                    # ctx = {'user': s}
                    # print(s)
                    li.append(s)
                    # print(ctx)
        ctx = {'op':li}
    return render(request, 'home.html', ctx)
