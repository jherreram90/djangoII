from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa #pillow & reportlab

def render_to_pdf(template_src,context_dic={}):
	template=get_template(template_src)
	html=template.render(context_dic)
	result=BytesIO() #Permite el manejo de E/S
	pdf=pisa.pisaDocument(BytesIO(html.encode('UTF-8')),result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type='application/pdf')
	return None