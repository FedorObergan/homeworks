# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        new_sensor = Sensor(name=request.data.get('name'), description=request.data.get('description'))
        new_sensor.save()
        return Response({'status': 'OK'})


class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        if request.data.get('name'):
            Sensor.objects.filter(id=pk).update(name=request.data.get('name'))
        if request.data.get('description'):
            Sensor.objects.filter(id=pk).update(description=request.data.get('description'))
        return Response({'status': 'OK'})


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


    def post(self, request):
        sensor = Sensor.objects.get(id=int(request.data.get('sensor')))
        measurement = Measurement(sens_id=sensor.id, temperature=request.data.get('temperature'))
        measurement.save()

        return Response({'status': 'OK'})
