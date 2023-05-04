from django.shortcuts import render
from .models import ServerInformation, ServerInformation_15m, ServerInformation_30m, ServerInformation_1h, ServerInformation_6h, ServerInformation_24h
from rest_framework.views import APIView
from rest_framework.response import Response


def MainAbout(request):
    return render(request, 'About/about_main.html')


def MainServer(request):
    context = {'a': 1}
    return render(request, 'About/server/main_server.html', context)


def ServerComponents(request):
    return render(request, 'About/server/server_сomponents.html')


class ServerInformationView(APIView):
    def get(self, request):
        try:
            id = ServerInformation.objects.last().id
            id_count = 0

            cpu_list = []
            cpu_freq_list = []
            ram_list = []
            date_list = []
            time_list = []
            while True:
                try:
                    cpu_list.append(ServerInformation.objects.get(id=id - 30 + id_count).cpu)
                    cpu_freq_list.append(ServerInformation.objects.get(id=id - 30 + id_count).cpu_freq)
                    ram_list.append(ServerInformation.objects.get(id=id - 30 + id_count).ram)
                    date_list.append(ServerInformation.objects.get(id=id - 30 + id_count).date)
                    time_boof = ServerInformation.objects.get(id=id - 30 + id_count).time
                    right_time = time_boof.strftime('%H:%M:%S')
                    time_list.append(right_time)
                except ServerInformation.DoesNotExist:
                    pass

                id_count += 1

                if id_count >= 30:
                    break

            context_5m = {'cpu': cpu_list, 'cpu_freq': cpu_freq_list, 'ram': ram_list, 'date': date_list, 'time': time_list}
        except:
            context_5m = {}

        try:
            id = ServerInformation_15m.objects.last().id
            id_count = 0

            cpu_list = []
            cpu_freq_list = []
            ram_list = []
            date_list = []
            time_list = []
            while True:
                try:
                    cpu_list.append(ServerInformation_15m.objects.get(id=id - 30 + id_count).cpu)
                    cpu_freq_list.append(ServerInformation_15m.objects.get(id=id - 30 + id_count).cpu_freq)
                    ram_list.append(ServerInformation_15m.objects.get(id=id - 30 + id_count).ram)
                    date_list.append(ServerInformation_15m.objects.get(id=id - 30 + id_count).date)
                    time_boof = ServerInformation_15m.objects.get(id=id - 30 + id_count).time
                    right_time = time_boof.strftime('%H:%M:%S')
                    time_list.append(right_time)
                except ServerInformation_15m.DoesNotExist:
                    pass

                id_count += 1

                if id_count >= 30:
                    break

            context_15m = {'cpu': cpu_list, 'cpu_freq': cpu_freq_list, 'ram': ram_list, 'date': date_list, 'time': time_list}
        except:
            context_15m = {}


        try:
            id = ServerInformation_30m.objects.last().id
            id_count = 0

            cpu_list = []
            cpu_freq_list = []
            ram_list = []
            date_list = []
            time_list = []
            while True:
                try:
                    cpu_list.append(ServerInformation_30m.objects.get(id=id - 30 + id_count).cpu)
                    cpu_freq_list.append(ServerInformation_30m.objects.get(id=id - 30 + id_count).cpu_freq)
                    ram_list.append(ServerInformation_30m.objects.get(id=id - 30 + id_count).ram)
                    date_list.append(ServerInformation_30m.objects.get(id=id - 30 + id_count).date)
                    time_boof = ServerInformation_30m.objects.get(id=id - 30 + id_count).time
                    right_time = time_boof.strftime('%H:%M:%S')
                    time_list.append(right_time)
                except ServerInformation_30m.DoesNotExist:
                    pass

                id_count += 1

                if id_count >= 30:
                    break

            context_30m = {'cpu': cpu_list, 'cpu_freq': cpu_freq_list, 'ram': ram_list, 'date': date_list, 'time': time_list}
        except:
            context_30m = {}


        try:
            id = ServerInformation_1h.objects.last().id
            id_count = 0

            cpu_list = []
            cpu_freq_list = []
            ram_list = []
            date_list = []
            time_list = []
            while True:
                try:
                    cpu_list.append(ServerInformation_1h.objects.get(id=id - 30 + id_count).cpu)
                    cpu_freq_list.append(ServerInformation_1h.objects.get(id=id - 30 + id_count).cpu_freq)
                    ram_list.append(ServerInformation_1h.objects.get(id=id - 30 + id_count).ram)
                    date_list.append(ServerInformation_1h.objects.get(id=id - 30 + id_count).date)
                    time_boof = ServerInformation_1h.objects.get(id=id - 30 + id_count).time
                    right_time = time_boof.strftime('%H:%M:%S')
                    time_list.append(right_time)
                except ServerInformation_1h.DoesNotExist:
                    pass

                id_count += 1

                if id_count >= 30:
                    break

            context_1h = {'cpu': cpu_list, 'cpu_freq': cpu_freq_list, 'ram': ram_list, 'date': date_list, 'time': time_list}
        except:
            context_1h = {}

        try:
            id = ServerInformation_6h.objects.last().id
            id_count = 0

            cpu_list = []
            cpu_freq_list = []
            ram_list = []
            date_list = []
            time_list = []
            while True:
                try:
                    cpu_list.append(ServerInformation_6h.objects.get(id=id - 30 + id_count).cpu)
                    cpu_freq_list.append(ServerInformation_6h.objects.get(id=id - 30 + id_count).cpu_freq)
                    ram_list.append(ServerInformation_6h.objects.get(id=id - 30 + id_count).ram)
                    date_list.append(ServerInformation_6h.objects.get(id=id - 30 + id_count).date)
                    time_boof = ServerInformation_6h.objects.get(id=id - 30 + id_count).time
                    right_time = time_boof.strftime('%H:%M:%S')
                    time_list.append(right_time)
                except ServerInformation_6h.DoesNotExist:
                    pass

                id_count += 1

                if id_count >= 30:
                    break

            context_6h = {'cpu': cpu_list, 'cpu_freq': cpu_freq_list, 'ram': ram_list, 'date': date_list, 'time': time_list}
        except:
            context_6h = {}


        try:
            id = ServerInformation_24h.objects.last().id
            id_count = 0

            cpu_list = []
            cpu_freq_list = []
            ram_list = []
            date_list = []
            time_list = []
            while True:
                try:
                    cpu_list.append(ServerInformation_24h.objects.get(id=id - 30 + id_count).cpu)
                    cpu_freq_list.append(ServerInformation_24h.objects.get(id=id - 30 + id_count).cpu_freq)
                    ram_list.append(ServerInformation_24h.objects.get(id=id - 30 + id_count).ram)
                    date_list.append(ServerInformation_24h.objects.get(id=id - 30 + id_count).date)
                    time_boof = ServerInformation_24h.objects.get(id=id - 30 + id_count).time
                    right_time = time_boof.strftime('%H:%M:%S')
                    time_list.append(right_time)
                except ServerInformation_24h.DoesNotExist:
                    pass

                id_count += 1

                if id_count >= 30:
                    break

            context_24h = {'cpu': cpu_list, 'cpu_freq': cpu_freq_list, 'ram': ram_list, 'date': date_list, 'time': time_list}
        except:
            context_24h = {}

        context_final = {'5m': context_5m, '15m': context_15m, '30m': context_30m, '1h': context_1h, '6h': context_6h, '24h': context_24h}
        return Response(context_final)
