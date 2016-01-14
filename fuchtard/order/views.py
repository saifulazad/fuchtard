import datetime

from django.shortcuts import render
from django.views.generic import FormView, UpdateView, View

from .forms import OrderCheckoutForm


class OrderCheckoutView(FormView):
    form_class = OrderCheckoutForm
    template_name = 'order/order_checkout.html'

    def get_deferred_delivery_dates(self):
        humanized = (
            'Сегодня',
            'Завтра',
            'Послезавтра',
        )
        return [(humanized[td], datetime.date.today() + datetime.timedelta(days=td),) for td in range(3)]

    def _next_timestamp(self, current_timestamp):
            return (datetime.datetime.combine(datetime.datetime.today(), current_timestamp) +
                    datetime.timedelta(minutes=30)).time()

    def get_deferred_delivery_hours(self):
        import datetime
        working_hours_start = datetime.time(hour=11, minute=12)
        working_hours_end = datetime.time(hour=23, minute=11)
        if working_hours_start < working_hours_end:
            result = [datetime.time(hour=working_hours_start.hour)]
            while True:
                dt = self._next_timestamp(result[-1])
                if dt > working_hours_end:
                    break
                result.append(dt)
        else:
            result = [datetime.time(hour=0)]
            while True:
                dt = self._next_timestamp(result[-1])
                if dt > working_hours_end:
                    break
                result.append(dt)
            result.append(datetime.time(hour=working_hours_start.hour))
            while True:
                dt = self._next_timestamp(result[-1])
                if dt < working_hours_end:
                    break
                result.append(dt)


class CartUpdateView(View):
    def post(self, request, *args, **kwargs):
        pass