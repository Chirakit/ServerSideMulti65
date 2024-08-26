https://github.com/it-web-pro/django-week2
# รหัส: password


# Week 2
## WINDOW Install virtualenv
```bash
pip install virtualenv
```

Create a virtual environment
```bash
py -m venv myvenv
```

Activate virtual environment
```bash
myvenv\Scripts\activate.bat
```
---
## MacOS Install virtualenv
```bash
pip install virtualenv
```

Create a virtual environment
```bash
python -m venv myvenv
```

Activate virtual environment
```bash
source myvenv/bin/activate
```

```bash
django-admin startproject mysite
```
```python
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py # สำหรับตั้งค่า project
        urls.py # สำหรับกำหนด path url
        asgi.py
        wsgi.py
```
Run server
```
py manage.py runserver <port>
```

## Start app
```bash
py manage.py startapp <app>
```
## คำสั่งในการเข้า Shell ใน Postgres
```sh
psql -U postgres
```
## คำสั่งในการแก้ไข Database
คำสั่งต้องทำคู่กันเมื่อมีการแก้ไข models.py
```bash
python manage.py makemigrations <Optional app>
```
ใช้เมื่อมีการแก้ไขไฟล์ models.py

```bash
python manage.py migrate <Optional app> <Optional number of migrations>
```

ใช้เพื่อให้ระบบนำไปอัพเดทข้อมูลในฐานข้อมูล ถ้ามีการแก้ไข Models

## คำสั่งภายใน Shell Django
```bash
<Table>.objects.all()
```
```bash
<Table>.objects.first()
```
```python
<Table>.objects.get(pk=)
<Table>.objects.get(id=)
# pk คือ ID
```
```python
.save()
# ใช้เมื่อต้องการบันทึกข้อมูลลงฐานข้อมูล
```

```python
.<Table>_set.count()
# ใช้เมื่อ Tables นั้นมีความสัมพันธ์ 1-M โดย Table เป็น 1 (เช่น choice_set)
```
```bash
<Table>.objects.filter(question_text__icontains="llo")
```
```python
<Table>.objects.filter(question_text__startswith="What")
# แสดงข้อมูลที่มีการกำหนดประโยคภายใน
```
```python
<Table>.objects.filter(<Table_FK>_id=1, ...)
# แสดงข้อมูลตาม ID โดยมี _id โดยต้องมี Foreign Key
```
```python
print(<คำสั่งที่เรียกข้อมูล>.query)
# แสดง SQL Query ที่คำสั่งใช้ใน Database
```
```python
<Table>.objects.all().delete()
# ลบข้อมูลทั้งหมดใน Table
```
`{% <command> %}` command เป็นโค้ด Python

ถ้าเพิ่ม Template แล้วเข้าไปไม่ได้ให้รัน python manage.py runserver ใหม่

## Add django-extensions for notebook .ipynb
```bash
pip install django-extensions ipython jupyter notebook
```
แก้ไขเวอร์ชั่น MAC
```bash
pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2 notebook==6.5.6
```
แก้ไขเวอร์ชั่น WINDOW
```bash
pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2 notebook==6.5.7
```
ใน setting.py ต้องทำการเพิ่ม `django_extensions` เป็นส่วนหนึ่งของตัวแปร INSTALLED_ADDS ด้วย
```python
py manage.py shell_plus --notebook # ทำการเปิด Shell ผ่าน Notebook
```
และที่สำคัญคือต้องเลือก Run Script เป็น `Django Shell-Plus` ด้วย

# Week 3
## **Importance**
เมื่อมีการใช้งาน ForeignKey Field อย่างเช่น
```python
created_by_id = models.ForeignKey(Author, on_delete=models.PROTECT)
# เมื่อ Migrate จะทำการสร้าง Column ที่มีชื่อตามตัวแปร + _id ต่อท้ายให้ทำให้เป็น
# created_by_id_id
```
> **Note:** models.ForeignKey จะทำการเพิ่ม _id ต่อหลัง Field

เมื่อมีการใช้งาน ManyToMany Field อย่างเช่น
```python
categories = models.ManyToManyField("blogs.Category")
# จะสร้าง Table ที่่มีชื่อที่ขึ้นต้นด้วย Table ที่สร้าง Column นี้โดยอันนี้คือ blog ตามด้วย _<Field>
# blog_categories
# และจะสร้าง Foreign Key ที่มีชื่อของ ทั้ง Table ที่ใช้สร้าง Column นี้กับ Table ที่เชื่อมไปคือ blog กับ Category และทั้งสองจะมี _id ต่อท้าย
# blog_id กับ category_id

cartItem = models.ManyToManyField("shop.Product", through="CartItem")
# ถ้ามี Column มากกว่า FK
```

