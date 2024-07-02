from django.urls import path

from measurement.views import SensorsView, OneSensorView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
