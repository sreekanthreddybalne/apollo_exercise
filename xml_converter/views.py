from django.http import JsonResponse
from django.shortcuts import render
from django import forms
from http import HTTPStatus
from .utils import convert_xml_to_dict


# Form
class XMLConverterForm(forms.Form):
    file = forms.FileField(
        label="XML File",
        error_messages={'required': 'An XML file is required'}
    )

# Exception
class InvalidXMLException(Exception):
    """
    Raised when an invalid XML is submitted
    """

def upload_page(request):
    xml_form = XMLConverterForm()
    if request.method == 'POST':
        # TODO: Convert the submitted XML file into a JSON object and return to the user.
        form = XMLConverterForm(request.POST, request.FILES)
        if not form.is_valid():
            # The submitted form is invalid. Send back a response informing the same.
            # this error will also be thrown if the file is empty without any content
            return JsonResponse(
                "The data is not valid!. Please ensure a proper XML file is submitted.",
                status=HTTPStatus.NOT_ACCEPTABLE, safe=False)
        file = form.files['file']
        data = convert_xml_to_dict(file)
        return JsonResponse(data)

    return render(request, "upload_page.html", context={"xml_form": xml_form})
