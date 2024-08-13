from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.http.response import JsonResponse
from django.contrib import messages
from.models import *
from django.views.decorators.csrf import csrf_exempt
from Ecomapp.models import Contact
from Ecomapp.models import Feedback
from Ecomapp.models import Complaint
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product, Cart
import logging
import random
logger = logging.getLogger(__name__)



def home(request):
    arrival = Arrival.objects.filter(status=0)
    demand = Demand .objects.filter(status=0)
    delership = Delership .objects.filter()
    context ={'Arrival':arrival,'Demand':demand,'Delership':delership}
    return render(request, 'home.html',context) 
 


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, "collections.html", context)


def collectionsview(request, slug):
        if(Category.objects.filter(slug=slug,status=0)):       
             products=Product.objects.filter(category__slug=slug)
             category_name = Category.objects.filter(slug=slug).first()
             context = {'products':products,'category_name':category_name}
             return render(request,'Store/Products/Index.html',context)
        else:
             messages.warning(request,"No Such Category Found")
             return redirect('collections')
        
def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug).exists():
        if Product.objects.filter(slug=prod_slug).exists():
            product = Product.objects.get(slug=prod_slug)
            context = {'product': product}
            return render(request, "Store/Products/view.html", context)
        else:
            messages.error(request, "No such product found")
            return HttpResponse('No such product found')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')



def feature(request):
     return render(request,'Features.html')



def Aboutus(request):
     return render(request,'Aboutus.html')

@csrf_exempt 
def Contactus(request):
     if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        # Create a new contact instance and save it to the database
        contact = Contact(Name=name, Email=email, Phone=phone, Message=message)
        contact.save()

        return redirect('success')    
     return render(request, 'Contact.html')
     
     

@csrf_exempt 
def FeedbackView(request):
     if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        product = request.POST['product']
        message = request.POST['message']
        
        # Create a new feedback instance and save it to the database
        feedback = Feedback(Name2=name, Email2=email, Phone2=phone, Product2=product, Message2=message)
        feedback.save()

        return redirect('Feedback')    
     return render(request, 'Feedback.html')


@csrf_exempt
def Complaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        product = request.POST.get('product')
        model = request.POST.get('model')
        message = request.POST.get('message')
        uploaded_file = request.FILES.get('image')
        
        if name and email and phone and product and model and message and uploaded_file:
            # Create a new Complaint instance and save it to the database
            complaint = Complaint(
                Name3=name,
                Email3=email,
                Phone3=phone,
                Product3=product,
                Model3=model,
                Message2=message,
                Image=uploaded_file
            )
            complaint.save()
            return redirect('home')
        else:
            return render(request, 'Complaint.html', {'error': 'All fields are required'})
    return render(request, 'Complaint.html')

def Login(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('log')

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('wrong')

    return render(request, 'Login.html')






def Signup(request):
     if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('email')
        pass1 = request.POST.get('Password1')
        pass2 = request.POST.get('Password2')

        if not (name and Email and pass1 and pass2):
            return HttpResponse("All fields are required!")
        
        if pass1 != pass2:
            return redirect('notmatch')
        
        my_user = User.objects.create_user(name,Email,pass1)
        my_user.save()    
        return redirect("Login") 
     return render(request,'Signup.html')



@csrf_exempt
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("home")




def Cart2(request):
    if request.method == "POST":
        try:
            prod_id = int(request.POST.get('product_id'))
            prod_qty = int(request.POST.get('product_qty'))
            logger.info(f"Received POST request with product_id: {prod_id} and product_qty: {prod_qty}")
            product_check = get_object_or_404(Product, id=prod_id)
            logger.info(f"Product found: {product_check}")
            


            if Cart.objects.filter(user=request.user, product_id=prod_id,product_qty=prod_qty).exists():
                logger.info("Product already in Cart")
                return JsonResponse({"status": "Product already in Cart"}, status=400)
            else:
                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    logger.info("Product added to cart successfully")
                    return JsonResponse({"status": "Product added successfully"}, status=400)
                else:
                    logger.warning(f"Only {product_check.quantity} quantity available")
                    return JsonResponse({"status": f"Only {product_check.quantity} quantity available"}, status=400)
        except ValueError as ve:
            logger.error(f"ValueError: {ve}")
            return JsonResponse({"status": "Invalid input"}, status=400)
        except Exception as e:
            logger.error(f"Exception: {e}")
            return JsonResponse({"status": str(e)}, status=500)
    return render(request, '/')




def update_cart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('product_id')
        prod_qty = request.POST.get('product_qty')
        
        if prod_qty is None:
            return JsonResponse({"status": "Product quantity is required"}, status=400)
        
        try:
            prod_qty = int(prod_qty)
        except ValueError:
            return JsonResponse({"status": "Invalid product quantity"}, status=400)
        
        if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({"status": "Updated Successfully"}, status=300)
        else:
            return JsonResponse({"status": "Product not found in cart"}, status=404)
    return JsonResponse({"status": "Invalid request method"}, status=400)

def delete_cart_item(request):
    if request.method == 'POST':
        prod_id = request.POST.get('product_id')
        
        if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.delete()
            return JsonResponse({"status": "Item removed successfully"}, status=300)
        else:
            return JsonResponse({"status": "Product not found in cart"}, status=404)
    return JsonResponse({"status": "Invalid request method"}, status=400)

@login_required(login_url=Login)
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'cart': cart_items} 
    return render(request, 'Cart.html', context)
















