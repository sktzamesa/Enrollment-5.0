from .models import Profile

def student_profile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(User_Student_Profile=request.user)
            return {'student_profile': profile}
        except Profile.DoesNotExist:
            return {'student_profile': None}
    return {}
