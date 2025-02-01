from django.shortcuts import render
from .models import (
    MetaContent,
    SideBar,
    Header,
    Menu,
    MainContent,
    Add,
    Quiz,
    Category,
    ModelStatic,
    ModelDynamic,
    Catalog,
    Budget,
    Guarantees,
    More,
    Portfolio,
    Video,
    Reviews,
    Install, Numbers, Quality, Faq, Requisition, Contacts, Footer, PopupRequest, PopupStock, PopupPolitic, PopupLeave)

def city5_content(request):
    meta_tags = MetaContent.objects.first()
    sidebar = SideBar.objects.first()
    header = Header.objects.first()
    menu = Menu.objects.first()
    main_content = MainContent.objects.first()
    add = Add.objects.first()
    quiz = Quiz.objects.first()
    category = Category.objects.first()
    model_static = ModelStatic.objects.first()
    model_dynamic = ModelDynamic.objects.all()
    catalog = Catalog.objects.first()
    budget = Budget.objects.first()
    guarantees = Guarantees.objects.first()
    more = More.objects.first()
    portfolio = Portfolio.objects.first()
    video = Video.objects.first()
    reviews = Reviews.objects.first()
    install = Install.objects.first()
    numbers = Numbers.objects.first()
    quality = Quality.objects.first()
    faq = Faq.objects.first()
    requisition = Requisition.objects.first()
    contacts = Contacts.objects.first()
    footer = Footer.objects.first()
    popup_request = PopupRequest.objects.first()
    popup_stock = PopupStock.objects.first()
    popup_politic = PopupPolitic.objects.first()
    popup_leave = PopupLeave.objects.first()
    return render(request, 'city5/index.html', {'meta_tags': meta_tags, 'sidebar': sidebar,
                                               'header': header, 'menu': menu, 'main_content': main_content,
                                               'add': add, 'quiz': quiz, 'category': category, 'model_static': model_static,
                                               'model_dynamic': model_dynamic, "numbers10": range(1, 11),
                                               'catalog': catalog, 'budget': budget, 'guarantees': guarantees, 'more': more,
                                               'portfolio': portfolio, 'video': video, 'reviews': reviews, 'install': install,
                                               'numbers': numbers, 'quality': quality, 'faq': faq, 'requisition': requisition,
                                               'contacts': contacts, 'footer': footer, 'popup_request': popup_request,
                                               'popup_stock': popup_stock, 'popup_politic': popup_politic, 'popup_leave': popup_leave})