@login_required(login_url=Login)
def Wishlists(request):
    Wishlist_items = Wishlist.objects.filter(user=request.user)
    context = {'wishlist': Wishlist_items} 
    return render(request, 'Wishlist.html', context)



def addWishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            try:
                product_check = Product.objects.get(id=prod_id)
                if Wishlist.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': "Product already in Wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to Wishlist successfully"})
            except Product.DoesNotExist:
                return JsonResponse({"status": "No such product"})
        else:
            return JsonResponse({"status": "Login to continue"})
    return redirect('/')


@csrf_exempt
def delete_list_item(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        wishlist_item = Wishlist.objects.get(product_id=product_id, user=request.user)
        wishlist_item.delete()
        return JsonResponse({'status': 'Item removed from wishlist'})
    return JsonResponse({'status': 'Invalid request'}, status=400)


@login_required(login_url='Login')
def Check(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure the user is logged in

    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            item.delete()  # Correct way to delete the item

    cartitems = Cart.objects.filter(user=request.user)  # Corrected to use request.user
    total_price = 0
    for item in cartitems:
        total_price += item.product.Selling_Price * item.product_qty

    context = {'cartitems': cartitems, 'total_price': total_price}
    return render(request, 'Checkout.html', context)



@login_required(login_url='Login')
def placeorder2(request):
    if request.method =="POST":
        neworder = Order()
        neworder.user = request.user
        neworder.Fname =request.POST.get('Fname')
        neworder.Lname =request.POST.get('Lname')
        neworder.Email =request.POST.get('Email')
        neworder.Phone =request.POST.get('Phone')
        neworder.Address =request.POST.get('Adress')
        neworder.City =request.POST.get('City')
        neworder.State =request.POST.get('state')
        neworder.Country =request.POST.get('Country')
        neworder.Pincode =request.POST.get('Pincode')
        neworder.Total_price =request.POST.get('Totalprice')
        neworder.Payment_mode =request.POST.get('Paymentmode')
        
        cart =Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price =cart_total_price +item.product.selling_price *item.product_qty
        
        
        neworder.total_price = cart_total_price    
        trackno = 'AnveshJain' +str(random.randint(11111111,9999999))
        while Order.objects.filter(tracking_no =trackno)  is None:
                trackno = 'AnveshJain' +str(random.randint(11111111,9999999))

        neworder.tracking_no =trackno
        neworder.save()


        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            Orderitem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )           









    return render(request,'placeorder.html')













# its all about for Clipart messages #

def Book(request):
     return render(request,'Book.html')

def already(request):
    return render(request,'already.html')

def Incorrect(request):
    return render(request,'wrong.html')

def Password(request):
    return render(request,'Password.html')

def Send(request):
    return render(request,'Send Message.html')

def Feed(request):
    return render(request,'Feed.html')

