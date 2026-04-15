from .utils import send_welcome_email

def send_welcome_email_pipeline(backend, user, response, is_new=False, *args, **kwargs):
    """
    Social Auth pipeline function to send welcome email to new users.
    """
    if is_new and user.email:
        # For Google OAuth, the user's name is usually in the response
        name = user.first_name or user.username
        if not name:
            name = response.get('name') or response.get('given_name') or 'Operator'
            
        send_welcome_email(user.email, name)
    
    return None
