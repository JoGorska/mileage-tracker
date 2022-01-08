from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = ((0, "Draft"), (1, "Published"))

# CATEGORY describes the type of incident that has occured

CATEGORY_CHOICES = [

    ('accident', 'accident'),
    ('blocked', 'road blocked'),
    ('flood', 'flood'),
    ('queueing', 'queueing traffic'),
    ('roadworks', 'roadworks'),
    ('slow', 'slow'),

]

# list of counties form
# https://github.com/andreafalzetti/uk-counties-list/edit/master/uk-counties/uk-counties-list.csv
COUNTY_CHOICES = [
    ('aberdeen city', 'Aberdeen City'),
    ('aberdeenshire', 'Aberdeenshire'),
    ('anglesey', 'Anglesey'),
    ('angus', 'Angus'),
    ('antrim', 'Antrim'),
    ('argyll and bute', 'Argyll and Bute'),
    ('armagh', 'Armagh'),
    ('breconshire', 'Breconshire'),
    ('bedfordshire', 'Bedfordshire'),
    ('buckinghamshire', 'Buckinghamshire'),
    ('caernarvonshire', 'Caernarvonshire'),
    ('cambridgeshire', 'Cambridgeshire'),
    ('cardiganshire', 'Cardiganshire'),
    ('carmarthenshire', 'Carmarthenshire'),
    ('cheshire', 'Cheshire'),
    ('city of edinburgh', 'City of Edinburgh'),
    ('clackmannanshire', 'Clackmannanshire'),
    ('cleveland', 'Cleveland'),
    ('cornwall', 'Cornwall'),
    ('cumbria', 'Cumbria'),
    ('denbighshire', 'Denbighshire'),
    ('derbyshire', 'Derbyshire'),
    ('derry and londonderry', 'Derry and Londonderry'),
    ('devon', 'Devon'),
    ('dorset', 'Dorset'),
    ('down', 'Down'),
    ('dumfries and galloway', 'Dumfries and Galloway'),
    ('dundee city', 'Dundee City'),
    ('durham', 'Durham'),
    ('east ayrshire', 'East Ayrshire'),
    ('east dunbartonshire', 'East Dunbartonshire'),
    ('east lothian', 'East Lothian'),
    ('east renfrewshire', 'East Renfrewshire'),
    ('east sussex', 'East Sussex'),
    ('eilean siar', 'Eilean Siar'),
    ('essex', 'Essex'),
    ('falkirk', 'Falkirk'),
    ('fermanagh', 'Fermanagh'),
    ('fife', 'Fife'),
    ('flintshire', 'Flintshire'),
    ('glamorgan', 'Glamorgan'),
    ('glasgow city', 'Glasgow City'),
    ('gloucestershire', 'Gloucestershire'),
    ('greater london', 'Greater London'),
    ('greater manchester', 'Greater Manchester'),
    ('hampshire', 'Hampshire'),
    ('hertfordshire', 'Hertfordshire'),
    ('highland', 'Highland'),
    ('inverclyde', 'Inverclyde'),
    ('kent', 'Kent'),
    ('lancashire', 'Lancashire'),
    ('leicestershire', 'Leicestershire'),
    ('lincolnshire', 'Lincolnshire'),
    ('merionethshire', 'Merionethshire'),
    ('merseyside', 'Merseyside'),
    ('midlothian', 'Midlothian'),
    ('monmouthshire', 'Monmouthshire'),
    ('montgomeryshire', 'Montgomeryshire'),
    ('moray', 'Moray'),
    ('norfolk', 'Norfolk'),
    ('north ayrshire', 'North Ayrshire'),
    ('north lanarkshire', 'North Lanarkshire'),
    ('north yorkshire', 'North Yorkshire'),
    ('northamptonshire', 'Northamptonshire'),
    ('northumberland', 'Northumberland'),
    ('nottinghamshire', 'Nottinghamshire'),
    ('orkney islands', 'Orkney Islands'),
    ('oxfordshire', 'Oxfordshire'),
    ('pembrokeshire', 'Pembrokeshire'),
    ('perth and kinross', 'Perth and Kinross'),
    ('radnorshire', 'Radnorshire'),
    ('renfrewshire', 'Renfrewshire'),
    ('scottish borders', 'Scottish Borders'),
    ('shetland islands', 'Shetland Islands'),
    ('shropshire', 'Shropshire'),
    ('somerset', 'Somerset'),
    ('south ayrshire', 'South Ayrshire'),
    ('south lanarkshire', 'South Lanarkshire'),
    ('south yorkshire', 'South Yorkshire'),
    ('staffordshire', 'Staffordshire'),
    ('stirling', 'Stirling'),
    ('suffolk', 'Suffolk'),
    ('surrey', 'Surrey'),
    ('tyne and wear', 'Tyne and Wear'),
    ('tyrone', 'Tyrone'),
    ('warwickshire', 'Warwickshire'),
    ('west berkshire', 'West Berkshire'),
    ('west dunbartonshire', 'West Dunbartonshire'),
    ('west lothian', 'West Lothian'),
    ('west midlands', 'West Midlands'),
    ('west sussex', 'West Sussex'),
    ('west yorkshire', 'West Yorkshire'),
    ('wiltshire', 'Wiltshire'),
    ('worcestershire', 'Worcestershire'),
]


class TrafficMessage(models.Model):
    area = models.CharField(max_length=200, unique=False)
    county = models.CharField(max_length=200, choices=COUNTY_CHOICES, default='northamptonshire')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="traffic_messages")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='queueing traffic')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    thanks = models.ManyToManyField(User, related_name='thanks', blank=True)
    cleared = models.ManyToManyField(User, related_name='cleared', blank=True)

    # the newest traffic messages will show as first one on the list
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Reported {self.category} in the area {self.area} in {self.county}"

    def number_of_thanks(self):
        return self.thanks.count()

    def number_of_cleared(self):
        return self.cleared.count()
