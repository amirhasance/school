
from klass.models import Student , Teacher

def student_or_teacher(user):
    
    # import pdb ; pdb.set_trace()
    if  Student.objects.filter(user = user).exists():
        return 'student'
    elif Teacher.objects.filter(user = user).exists():
        return 'teacher'
    else :
        return None