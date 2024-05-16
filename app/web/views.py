from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Category, Product

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    


class RemontView(TemplateView):
    template_name = 'remont.html'

    

class AboutView(TemplateView):
    template_name = 'about.html'



class CatalogView(ListView):
    template_name = 'catalog.html'
    model = Category

    
class ProductsView(ListView):
    template_name = 'products.html'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs["id"])
        self.products = Product.objects.filter(category=category)
        return self.products
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["products"] = self.products
        return context