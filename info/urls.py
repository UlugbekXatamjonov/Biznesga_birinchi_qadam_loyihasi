from django.urls import path
from .views import InfoView, ResultView, WinnerView, export_result

urlpatterns = [
	path('', InfoView, name='info'),
	path('all/', ResultView.as_view(), name='all_people'),
	path('winner/', WinnerView.as_view(), name='win_people'),
	path('exel/', export_result, name='exel'),
]

