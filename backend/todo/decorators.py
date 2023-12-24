# decorators.py
from django.http import JsonResponse
from functools import wraps
from firebase_admin import auth

def verify_firebase_auth(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        id_token: str = request.headers.get('Authorization')
        if not id_token or not id_token.startswith("Bearer "):
            return JsonResponse({'error': 'Authorization token is missing'}, status=401)
        id_token = id_token.replace("Bearer ", "")
        try:
            decoded_token = auth.verify_id_token(id_token)
            request.firebase_user = decoded_token
        except auth.InvalidIdTokenError:
            print(1)
            return JsonResponse({'error': 'Invalid Authorization token'}, status=401)
        except auth.ExpiredIdTokenError:
            print(1)
            return JsonResponse({'error': 'Expired Authorization token'}, status=40)
        except auth.RevokedIdTokenError:
            return JsonResponse({'error': 'Revoked Authorization token'}, status=401)
        except auth.CertificateFetchError:
            print(2)
            return JsonResponse({'error': 'Unable to fetch Firebase Auth certificate'}, status=500)

        return view_func(request, *args, **kwargs)

    return _wrapped_view