class ParentDefault():
    """
    Returns the parent instance received from the nested resource view.
    """

    def set_context(self, serializer_field):
        self.parent = serializer_field.context['parent']

    def __call__(self):
        return self.parent


class ParentPrimaryKeyDefault():
    """
    Returns the parent primary key received from the nested resource view.
    """

    def set_context(self, serializer_field):
        self.parent = serializer_field.context['parent']

    def __call__(self):
        return self.parent.pk


class ParentContentTypeDefault():
    """
    Returns the parent content type from the nested resource view.
    """

    def set_context(self, serializer_field):
        self.parent = serializer_field.context['parent']

    def __call__(self):
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(self.parent)
