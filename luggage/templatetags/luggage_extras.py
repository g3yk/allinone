import base64
from io import BytesIO

from barcode import UPCA
from django import template

register = template.Library()


@register.filter(name="generate_barcode")
def generate_barcode(value):
    upca = UPCA(f"{value:011}")
    output = BytesIO()
    upca.write(output, options={"background": "transparent"})
    output.seek(0)

    encoded_string = base64.b64encode(output.getvalue()).decode()

    return "data:image/svg+xml;base64," + encoded_string
