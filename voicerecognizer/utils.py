import pkg_resources

from django.template import Context, Template

def load_resource(resource_path):
    # Load the resource content as binary data
    resource_content = pkg_resources.resource_string(__name__, resource_path)
    # Decode the binary data to a text string using UTF-8 or another appropriate encoding
    return resource_content.decode('utf-8')


def render_template(template_path, context={}):
    template_str = load_resource(template_path)
    template = Template(template_str)
    return template.render(Context(context))
