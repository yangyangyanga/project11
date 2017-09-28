from django.shortcuts import render, redirect

from .models import Wheel, Nav, Mustbuy, Shop, MainShow, FoodTypes, Goods, User, Cart,Order

# Create your views here.
def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()

    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]

    mainList = MainShow.objects.all()

    context = {
        "title": '主页',
        "wheelsList": wheelsList,
        "navList": navList,
        "mustbuyList": mustbuyList,
        "shop1": shop1,
        "shop2": shop2,
        "shop3": shop3,
        "shop4": shop4,
        "mainList": mainList,

    }
    return render(request, 'axf/home.html', context=context)

def market(request, categoryid, cid, sortid):
    leftSlider = FoodTypes.objects.all()

    if cid == '0':
        # 默认全部分类
        productList = Goods.objects.filter(categoryid=categoryid)
    else:
        productList = Goods.objects.filter(categoryid=categoryid, childcid=cid)

    # 排序
    if sortid == '1':   # 销量排序
        productList = productList.order_by("productnum")
    elif sortid == '2':     # 价格最低
        # price = eval(productList.price)
        # print(type(price))
        productList = productList.order_by("price")
    elif sortid == '3':     # 价格最高
        productList = productList.order_by("price")

    group = leftSlider.get(typeid=categoryid)
    childList = []
    # 全部分类:0#进口水果:103534#国产水果:103533
    childnames = group.childtypenames   # group 是一个对象
    arr1 = childnames.split("#")
    for str in arr1:
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList.append(obj)

    #
    cartlist = []
    token = request.session.get("token")
    if token:
        user = User.objects.get(userToken=token)
        cartlist = Cart.objects.filter(userAccount=user.userAccount)

    for p in productList:
        for c in cartlist:
            if c.productid == p.productid:
                p.num = c.productnum
                continue
    context = {
        "title": '闪送超市',
        "leftSlider": leftSlider,
        "productList": productList,
        "childList": childList,
        "categoryid": categoryid,
        "cid": cid,
        "cartlist": cartlist,
        # "cartlistnum": cartlistnum,
    }

    return render(request, 'axf/market.html', context=context)

def cart(request):
    cartslist = []
    user = User()
    # 判断用户是否登录
    token = request.session.get("token")
    # print("token = ", token)
    if token != None:
        user = User.objects.get(userToken=token)
        cartslist = Cart.objects.filter(userAccount=user.userAccount)
    return render(request, 'axf/cart.html', {"title": '购物车',
                                             "cartslist": cartslist,
                                             "user": user,})

# 修改购物车
def changecart(request, flag):
    # 判断用户是否登录
    token = request.session.get("token")
    # print("token = ", token)
    if token == None:
        # 没有登录，传去json数据
        return JsonResponse({"data": -1, "status": "error"})

    # 获得当前想要操作商品的id
    productid = request.POST.get("productid")
    # 通过过滤商品id获得商品
    product = Goods.objects.get(productid=productid)
    # 获得当前登录的用户
    user = User.objects.get(userToken=token)

    totalprice = 0
    if flag == "0":
        if product.storenums == 0:
            return JsonResponse({"data": -2, "status": "error"})

        # 获得当前用户的购物车模型
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            # 判断库存的数量

            # 直接增加一条订单
            c = Cart.createcart(user.userAccount, productid, 1, product.price, True,
                                product.productimg,product.productlongname, False)
            c.save()
        else:
            try:
                c = carts.get(productid=productid)
                # 修改数量和价格
                c.productnum += 1
                c.productprice = "%.2f" % (c.productnum * float(product.price))
                c.save()
            except Cart.DoesNotExist as e:
                # 直接增加一条订单
                c = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg,
                                    product.productlongname, False)
                c.save()
        # 库存减1
        product.storenums -= 1
        product.save()
        totalprice = float(product.price)
        return JsonResponse({"data": c.productnum,"price": c.productprice, "status": "success","totalprice":totalprice})
    elif flag == "1":
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
           return JsonResponse({"data": -2, "status": "error"})
        else:
            try:
                c = carts.get(productid=productid)
                # 修改数量和价格
                c.productnum -= 1
                c.productprice = "%.2f" % (c.productnum * float(product.price))
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()
            except Cart.DoesNotExist as e:
                return JsonResponse({"data": -2, "status": "error"})
        # 库存减1
        product.storenums += 1
        product.save()
        totalprice = float(product.price)
        return JsonResponse({"data": c.productnum,"price": c.productprice, "status": "success","totalprice":totalprice})

    elif flag == "2":
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()
        str = ""
        if c.isChose:
            str = "√"
            # totalprice = 1
        return JsonResponse({"data": str, "status": "success", "totalprice":totalprice})
    elif flag == "3":
        pass

