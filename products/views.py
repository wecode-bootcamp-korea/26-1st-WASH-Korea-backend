import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from products.models import Product

class ProductListView(View):
    def get(self, request):
        category     = request.GET.get('category')
        sub_category = request.GET.get('sub_category')
        price        = request.GET.get('price')
        print(request.GET)

        q = Q()

        if category:
            q &= Q(sub_category__category_id= category)

        if sub_category:
            q &= Q(sub_category_id = sub_category)

        product_list = Product.objects.filter(q)

        if price:
            product_list = product_list.order_by(price)

        results = [{
                    "name"                     : product.name,
                    "price"                    : int(product.price),
                    "weight"                   : product.weight,
                    "sub_name"                 : product.sub_name,
                    "description"              : product.description,
                    "sub_category"             : product.sub_category.name,
                    "sub_category_image"       : product.sub_category.image,
                    "sub_category_description" : product.sub_category.description,
                    "category"                 : product.sub_category.category.name,
                    "category_image"           : product.sub_category.category.image,
                    "category_description"     : product.sub_category.category.description,
                    'tags'                     : [tag.name for tag in product.tags.all()],
                    "product_image"            : [image.url for image in product.productimage_set.all()]
            } for product in product_list]

        return JsonResponse({'results' : results}, status = 200)