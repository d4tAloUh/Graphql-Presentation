from functools import wraps

from django.core.exceptions import PermissionDenied
from graphql import ResolveInfo


def context(f):
    def decorator(func):
        def wrapper(*args, **kwargs):
            info = next(arg for arg in args if isinstance(arg, ResolveInfo))
            return func(info.context, *args, **kwargs)

        return wrapper

    return decorator


def user_passes_test(test_func,
                     exc=PermissionDenied('You do not have permissions to '
                                          'access this resource')):
    def decorator(f):
        @wraps(f)
        @context(f)
        def wrapper(ctx, *args, **kwargs):
            if test_func(ctx.user):
                return f(*args, **kwargs)
            raise exc

        return wrapper

    return decorator


login_required = user_passes_test(lambda u: u.is_authenticated)