เมื่อมีการใช้งาน Decimal Field อย่างเช่น
```python
models.DecimalField(..., max_digits=5, decimal_places=2)
# ตัวเลขที่ใส่ได้มากที่สุดคือ 999.99 มาจากการเอา max_digits - decimal_places = 3 ก็คือจะต้องใส่ 9 สามตัว และ decimal_places คือจะต้องใส่ 9 สองตัว หลัง . หรือก็คือมีทศนิยมได้ 2 ตำแหน่ง
# 999.99

models.DecimalField(..., max_digits=19, decimal_places=10)
# 999999999.9999999999 ประมาณคือใส่ได้เยอะสุดเกือบ 1 พันล้าน
```

## Date/Datetime Field
`models.DateField()`

`models.DateTimeField()`
### Arguments
```python
auto_now_add=True # เมื่อสร้าง Field นี้จะใส่เวลาปัจจุบันในอัตโนมัติ
auto_now=True # เมื่อมีการเพิ่ม และอัพเดท Field นี้จะใส่เวลาปัจจุบันในอัตโนมัติ
```

## Foreign Key
```python
models.CASCADE # เมื่อ Parent ถูกลบจะไปลบข้อมูล Child ที่มี ID ของ Parent อยู่
models.PROTECT # เมื่อ Parent จะถูกลบจะปกป้องไม่ให้ถูกลบหาก Child ที่มี ID ของ Parent ยังอยู่
```

# Datetime
```python
import datetime as dt
import zoneinfo as zi
from django.utils import timezone

dt.datetime.now() # ให้เวลาปัจจุบัน แต่ไม่มี Timezone: NAIVE
timezone.now() # ให้เวลาปัจจุบัน ที่มี Timezone +0.00 UTC: AWARE

timezone.make_aware(<datetime>) # ต้องเป็น naive ใส่ Timezone ให้เป็นตาม setting.py
timezone.localtime(<datetime>) # ต้องเป็น aware ใส่ Timezone ให้เป็นตาม setting.py

timezone.is_aware(<datetime>) # True ถ้ามี Timezone
timezone.is_naive(<datetime>) # True ถ้าไม่มี Timezone
zi.ZoneInfo(key="Asia/Bangkok")

dt.timedelta(weeks=1, days=1, hours=1, minutes=1, seconds=1, milliseconds=1, microseconds=1) # สามารถเอาไป + กับ Datetime เพื่อเพิ่มเวลาได้

<dt>.strftime("%a | %A") # บอกวัน
<dt>.strftime("%b | %B") # บอกเดือน
<dt>.strftime("%c | %C") # บอกวัน เดือน วันที่ วันเวลา ปี | บอกศตวรรษ
<dt>.strftime("%d | %D") # บอกวันที่ | บอกวันเดือน/วันที่/ปี เป็นเลข
<dt>.strftime("%y | %Y") # บอกปีแต่ไม่บอก ศตวรรษ | บอกปี
<dt>.weekday() | <dt>.strftime("%w") # บอก 0-6 {0: Monday, .., 6: Sunday}
```

# Week 4

## Insert Data
วิธีสร้าง row หรือเพิ่มข้อมูลเข้าไปใน Table
```python
from blog.models import Blog, Author, Entry
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()
```
อีกโดยวิธีนี้ไม่ต้อง
`save()` ก็จะเพิ่มข้อมูลเข้าไปใน Database ทันที
```python
b = Blog.objects.create(name="Beatles Blog", tagline="All the latest Beatles news.")
```

### ManyToMany ให้ใช้ `add()` กับ Table ที่สร้างขึ้นมาโดยสามารถเพิ่มได้ในหลายข้อมูลพร้อมกัน เพิ่มข้อมูลเข้าไปใน Database ทันที
```python
john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, george, ringo)

# Opposite
john.entry_set.add(e1, e2, e3) # สามารถใช้ Author ก่อนได้ แต่ต้องระบุเป็น Table_set.add(<object_Table>)
```

## Select Data
ข้อมูลที่จะได้มาจะเป็น Instance ของ Class **QuerySet**

```Python
Entry.objects.all() # SELECT * FROM entry;

Table.objects.filter().dictinct() # จะได้แบบ Unique Row
```

```python
Entry.objects.filter(pub_date__year=2010) # SELECT * FROM entry WHERE pub_date=2010;
```

