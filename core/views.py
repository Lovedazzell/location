from django.http import  JsonResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.files.storage import FileSystemStorage
from . models import UserData
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import UserDataSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt,name = 'dispatch')
@method_decorator(login_required,name = 'dispatch')
class Dashboard(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['class'] = 'active'
        return context

    def post(self,request):

        print(request.POST)        
        name = request.POST.get('name')
        number = request.POST.get('number')
        comment = request.POST.get('comment')
        s_shot = request.FILES.get('s_shot')
        door_file = request.FILES.get('door_file')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        print(latitude)
        print(longitude)

        # getting screenshot image file 
        fss = FileSystemStorage()
        screenshot = fss.save(s_shot.name,s_shot)
        screenshot_url = fss.url(screenshot)

        # getting doorstep image
        doorstep = fss.save(door_file.name,door_file)
        doorstep_url = fss.url(doorstep)

       
        data = UserData(user=request.user , name=name ,number = number, sshot=s_shot,door=door_file , comment = comment,lat_tude=latitude,lon_tude=longitude)
        data.save()



        return JsonResponse({'Status':'saved successfully'})
    

@method_decorator(login_required,name = 'dispatch')
class Search(TemplateView):
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classS'] = 'active'
        return context
    
@method_decorator(login_required,name = 'dispatch')
class Reference(TemplateView):
    template_name = 'core/reference.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classR'] = 'active'
        return context
    
@api_view()
def referance_api(request):
    user_obj = UserData.objects.filter(user=request.user).order_by('-created')
    serializer = UserDataSerializer(user_obj,many = True)
    return Response({'success':200,'payload':serializer.data})


@api_view(['POST'])
def search_api(request):
    method = request.data['search_by']
    val = request.data['val']
    print(request.data)
    if method == 'number':
        data = UserData.objects.filter(number__icontains = val)
    elif method == 'name':
        data = UserData.objects.filter(name__icontains = val)
    elif method == 'remarks':
        data = UserData.objects.filter(comment__icontains = val)
    else:
        data = UserData.objects.filter(address__icontains = val)

    print(data)
    
    serializer = UserDataSerializer(data,many = True)

    return Response({'success':200,'message':'result find','payload':serializer.data})