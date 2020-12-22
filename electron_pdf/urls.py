# coding: utf-8

from django.urls import path
from electron_pdf.views import PDFTemplateView

urlpatterns = [
    path('test/', PDFTemplateView.as_view(
        template_name='test.html',
        filename='test.pdf',
        show_content_in_browser=True,
        get_context_data=lambda: {'company_name': 'Namespace OÜ'},
    ), name='pdf'),
]