สามารถใช้ Lookup __type ตามด้วยความหมายที่ต้องการดึง
```python
__exact=""|0|None # field="", field=0, field is NULL
__iexact=""|0|None # เหมือนกับ exact แต่เป็น case-insensitive ILIKE "" | ILIKE 0 | IS NULL
__contains="K" # LIKE %K%
__icontains="K" # ILIKE %K% เป็น case-insensitive
__startswith="K" # LIKE K%
__istartswith="K" # ILIKE K%
__endswith="K" # LIKE %K
__iendswith="K" # ILIKE %K
__in = [1, 2, 3]|"abc" # IN (1, 2, 3) | IN ("a", "b", "c")
__gte=1 # >= 1
__gt=1 # > 1
__lte=1 # <= 1
__lt=1 # < 1
__range=(1, 2)|(date, date) # BETWEEN data AND date
__date=datetime # หมายความว่าที่ใส่ไปคือ type date || __date__gt || __date__gte ใช้ น้อยกว่า มากกว่า เพิ่มเติมได้
__year=2005 # แปลงเป็น BETWEEN '2005-01-01' AND '2005-12-31'
__year__gt=2005 # แปลงเป็น > "2005-01-01"
<field>__avg
<field>__count
<field>__max
<field>__min
<field>__sum
<field>__isnull=True
```
```python
Entry.objects.filter(headline__startswith="What").exclude(
    pub_date__gte=datetime.date.today()
).filter(pub_date__gte=datetime.date(2005, 1, 30))
```
`values(field1, field2, ..)` สามารถนำมาใช้กับการดึงข้อมูลแค่ Column ที่ต้องการได้
```python
Author.objects.all().values("name")
# <QuerySet [{'name': 'John'}, {'name': 'Joe'}, {'name': 'Paul'}, {'name': 'George'}, {'name': 'Ringo'}, {'name': 'John2'}, {'name': 'Test'}, {'name': 'Test'}]>
```
สามารถเอาไปประยุกต์กับการใช้ Lookup ได้ด้วยการ
```python
authors = Entry.objects.filter(pk=1).values("authors")
for i in Author.objects.filter(id__in=authors):
    print(i)
```

เลือกข้อมูลจากใน Table สามารถกำหนดเงื่อนไขผ่าน arguments ที่ Model มี
`<Table>.objects.get(column1="", column2="", ...)`
```python
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
```

### ข้อแตกต่างของ `get()` กับ `filter()`

- get() สามารถดึงข้อมูลเพียงแค่ตัวเดียว แล้วสามารถใช้ข้อมูลได้เลย แต่นั้นก็ทำให้ต้อง ***กำหนดเงื่อนไขให้ได้แค่ข้อมูลเดียว***
- filter() สามารถดึงข้อมูลได้ >= 1 ตัว แต่ต้องเข้าไปในแต่ละตัวเพื่อใช้งาน โดยจะได้เป็น `QuerySet`

```python
one_entry = Entry.objects.get(pk=1)
one_entry = Entry.objects.filter(pk=1).first()
one_entry = Entry.objects.filter(pk=1)[0]
# ทั้ง 3 บรรทัดนี้ให้ผลเหมือนกัน
```

### Limit ข้อมูลที่ต้องการ Query
การทำ Query อย่าง `SELECT * FROM table LIMIT 5` เพื่อประหยัดเวลาในการประมวลผลดึงข้อมูล

```python
Entry.objects.all()[:5] # LIMIT 5
Entry.objects.all()[5:11] # OFFSET 5 LIMIT 5
Entry.objects.all()[1:5] # OFFSET 1 LIMIT 4
Entry.objects.all()[:-1] # ! ERROR ValueError: Negative indexing is not supported.
```

### Compare ข้อมูล
เช็คข้อมูลว่าเป็นตัวเดียวกันหรือป่าวใช้ `==`

```python
author_1 = Author.objects.get(pk=1)
author_j = Author.objects.get(name="John")
author_1 == author_j # True
author_1.id == author_j.id # True
```

### Delete ข้อมูล
ลบข้อมูลออกจาก Database จากการใช้ `delete()`

```python
Author.objects.filter(name__startswith="T").delete() # ลบ Author ที่มีชื่อขึ้นต้นด้วย T
# (2, {'blog.Author': 2})
Author.objects.get(name="John").delete() # ลบ Author ที่ชื่อว่า John
# (1, {'blog.Author': 1})
Author.objects.all().delete() # ลบข้อมูลทั้งหมดใน Author
# (10, {'blog.Author': 10})
```

**ManyToMany** ถ้าต้องการลบ หรือล้างข้อมูลการเชื่อมกัน
```python
entry.authors.remove(john, paul, george, ringo) # เป็นการลบข้อมูลออกจาก Table ManaToMany
entry.authors.clear() # ลบทุกความสัมพันธ์ออกจาก Entry ใน Authors ที่เป็น Table ManaToMany
```

### Copy ข้อมูล

คัดลอกข้อมูลที่มีรายละเอียดเหมือนกัน โดยจะทำการลบ pk แล้วให้ใช้ `_state_adding = True` เป็นการเพิ่ม pk ใหม่อัตโนมัติ ต้องมีการ `save()` ด้วยเพื่อเพิ่มข้อมูลลงไป
```python
test = Author.objects.create(name="Test") # Author.objects.get(pk=1) || Author.objects.get(name="John")
test.pk = None
test._state_adding = True
test.save()
```

### Raw (query) ข้อมูล

การเขียน SQL Query ที่ต้องการโดยไม่ใช้ API จาก Django

