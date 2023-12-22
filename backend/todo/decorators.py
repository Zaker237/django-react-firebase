# decorators.py

from django.http import JsonResponse
from functools import wraps
from firebase_admin import auth

def verify_firebase_auth(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        id_token = request.headers.get('Authorization')
        if not id_token:
            return JsonResponse({'error': 'Authorization token is missing'}, status=401)

        try:
            decoded_token = auth.verify_id_token(id_token)
            # Access user information from decoded_token (e.g., decoded_token['uid'])
            request.firebase_user = decoded_token
        except auth.InvalidIdTokenError:
            return JsonResponse({'error': 'Invalid Authorization token'}, status=401)
        except auth.ExpiredIdTokenError:
            return JsonResponse({'error': 'Expired Authorization token'}, status=401)
        except auth.RevokedIdTokenError:
            return JsonResponse({'error': 'Revoked Authorization token'}, status=401)
        except auth.CertificateFetchError:
            return JsonResponse({'error': 'Unable to fetch Firebase Auth certificate'}, status=500)

        return view_func(request, *args, **kwargs)

    return _wrapped_view