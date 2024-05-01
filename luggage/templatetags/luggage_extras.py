import base64
from io import BytesIO

from barcode import UPCA
from barcode.writer import ImageWriter
from django import template

register = template.Library()


@register.filter(name="generate_barcode")
def generate_barcode(value):
    upca = UPCA(f"{value:011}", writer=ImageWriter())
    output = BytesIO()
    upca.write(output)
    output.seek(0)

    encoded_string = base64.b64encode(output.getvalue()).decode()

    return "data:image/png;base64," + encoded_string
