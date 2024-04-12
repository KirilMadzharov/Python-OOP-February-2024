def role_required(role):
    """Decorator factory that accepts a role required to execute the function."""

    def decorator(func):
        """The actual decorator that uses the 'role' argument from the outer function."""

        def wrapper(*args, **kwargs):
            """Wrapper function to add additional functionality."""
            user_role = kwargs.get('role', None)  # Assumes user role is passed as a keyword argument
            if user_role != role:
                raise Exception(f"Unauthorized access, required role: {role}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@role_required('admin')
def sensitive_function(*args, **kwargs):
    """Function that requires admin role to execute."""
    print("Sensitive data shown only to admins.")


# Example usage:
try:
    sensitive_function(role='admin')
    sensitive_function(role='user')  # This will raise an exception
except Exception as e:
    print(e)