def mine(request):
    username = request.session.get("username", "未登录")
    token = request.session.get("token")
    print("token = ",token)
    userimg = 'E:\Python-1704\project11\day39\project\static\main\img\mine.png'
    if token !=  None:
        user = User.objects.get(userToken=token)
        userimg = user.userImg
        print("userimg = ", userimg)
    return render(request, 'axf/mine.html', {"title": '我的', "username": username, "userimg": userimg})

# 登录
from .forms.login import LoginForm
from django.http import HttpResponse
def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            # 信息没多大问题，验证账号和密码的正确性
            # 获得登录表单输入的值
            nameid = f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]

            remain = ""
            # 登录不成功
            try:
                # 筛选出账号等于表单输入的账号
                user = User.objects.get(userAccount=nameid)
                if user.userPasswd != pswd:
                    remain = "密码输入不正确，请重新登录"
                    return render(request, 'axf/login.html', {"title": "登录", "remain": remain, "form":f,})
            except User.DoesNotExist as e:
                return redirect("/login/")

            # 登陆成功
            token = time.time() + random.randrange(1, 100000)
            user.userToken = str(token)
            user.save()
            request.session["username"] = user.userName
            request.session["token"] = user.userToken
            return redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {"title": "登录"})
    else:
        f = LoginForm()
        return render(request, 'axf/login.html', {"title": "登录","form":f,})

# 注册
import time
import random
from django.conf import settings
import os
def register(request):
    if request.method == "POST":
        # 获取从注册表单填写的值
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPass")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAdderss = request.POST.get("userAdderss")
        userRank = 0
        # touken验证值，每次登陆之后都会更新
        token = time.time() + random.randrange(1, 100000)
        userToken = str(token)

        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MEDIA_ROOT, userAccount + ".png")
        with open(userImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        # 创建用户保存到数据库
        user = User.createuser(userAccount, userPasswd, userName,userPhone, userAdderss, userImg, userRank,userToken)
        user.save()
        # 将用户名和token传到session中
        request.session["username"] = userName
        request.session["token"] = userToken
        return redirect('/mine/')
    else:
        return render(request, 'axf/register.html', {"title": "注册"})

from django.http import JsonResponse
def checkuserid(request):
    # 从register.js中的一个ajax请求中获取的userid值
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount=userid)
        return JsonResponse({"data": "该用户已经被注册", "status": "error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data": "可以注册", "status": "success"})

# 退出登录
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect("/mine/")

def saveorder(request):
    # 判断用户是否登录
    token = request.session.get("token")
    if token == None:
        # 没有登录
        return JsonResponse({"data": -1, "status": "error"})
    user = User.objects.get(userToken=token)
    carts = Cart.objects.filter(isChose=True)
    if carts.count() == 0:
        return JsonResponse({"data": -1, "status": "error"})
    oid = time.time() + random.randrange(1, 10000)
    oid = "%d"%oid
    o = Order.createorder(1, user.userAccount, 0)
    o.save()
    for item in carts:
        item.isDelete = True
        item.orderid = oid
        item.save()
    return JsonResponse({"status": "success"})