## One to One Field Retrive Data

การดึงข้อมูลจากการใช้ความสัมพันธ์แบบ OneToOne ยกตัวอย่าง Order และ Payment มีความสัมพันธ์แบบ OneToOne โดยมีข้อมูลโครงสร้างดังนี้

```python
class Order(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    orderItem = models.ManyToManyField(Product, through='shop.OrderItem')

class Payment(models.Model):
    order = models.OneToOneField(Order, models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
```

จะเห็นว่า Payment มี field order อยู่ทำให้เวลาเรามี object ของ Payment เราจะสามารถดึงข้อมูลจาก Order ที่เชื่อมได้เลยอย่าง

```python
payment = Payment.objects.get(pk=1)
payment.order.order_date # Payment นี้ให้ดึงว่า Order เวลาไหน

order = Order.objects.get(pk=1)
order.payment.price # Order นี้ให้ดึงว่า payment ราคาเท่าไร
```

## Many to Many Field Retrive Data

การดึงข้อมูลโดยมีความสัมพันธ์แบบ ManyToMany จะแตกต่างกันโดยจะได้ข้อมูลมา
```python
class Order(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    remark = models.TextField(null=True)
    orderItem = models.ManyToManyField(Product, through='shop.OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    amount = models.IntegerField(default=1)
```

เราสามารถดึงข้อมูล OrderItem ผ่าน Order ได้เลยโดยวิธีดึงให้ใช้
```python
order = Order.objects.get(pk=1)
order.orderItem.all() # ดึงข้อมูล orderItem ทั้งหมด และจะสามารถดึงข้อมูลจาก field ที่ต้องการได้
```

ในกรณีที่อยากได้ amount ใน OrderItem ให้
```python
order = Order.objects.filter(order_date__month=5)[:10]
for i in order:
    for j in i.orderitem_set.all():
        print(j.amount, j.product.name, j.product.price)
```

**! ระวัง**
* `order.OrderItem.all()` อันนี้ดึงข้อมูลจาก Field ใน Order ที่ลิงค์ไปหา Product ทันทีเพราะงั้นคำสั่งนี้จะได้แค่ Product
* `order.orderitem_set.all()` อันนี้ดึงข้อมูลผ่าน Table OrderItem ทำให้ได้ Field ทั้งหมดใน OrderItem และดึงข้อมูล amount ได้

## One to One/Many Field Retrive Data
การดึงข้อมูลจาก Table ที่มี Foreign Key สามารถทำได้โดย
```python
<Parent>.objects.filter(<Child>__<Field_Child>)
<Child>.objects.filter(<Field_ForeignkeyParent>__<Field_Parent>)
```

### Playground

เมื่อต้องการ filter ข้อมูลที่เป็น field แบบ ManyToMany สามารถใช้ __ แล้วตามด้วย field ของ Table ที่เชื่อมเช่น
```python
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory)
```

เราต้องการได้ Product แต่งื่อนไขคือต้องเป็นประเภท "Technologies" ซึ่งต้องดึงข้อมูลจาก categories ที่เป็น name มาโดยสามารถใช้
```python
product = Product.objects.filter(categories__name="Technologies") # ดึงข้อมูลสินค้าที่มีประเภท "Technologies"
```
ก็จะได้ข้อมูลที่ต้องการมา

## IMPORTANT 
`dir(<object>)` เพื่อ Function และ Attribute ของ Object มาดู


