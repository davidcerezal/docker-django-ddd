from django.contrib import admin
from .models import DemoModel
from .domain.models.bet import BetModel

admin.site.register(DemoModel)
admin.site.register(BetModel)
