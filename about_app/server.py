import threading
import datetime
import psutil


def periodic_task_5m():
    threading.Timer(interval=10.0, function=periodic_task_5m).start()

    from .models import ServerInformation

    data = ServerInformation(cpu=int(round(psutil.cpu_percent(5))), cpu_freq=int(round(psutil.cpu_freq().current)), ram=int(round(psutil.virtual_memory().percent)))
    data.save()


threading.Timer(interval=10.0, function=periodic_task_5m).start()


def periodic_task_15m():
    threading.Timer(interval=30.0, function=periodic_task_15m).start()

    from .models import ServerInformation_15m

    data = ServerInformation_15m(cpu=int(round(psutil.cpu_percent(15))), cpu_freq=int(round(psutil.cpu_freq().current)), ram=int(round(psutil.virtual_memory().percent)))
    data.save()


threading.Timer(interval=30.0, function=periodic_task_15m).start()


def periodic_task_30m():
    threading.Timer(interval=60.0, function=periodic_task_30m).start()

    from .models import ServerInformation_30m

    data = ServerInformation_30m(cpu=int(round(psutil.cpu_percent(30))), cpu_freq=int(round(psutil.cpu_freq().current)), ram=int(round(psutil.virtual_memory().percent)))
    data.save()


threading.Timer(interval=60.0, function=periodic_task_30m).start()


def periodic_task_1h():
    threading.Timer(interval=120.0, function=periodic_task_1h).start()

    from .models import ServerInformation_1h

    data = ServerInformation_1h(cpu=int(round(psutil.cpu_percent(30))), cpu_freq=int(round(psutil.cpu_freq().current)), ram=int(round(psutil.virtual_memory().percent)))
    data.save()


threading.Timer(interval=120.0, function=periodic_task_1h).start()


def periodic_task_6h():
    threading.Timer(interval=720.0, function=periodic_task_6h).start()

    from .models import ServerInformation_6h

    data = ServerInformation_6h(cpu=int(round(psutil.cpu_percent(30))), cpu_freq=int(round(psutil.cpu_freq().current)), ram=int(round(psutil.virtual_memory().percent)))
    data.save()


threading.Timer(interval=720.0, function=periodic_task_6h).start()


def periodic_task_24h():
    threading.Timer(interval=2880.0, function=periodic_task_24h).start()

    from .models import ServerInformation_24h

    data = ServerInformation_24h(cpu=int(round(psutil.cpu_percent(30))), cpu_freq=int(round(psutil.cpu_freq().current)), ram=int(round(psutil.virtual_memory().percent)))
    data.save()


threading.Timer(interval=2880.0, function=periodic_task_24h).start()


def clean():
    threading.Timer(interval=3600.0, function=clean).start()

    from .models import ServerInformation
    from .models import ServerInformation_15m
    from .models import ServerInformation_30m
    from .models import ServerInformation_1h
    from .models import ServerInformation_6h
    from .models import ServerInformation_24h

    ServerInformation.objects.filter(ts__gte=datetime.datetime.now() - datetime.timedelta(days=2)).delete()
    ServerInformation_15m.objects.filter(ts__gte=datetime.datetime.now() - datetime.timedelta(days=2)).delete()
    ServerInformation_30m.objects.filter(ts__gte=datetime.datetime.now() - datetime.timedelta(days=2)).delete()
    ServerInformation_1h.objects.filter(ts__gte=datetime.datetime.now() - datetime.timedelta(days=2)).delete()
    ServerInformation_6h.objects.filter(ts__gte=datetime.datetime.now() - datetime.timedelta(days=2)).delete()
    ServerInformation_24h.objects.filter(ts__gte=datetime.datetime.now() - datetime.timedelta(days=2)).delete()

threading.Timer(interval=3600.0, function=clean).start()
