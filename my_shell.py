python manage.py shell
from shop.models import Item, Purchase
from django.utils import timezone
i1 = Item(name="Microwave", price=10000)
i2 = Item(name="Vacuum cleaner", price=20000)
i3 = Item(name="Toaster", price=5500)
i4 = Item(name="Notebook", price=75000)
i5 = Item(name="Monitor", price=35000)
i1.save()
i2.save()
i3.save()
i4.save()
i5.save()
Item.objects.all()
i1.purchase_set.create(name="Steph", age=32, date_purchase=timezone.now())
i1.purchase_set.create(name="Dirk", age=35, date_purchase=timezone.now())
i2.purchase_set.create(name="Dirk", age=35, date_purchase=timezone.now())
i2.purchase_set.create(name="James", age=33, date_purchase=timezone.now())
i3.purchase_set.create(name="Jordan", age=39, date_purchase=timezone.now())
i3.purchase_set.create(name="Johnson", age=38, date_purchase=timezone.now())
i4.purchase_set.create(name="Luka", age=28, date_purchase=timezone.now())
i4.purchase_set.create(name="Ermek", age=31, date_purchase=timezone.now())
i5.purchase_set.create(name="Ermek", age=31, date_purchase=timezone.now())
i5.purchase_set.create(name="Shaq", age=35, date_purchase=timezone.now())
