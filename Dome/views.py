from django.views import View
from django.shortcuts import render,redirect,reverse,HttpResponse
from gen import gen,veri,veri_forge
import os

#generate start
class Index(View):
    def get(self,request):
        return render(request,'index_index.html')
    def post(self,request):
        pass
#generate result
class Index_1(View):
    def get(self,request):
        gen.main()
        list = []
        list1 = []
        filePath = './static/ewm_img'
        tt = os.listdir(filePath)
        if tt:
            can = 0
            for i in tt:
                list.append(i.split('.')[0])
                if can < 5:
                    can += 1
                    list1.append(i.split('.')[0])

            return render(request, 'index1.html', {'name': list, 'name_li': list1})
        else:
            return render(request, 'index1.html', {'name': tt})
    def post(self,request):
        pass


#veri-initial
class Index_logo(View):
    def get(self,request):
        return render(request,'index_logo.html')
    def post(self,request):
        pass

#veri-result-genuine
class Index_3(View):
    def get(self,request):
        list = veri.ma()
        return render(request,'index2.html',{ 'name_i': list})
    def post(self,request):
        pass

#veri-initial
class Index_forge(View):
    def get(self,request):
        return render(request,'index_forge.html')
    def post(self,request):
        pass

#veri-result-forge
class Index_4(View):
    def get(self,request):
        lst = veri_forge.maf()
        return render(request,'index4.html',{ 'name_f': lst})
    def post(self,request):
        pass