from django.db import models
from django.contrib.auth import User
from cloudinary.models import CloudinaryField

STATUS_CHOICES = ((0, "Draft"), (1, "Published"))

# CATEGORY describes the type of incident that has occured

CATEGORY_CHOICES = [

    ('a', 'accident'),
    ('b', 'road blocked'),
    ('f', 'flood'),
    ('q', 'queueing traffic'),
    ('r', 'roadworks'),
    ('s', 'slow'),

]

# list of counties form
# https://github.com/andreafalzetti/uk-counties-list/edit/master/uk-counties/uk-counties-list.csv
COUNTY_CHOICES = [
    ('bedfordshire', 'Bedfordshire'),
    ('buckinghamshire', 'Buckinghamshire'),
    ('cambridgeshire', 'Cambridgeshire'),
    ('cheshire', 'Cheshire'),
    ('cleveland', 'Cleveland'),
    ('cornwall', 'Cornwall'),
    ('cumbria', 'Cumbria'),
    ('derbyshire', 'Derbyshire'),
    ('devon', 'Devon'),
    ('dorset', 'Dorset'),
    ('durham', 'Durham'),
    ('east sussex', 'East Sussex'),
    ('essex', 'Essex'),
    ('gloucestershire', 'Gloucestershire'),
    ('greater london', 'Greater London'),
    ('greater manchester', 'Greater Manchester'),
    ('hampshire', 'Hampshire'),
    ('hertfordshire', 'Hertfordshire'),
    ('kent', 'Kent'),
    ('lancashire', 'Lancashire'),
    ('leicestershire', 'Leicestershire'),
    ('lincolnshire', 'Lincolnshire'),
    ('merseyside', 'Merseyside'),
    ('norfolk', 'Norfolk'),
    ('north yorkshire', 'North Yorkshire'),
    ('northamptonshire', 'Northamptonshire'),
    ('northumberland', 'Northumberland'),
    ('nottinghamshire', 'Nottinghamshire'),
    ('oxfordshire', 'Oxfordshire'),
    ('shropshire', 'Shropshire'),
    ('somerset', 'Somerset'),
    ('south yorkshire', 'South Yorkshire'),
    ('staffordshire', 'Staffordshire'),
    ('suffolk', 'Suffolk'),
    ('surrey', 'Surrey'),
    ('tyne and wear', 'Tyne and Wear'),
    ('warwickshire', 'Warwickshire'),
    ('west berkshire', 'West Berkshire'),
    ('west midlands', 'West Midlands'),
    ('west sussex', 'West Sussex'),
    ('west yorkshire', 'West Yorkshire'),
    ('wiltshire', 'Wiltshire'),
    ('worcestershire', 'Worcestershire'),
    ('flintshire', 'Flintshire'),
    ('glamorgan', 'Glamorgan'),
    ('merionethshire', 'Merionethshire'),
    ('monmouthshire', 'Monmouthshire'),
    ('montgomeryshire', 'Montgomeryshire'),
    ('pembrokeshire', 'Pembrokeshire'),
    ('radnorshire', 'Radnorshire'),
    ('anglesey', 'Anglesey'),
    ('breconshire', 'Breconshire'),
    ('caernarvonshire', 'Caernarvonshire'),
    ('cardiganshire', 'Cardiganshire'),
    ('carmarthenshire', 'Carmarthenshire'),
    ('denbighshire', 'Denbighshire'),
    ('aberdeen city', 'Aberdeen City'),
    ('aberdeenshire', 'Aberdeenshire'),
    ('angus', 'Angus'),
    ('argyll and bute', 'Argyll and Bute'),
    ('city of edinburgh', 'City of Edinburgh'),
    ('clackmannanshire', 'Clackmannanshire'),
    ('dumfries and galloway', 'Dumfries and Galloway'),
    ('dundee city', 'Dundee City'),
    ('east ayrshire', 'East Ayrshire'),
    ('east dunbartonshire', 'East Dunbartonshire'),
    ('east lothian', 'East Lothian'),
    ('east renfrewshire', 'East Renfrewshire'),
    ('eilean siar', 'Eilean Siar'),
    ('falkirk', 'Falkirk'),
    ('fife', 'Fife'),
    ('glasgow city', 'Glasgow City'),
    ('highland', 'Highland'),
    ('inverclyde', 'Inverclyde'),
    ('midlothian', 'Midlothian'),
    ('moray', 'Moray'),
    ('north ayrshire', 'North Ayrshire'),
    ('north lanarkshire', 'North Lanarkshire'),
    ('orkney islands', 'Orkney Islands'),
    ('perth and kinross', 'Perth and Kinross'),
    ('renfrewshire', 'Renfrewshire'),
    ('scottish borders', 'Scottish Borders'),
    ('shetland islands', 'Shetland Islands'),
    ('south ayrshire', 'South Ayrshire'),
    ('south lanarkshire', 'South Lanarkshire'),
    ('stirling', 'Stirling'),
    ('west dunbartonshire', 'West Dunbartonshire'),
    ('west lothian', 'West Lothian'),
    ('antrim', 'Antrim'),
    ('armagh', 'Armagh'),
    ('down', 'Down'),
    ('fermanagh', 'Fermanagh'),
    ('derry and londonderry', 'Derry and Londonderry'),
    ('tyrone', 'Tyrone')
]


class TrafficMessage(models.Model):
    area = models.CharField(max_length=200, unique=False)
    # default = user's county, but can be changed
    county = models.CharField(max_length=200, choices=COUNTY_CHOICES, default='Northamptonshire')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="traffic_messages")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='queueing traffic')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    thanks = models.ManyToManyField(User, related_name='thanks', blank=True)
    cleared = thanks = models.ManyToManyField(User, related_name='cleared', blank=True)

