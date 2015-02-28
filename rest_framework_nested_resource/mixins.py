from django.db.models import QuerySet
from rest_framework.generics import get_object_or_404


class NestedResourceMixin(object):
    """
    View mixin for nested resources. Defines the relation between the nested resource and the parent,
    checks if the parent object actually exists and passes the parent instance
    into the nested resource serializer as part of `validated_data`.
    """
    # You'll need to either set this attribute,
    # or override `get_parent_queryset()`.
    # If you are overriding a view method, it is important that you call
    # `get_parent_queryset()` instead of accessing the `parent_queryset` property directly,
    # as `parent_queryset` will get evaluated only once, and those results are cached
    # for all subsequent requests.
    parent_queryset = None

    # If you want to use parent object lookups other than pk, set 'parent_lookup_field'.
    # For more complex lookup requirements override `get_parent_object()`.
    parent_lookup_field = 'pk'
    parent_lookup_url_kwarg = None

    def get_parent_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.parent_queryset`.
        This method should always be used rather than accessing `self.parent_queryset`
        directly, as `self.parent_queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.
        You may want to override this if you need to provide different
        querysets depending on the incoming request.
        (Eg. return a list of items that is specific to the user)
        """
        assert self.parent_queryset is not None, (
            "'%s' should either include a `parent_queryset` attribute, "
            "or override the `get_parent_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.parent_queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def get_parent_object(self):
        """
        Returns the parent object of the underlying object of the view.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg. if parent objects are referenced using multiple
        keyword arguments in the url conf.
        """
        parent_queryset = self.get_parent_queryset()

        # Perform the lookup filtering.
        parent_lookup_url_kwarg = self.parent_lookup_url_kwarg or self.parent_lookup_field

        assert parent_lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.parent_lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, parent_lookup_url_kwarg)
        )

        filter_kwargs = {self.parent_lookup_field: self.kwargs[parent_lookup_url_kwarg]}
        obj = get_object_or_404(parent_queryset, **filter_kwargs)

        return obj

    def get_serializer_context(self):
        """
        Adds the parent instance to the context of the nested resource serializer.
        This instance can later be used by default fields or other custom fields.
        """
        context = super(NestedResourceMixin, self).get_serializer_context()
        context['parent'] = self.get_parent_object()
        return context
