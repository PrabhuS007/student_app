from django.shortcuts import render,redirect
from studentapp.models import student
from django.contrib import messages
# Create your views here.
def handleindex(request):
    allusers=student.objects.all()
    userdict={"allusers":allusers}
    return render(request,'index.html',userdict)

def handleinsert(request):
    if request.method == 'POST':
        fname=request.POST['name']
        femail=request.POST['email']
        fage=request.POST['age']
        fgender=request.POST['gender']

        #
        fimage = request.FILES.get('image')
        #
        #print(fname,femail,fage,fgender)
        users=student(sname=fname,semail=femail,sage=fage,sgender=fgender,simage=fimage)
        users.save()
        messages.success(request,"Student Details Inserted Succesfully")
        return redirect('/')
    return render(request,'index.html')

def handleupdate(request,id):
    user=student.objects.get(id=id)
    user_dict={"user":user}

    if request.method == 'POST':
        fname=request.POST['name']
        femail=request.POST['email']
        fage=request.POST['age']
        fgender=request.POST['gender']
        #
        fimage = request.FILES.get('image') # multivalued dict
        
        #
        #print(fname,femail,fage,fgender)
        users=student(id=id,sname=fname,semail=femail,sage=fage,sgender=fgender,simage=fimage)
        users.save()
        messages.info(request,"Student Details Updated Succesfully")
        return redirect('/')
    
    return render(request,'update.html',user_dict)

def handledelete(request,id):
    user=student.objects.get(id=id)
    user.delete()
    messages.error(request,"Student Details Deleted Succesfully")
    return redirect('/')
    