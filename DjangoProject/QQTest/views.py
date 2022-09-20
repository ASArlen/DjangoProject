from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from QQTest.models import Application,Interface





def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        username = request.POST.get("userid")
        password = request.POST.get("pwd")

        if username == "QQ100" and password == "rules":
            # return HttpResponse("Login successully")
            return redirect("https://digital-processing-int.cn.bg.corpintra.net/prclusterservice")
        else:
            # return HttpResponse("Login fail")
            return render(request, "login.html","error_message",{"error_message":"userid or password error"} )

def interface_list(request):
    interface_list = Interface.objects.all()

    return render(request,"interfacelist.html",{"interface_list":interface_list})




def interface_add(request):
    # return render(request, 'interface_add.html')
    if request.method == "GET":
        return render(request,'interface_add.html')

    # 获取用户添加提交的数据

    interface_name = request.POST.get("InterfaceName")
    service_id = request.POST.get("ServiceID")
    application_id = request.POST.get("ApplicationID")
    create_time = request.POST.get("CreateTime")
    interface_method = request.POST.get("interfacemethod")
    print(interface_name,service_id,application_id,create_time)

    #添加到数据库
    Interface.objects.create(service_id=service_id,application_id=application_id,interface_name=interface_name,create_time=create_time,interface_method=interface_method)



    # 自动跳转
    return redirect("/interface/list/")


def interface_delete(request):
    nid = request.GET.get("nid")
    Interface.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8080/interface/list/")


def interface_update(request,nid):

    if request.method == "GET":
        # row_object = Interface.objects.filter(id=nid).first()
        row_object = Interface.objects.filter(id=nid)
        row_object = row_object[0]
        return render(request, "interface_update.html", {"row_object": row_object})



    ServiceID = request.POST.get("ServiceID")
    InterfaceName = request.POST.get("InterfaceName")
    ApplicationID = request.POST.get("ApplicationID")
    CreateTime = request.POST.get("CreateTime")
    interfacemethod = request.POST.get("interfacemethod")
    Interface.objects.filter(id=nid).update(service_id=ServiceID,application_id=ApplicationID,interface_name=InterfaceName,create_time=CreateTime,interface_method=interfacemethod)
    return redirect("/interface/list/")




from django import forms
from QQTest import models
class InterfaceModelForm(forms.ModelForm):

    class Meta:
        model = models.Interface
        fields = ['interface_name','application','interface_method']
        # fields = '_all_'
        # widgets = {
        #     "interface_name" :forms.TextInput(attrs={"class": "form-control"}),
        #     "application": forms.TextInput(attrs={"class": "form-control"})
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            print(name,field)
            field.widget.attrs = {"class": "form-control"}

def interface_classification(request):
    form = InterfaceModelForm()

    # interface_classification = Interface.objects.all()

    return render(request,"InterfaceClassification.html",{"form":form})