# Week 5
[Django Doc: query-expressions](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#query-expressions)


```python
pip install <library> <library> ...
```

จะเรียนเกี่ยวกับ Expressions ที่ใช้ได้จาก django.db.models และ built-in ของ Django
```python
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from django.db.models.lookups import GreaterThan
```

## Functions F()

ฟังชั่น F ใช้เมื่อต้องการคำนวณโดยใช้ข้อมูล Field ใน Table
```python
Company.objects.filter(num_employees__gt=F("num_chairs"))

Company.objects.filter(num_employees__gt=F("num_chairs")).annotate(chairs_needed=F("num_employees") - F("num_chairs")).first()
```

`annotate()` ใช้เมื่อต้องการคำนวณข้อมูลเพิ่มเติม โดยการกำหนดชื่อ Field และข้อมูลที่ต้องการ เมื่อจะเข้าถึงข้อมูลให้ทำเหมือนเป็น Attribute อีกตัว

## Functions Upper(), Value()

* `Value()` กำหนดว่าหมายถึงอันนี้เป็น ค่าจริง ๆ ไม่ใช่ส่ง Field ให้
* `<object>.refresh_from_db()` ดึงข้อมูลจาก Database จาก Object ที่เรียก
```python
# 1
company = Company.objects.create(name="Google", ticker=Upper(Value("goog")), num_employees=100, num_tables=100, num_chairs=200)
company.ticker
# Upper(Value("goog"))

company.refresh_from_db()
company.ticker
# 'GOOG'

# 2
company = Company.objects.create(name="Google", ticker="goog".upper(), num_employees=100, num_tables=100, num_chairs=200)
company.ticker
# 'GOOG'

# Error
company = Company.objects.create(name="Google", ticker=Upper("goog"), num_employees=100, num_tables=100, num_chairs=200)
```

## Function Length()

ฟังชั่นที่ดึงข้อมูลจาก Field มาดูว่ามีความยาวเท่าไร หรือก็คือแปลงข้อมูลของ Field ที่ใส่เข้าไปเป็นความยาว
```python
Length("<field>")
```

ตัวอย่าง
```python
Company.objects.order_by(Length("name").asc())
# <QuerySet [<Company: Google>, <Company: Google2>, <Company: Company AAA>, <Company: Company BBB>, <Company: Company CCC>]>

Company.objects.order_by(Length("name").desc())
# <QuerySet [<Company: Company AAA>, <Company: Company BBB>, <Company: Company CCC>, <Company: Google2>, <Company: Google>]>
```

## Function GreaterThan()
ฟังชั่นที่ใช้เปรียบค่าระหว่าง Argument1 กับ Argument2
```python
Company.objects.filter(GreaterThan( F("num_employees"), F("num_chairs") )) # num_employees > num_chairs
# ให้ข้อมูลที่ num_employeees > num_chairs

Company.objects.annotate(needed_chairs=GreaterThan(F("num_employees"), F ("num_chairs") ))
# ให้ข้อมูลทั้งหมด แต่ทุกข้อมูลที่ได้มาจะมี Field needed_chairs ที่เป็น Boolean โดยถ้าเป็น True คือ num_employeees > num_chairs
```

## Function Avg()
ฟังชั่นในการคำนวณค่าเฉลี่ยของ Field ที่ใส่เข้าไป
```python
from django.db.models import Avg
Book.objects.aggregate(Avg("price", default=0))
# {'price__avg': Decimal('9.7018644067796610')}
```

## Function Max()
ฟังชั่นในการหาค่าสูงสุดของ Field ที่ใส่เข้าไป
```python
from django.db.models import Max
Book.objects.aggregate(Max("price", default=0))
# {'price__max': Decimal('14.99')}
```

## Function Count()
ฟังชั่นนับจำนวน Row ของ Table ที่ใส่เข้าไป โดยต้องเป็น แม่ของ Foreign Key
```python
from django.db.models import Count
pubs = Publisher.objects.annotate(num_books=Count("book"))
# <QuerySet [<Publisher: Publisher object (1)>, <Publisher: Publisher object (2)>]>
pubs.first().num_books
# 20
```
> **Note:** Book มี Foreign key ของ Publisher

```python
pubs = Publisher.objects.annotate(num_books=Count("book")).order_by("-num_books")[:5]
pubs[0].num_books
pubs[len(pubs)-1].num_books
```

> **Note:** `annotate()` เป็นการสร้าง Field เพิ่มขึ้นมา ทำให้สามารถใช้ `order_by(<field>)` ได้

## Function Q()
ทำให้สามารถดึงค่าข้อมูลเสมือนการทำ Select ใน Select

```python
above = Publisher.objects.annotate(above_4=Count("book", filter=Q(book__rating__gt=4)))
below = Publisher.objects.annotate(below_4=Count("book", filter=Q(book__rating__lte=4)))
```

## Funtion values_list()
เป็นฟังชั่นที่ดึงค่า field ออกมาตามที่ต้องการให้แสดง โดยจะให้มาเป็น List ของ QuerySet
```python
penguin_pub.book_set.filter(name__startswith="The").values_list("id", flat=True)
# <QuerySet [1, 5, 8, 14, 17]>

penguin_pub.book_set.filter(name__startswith="The").values_list("id")
# <QuerySet [(1,), (5,), (8,), (14,), (17,)]>

penguin_pub.book_set.filter(name__startswith="The").values_list("id", "name")
# <QuerySet [(1, 'The Great Gatsby'), (5, 'The Catcher in the Rye'), (8, 'The Odyssey'), (14, 'The Hobbit'), (17, 'The Hitchhiker Guide to the Galaxy')]>
```
> **Note:** ถ้ามีการใส่ Field มากกว่า 1 จะไม่สามารถใช้ Argument flat=True ได้

## Function values()
ฟังชั่นแปลงค่า Object ที่ดึงข้อมูลทั้งหมดมาเป็น JSON

## Function annotate() กับ values() เพื่อทำการ Group by
เราสามารถทำการนับค่าทั้งหมดโดยแบ่งแยกประเภท หรือข้อมูลที่มีค่าเหมือนกันใน Field ใด Field หนึ่งได้จากการใช้ Annotate และ Values
```python
Product.objects.filter(categories__name__in=("Clothing and Apparel", "Furniture"), price__range=(1000, 10000)).
values("categories__name").annotate(count=Count("categories"))
# โดยจะเห็นว่าเป็นการแยกประเภทของ สินค้า ผ่านชื่อของประเภทสินค้า และค่อยนับไปใส่ใน Field count
```

## IMPORTANT ตั้งค่า Database ให้แต่ละ App

ถ้าต้องการให้ App แต่ละอันใช้ Database ต่างกันให้ใช้

```python
# setting.py
DATABASES = {
    'default': {},
    'books': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'books',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'companies': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'companies',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASE_ROUTERS = ['books.dbRouter.BookDBRouter', 'companies.dbRouter.CompanyDBRouter']
```
```python
# <app>/dbRouter.py ยกตัวอย่างของ app books
class BookDBRouter(object):
    """
    A router to control db operations
    """
    route_app_labels = {'books'}
    db_name = 'books'

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to self.db_name.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to self.db_name.
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        self.db_name database.
        """
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None
```
- `py manage.py makemigrations <app_name>`
- `py manage.py migrate --database=<database_name>`


`.aggregate` เหมือนการทำ `Group by` ที่ได้ผลลัพธ์ตามข้อมูลใน Column อยากให้ลองทำ Exercise ใหม่ดู ข้อที่นับ Categories

# Week 6
ดูใน Folder week 6

# Week 7
## Show database in postgres
```bash
\l
```

## Escaping characters
```
< is converted to &lt;
> is converted to &gt;
' is converted to '
" is converted to "
& is converted to &amp;
```

[Doc variable in templates](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
## Filter (Template) 1
```python
value|length # ได้รับความยาว หรือขนาดกลับมา
{# command #} # เพื่อคอมเมนต์
include <file.html> # คล้ายกับ PHP
value|safe # ทำให้ตัวอักษรไม่แปลงค่า (No auto-escaping)

# Date
value|date # ทำให้เป็น Date
value|date:'c' # ทำให้แสดงเป็นแบบ YYYY:MM:DD เป็นเลข
value|date:"Y-m-d" # แสดงเป็น YYYY-MM-DD เป็นเลข

value|add:"string" # ต่อ String
value|add:second
value.function # เมื่อ Value นั้น ๆ มี Function ไม่ต้องใส่ ()
csrf_token # ให้ Token ที่ใส่ใน CSRF
```
```
This will be escaped: {{ data }} | This will be escaped: &lt;b&gt;
This will not be escaped: {{ data|safe }} | This will not be escaped: <b>
```

[Doc {% %}](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#json-script)
## Function in {%%} (Templates)
```python
for i in value | for i in range(start=0, end, step=1)
endfor

if elif else
endif

url '<nameofPath>' <optional-argument> <optional-argument> <optional-argument> ..
```

[Doc Request](https://docs.djangoproject.com/en/5.0/ref/request-response/)
## Request | HttpRequest
```python
request.scheme # แสดงว่าเป็น http|https
request.body # ข้อมูลที่ส่งผ่าน Method
request.path # แสดง Path ที่ถูกติดต่อ (urls.py)
request.content_type # แสดง Type ของ Content (ex. application/json)
request.GET # เมื่อ Method เป็น Get สามารถใช้อย่างงี้เพื่อใช้ .get("<argument>")
request.POST # เมื่อ Method เป็น Post สามารถใช้อย่างงี้เพื่อใช้ .get("<argument>")
request.method # แสดง method
request.COOKIES # แสดง cookies
request.META # แสดงข้อมูลของข้อมูล Request
request.headers # แสดงข้อมูล headers สามารถใช้ get ได้
request.get_host() # ได้ Address:port ของ Request
request.get_port() # ได้ Port ของ Request
```

## Convert bytes to JSON
```python
# views.py
content = request.body.decode("utf-8") # ได้ข้อมูลจาก body เป็น bytes เลยต้องทำการ Decode
content_json = json.loads(content) # แปลงข้อมูลเป็น json
employee_id = content_json['emp_id']
# or
content_json = json.loads(request.body) # แปลงข้อมูลเป็น json
employee_id = content_json['emp_id']
```
```python
# templates/*.py
const data = {'emp_id': emp_id}
fetch(`/employees/projects/{{ project.id }}/addStaff/`, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}' // มี
    },
    body: JSON.stringify(data) # อันนี้คือข้อมูลที่ Request ส่งมา
})
.then(response => response.json())
.then(data => {
    console.log('Item updated successfully')
    window.location.reload()
})
.catch(error => console.error('Error:', error));
```

## JsonResponse
เมื่อ Template ต้องการให้ตอบกลับเป็น JSON
```python
# views.py
JsonResponse({'foo':'bar'}, status=200)
# or
HttpResponse("\"{'status':'0'}\"")
```
```python
# templates/*.py
...
.then(response => response.json())
...
```

## Decorator
```python
def hook(func):
    def test(x, y):
        print(x, y)
    return test

@hook
def test2(x, y):
    return (x, y)

test2(1, 2)
# 1 2
```
## Best Practice
`ควรใส่ urls.py ในแต่ละ app แล้วค่อยไป include ที่ urls.py ที่ตัวหลัก`
```python
# main-app/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include("employee.urls"))
]
```

## Import app
![PNG](./images/week7-1.png)

## Undefine type
![PNG](./images/week7-2ไม่บอกType.png)


# Week 8

## Static
```py
# main/settings.py
INSTALLED_APPS = [ "django.contrib.staticfiles" ]
...
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

# main/templates/*.html
{% load static %}
{% static 'FILE PATH IN STATIC FOLDER' %}
```

## Block
ใน `<name>.html` แบ่งโครงสร้างเว็บเป็น 3 ส่วนซึ่งช่วยในการจัดหน้าเว็บให้ง่ายขึ้นโดย
1. title
2. sidebar
3. content

หรือจะไม่เหมือนกันก็ได้ โดยจะใส่ตามใน `<name>.html`
```py
# <name>.html
<!DOCTYPE html>
<html>
    <body>
    <h1>Welcome</h1>

    {% block title %}
        <h2>Title</h2>
    {% endblock %}

    {% block sidebar %}
        <h2>Sidebar<h2>
    {% endblock %}

    {% block content %}
        <h2>Content<h2>
    {% endblock %}

    <p>
        Check out the two templates to see what they look like, and views.py to see the reference to the child template.
    </p>

    </body>
</html>

# other.html
{% extends "<name>.html" %}
{% block title %} content {% endblock %}
{% block sidebar %} content {% endblock %}
{% block content %} content {% endblock %}
```
> **Note:** หากไม่ได้กำหนด Block ที่กำหนด จะเอาข้อมูลใน `<name>.html` ไปใส่

## Escape
### Block-level
```python
{% autoescape off/on %} {% endautoescape %}
```
### Filter-level
```py
value|safe
value|escape
'{{ value|escapejs }}' # สำหรับการใช้กับ Javascript String ใน '' หรือ ""
```

## Forloop (Template)
[Doc](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#for)
```py
{% cycle 'row1' rowvalue 'row2' %} # จะทำการลูปเริ่มตั้งแต่ตัวแรก จนถึงตัวท้าย แล้วเริ่มที่ตัวแรกใหม่ ใช้ใน {% for %}
{% for %} {% empty %} {% endfor %} # empty ใช้กับ for หาก for ไม่ลูปจะแสดงข้อมูลที่ empty
{% ifchanged %} # Check ว่าข้อมูลมีการเปลี่ยนแปลงจากการลูปครั้งก่อนไหม
```
### Variable
| Variable              | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| `forloop.counter`     | The current iteration of the loop (1-indexed)                  |
| `forloop.counter0`    | The current iteration of the loop (0-indexed)                  |
| `forloop.revcounter`  | The number of iterations from the end of the loop (1-indexed)  |
| `forloop.revcounter0` | The number of iterations from the end of the loop (0-indexed)  |
| `forloop.first`       | True if this is the first time through the loop                |
| `forloop.last`        | True if this is the last time through the loop                 |
| `forloop.parentloop`  | For nested loops, this is the loop surrounding the current one |

## Filter (Template) 2
[Doc](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#std-templatefilter-escape)
```py
value|join:'<string>'
value|filesizeforma # บอก Size ของ value เป็น Format ที่อ่านรู้เรื่อง (13 KB, 4.1 MB, 102 bytes)
value|first # return first item in list
value|last
value|floatformat:N # N ให้บอกทศนิยม Default=1 ถ้าเป็น Int Default=0 N=[-inf, inf]
value|floatformat:"Ng" # จะมีการแยกจุดพันให้ ex.3,400 โดย N ยังกำหนดเหมือนเดิม
value|get_digit:"N" # n=2; value is 123456789, the output will be 8
value|lower
value|title # "asdf As e" = "Asdf As E"
value|capfirst
value|ljust:"N" # กำหนด Space ถ้าไม่ถึงจะเว้นระยะไปทางซ้าย
value|rjust:"N" # กำหนด Space ถ้าไม่ถึงจะเว้นระยะไปทางขวา
value|center:"N" # ทำให้ String อยู่ตรงกลางตามตัวอักษรที่กำหนด
value|slice:':N' # n=2; value=['a', 'b', 'c'], the output will be ['a', 'b']
value|truncatechars:N # กำหนดจำนวนอักษรที่จะแสดง และถ้าเกินที่เหลือจะเป็น ... เช่น Joel i…
value|make_list # value="Joel", output=['J', 'o', 'e', 'l']
value|pluralize # value >= 2 จะได้ s กลับมา เหมาะกับการทำ 1 day, 2 days
value|random # value=[1,2,3,4] random มา 1 ตัว
value|wordcount # value="Joel is a slug", the output will be 4.
value|cut:"<String>" # string=" "; value="String with spaces", the output will be "Stringwithspaces".
value|default:"<String>" # value==False display <string>
value|default_if_none:"<String>" # value==None display <string>
value|dictsort:"<Attribute>" # value=dict Attribute=attribute in dict
```

### Date format (Filter)
[Date format](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#date)
| Format character	| Description |Example output |
| ----------------- | ----------- | --------------| 
| Day               |
| d                 | Day of the month, 2 digits with leading zeros.	|'01' to '31'
| j                 |  Day of the month without leading zeros.	|'1' to '31'
| D                 |  Day of the week, textual, 3 letters.	|'Fri'
| l                 |  Day of the week, textual, long.	|'Friday'
| S                 |  English ordinal suffix for day of the month, 2 characters.	|'st', 'nd', 'rd' or 'th'
| w                 |  Day of the week, digits without leading zeros.	|'0' (Sunday) to '6' (Saturday)
| z                 |  Day of the year.	|1 to 366
| Week	 	 
| W                 |  ISO-8601 week number of year, with weeks starting on Monday.	| 1, 53
| Month	 	 
| m                 |  Month, 2 digits with leading zeros.|	'01' to '12'
| n                 |  Month without leading zeros.	|'1' to '12'
| M                 |  Month, textual, 3 letters.	|'Jan'
| b                 |  Month, textual, 3 letters, lowercase.	|'jan'
| E                 |  Month, locale specific alternative representation usually used for long date representation.|	'listopada' (for Polish locale, as opposed to 'Listopad')
| F                 |  Month, textual, long.|	'January'
| N                 |  Month abbreviation in Associated Press style. Proprietary extension.	|'Jan.', 'Feb.', 'March', 'May'
| t                 |  Number of days in the given month.	|28 to 31
| Year	 	 
| y                 | Year, 2 digits with leading zeros.	|'00' to '99'
| Y                 | Year, 4 digits with leading zeros.	|'0001', …, '1999', …, '9999'
| L                 | Boolean for whether it’s a leap year.	|True or False
| o                 | ISO-8601 week-numbering year, corresponding to the ISO-8601 week number (W) which uses leap weeks. See Y for the more common year format.|	'1999'
| Time	 	 
| g                 |  Hour, 12-hour format without leading zeros. |	'1' to '12'
| G                 |  Hour, 24-hour format without leading zeros.	|'0' to '23'
| h                 |  Hour, 12-hour format.	|'01' to '12'
| H                 |  Hour, 24-hour format.	|'00' to '23'
| i                 |  Minutes.	|'00' to '59'
| s                 |  Seconds, 2 digits with leading zeros.	|'00' to '59'
| u                 |  Microseconds.	|000000 to 999999
| a                 |  'a.m.' or 'p.m.' (Note that this is slightly different than PHP’s output, because this includes periods to match Associated Press style.)	|'a.m.'
| A                 |  'AM' or 'PM'.	|'AM'
| f                 |  Time, in 12-hour hours and minutes, with minutes left off if they’re zero. Proprietary extension.	|'1', '1:30'
| P                 |  Time, in 12-hour hours, minutes and ‘a.m.’/’p.m.’, with minutes left off if they’re zero and the special-case strings ‘midnight’ and ‘noon’ if appropriate. Proprietary extension.	'1 a.m.', '1:30 p.m.', 'midnight', 'noon', '12:30 p.m.'
| Time zone	 	 
| e                 |  Timezone name. Could be in any format, or might return an empty string, depending on the datetime.	| '', 'GMT', '-500', 'US/Eastern', etc.
| I                   Daylight saving time, whether it’s in effect or not.	|'1' or '0'
| O                 |  Difference to Greenwich time in hours.	|'+0200'
| T                 |  Time zone of this machine.	|'EST', 'MDT'
| Z                 |  Time zone offset in seconds. The offset for timezones west of UTC is always negative, and for those east of UTC is always positive.	| -43200 to 43200
| Date/Time	 	 
| c                 |  ISO 8601 format. (Note: unlike other formatters, such as “Z”, “O” or “r”, the “c” formatter will not add timezone offset if value is a naive datetime (see datetime.tzinfo).	| 2008-01-02T10:30:00.000123+02:00, or 2008-01-02T10:30:00.000123 if the datetime is naive
| r                 |  RFC 5322 formatted date. |	'Thu, 21 Dec 2000 16:01:07 +0200'
| U                 |  Seconds since the Unix Epoch | (January 1 1970 00:00:00 UTC).	 

## Tips
- หากแก้ไข Javascript ที่อยู่ใน Static แล้วไม่ Update ให้ใช้ `Ctrl+F5` เพื่อรีเซ็ต Cookies
- ลองโยน Path จากคำสั่ง `{% url %}` เข้าเป็น Argument?
