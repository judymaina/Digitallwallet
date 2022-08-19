from django.contrib import admin
# Register your models here.
from .models import Account, Card, Customer,Currency, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'age')
    search_fields = ('first_name','last_name',)
admin. site.register(Customer, CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
     list_display = ('account_type','account_balance', 'wallet')
     search_fields = ('account_type','wallet',)
admin. site.register(Account, AccountAdmin)

class CardAdmin(admin.ModelAdmin):
     list_display = ('expiry_date',)
     search_fields = (' date_of_issue ','expiry_date',)
admin. site.register(Card, CardAdmin)

class ReceiptAdmin(admin.ModelAdmin):
     list_display = ('receipt_number', 'transaction')
     search_fields = ('transaction','receipt_number',)
admin. site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
     list_display = ('wallet','issuer')
     search_fields = ('guaranter',' issuer',)
admin. site.register(Loan, LoanAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
     list_display = ('wallet','issuer','currency')
     search_fields = ('date_of_issue','currency',)
admin. site.register(ThirdParty, ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
     list_display = ('title',)
     search_fields = ('title',' message',)
admin. site.register(Notification, NotificationAdmin)

class WalletAdmin(admin.ModelAdmin):
     list_display = ('customer','history','status')
     search_fields = (' amount ', ' balance',)
admin. site.register(Wallet, WalletAdmin)

class RewardAdmin(admin.ModelAdmin):
     list_display = ('points',)
     search_fields = ('transaction',' recipient',)
admin. site.register(Reward, RewardAdmin)


class CurrencyAdmin(admin.ModelAdmin):
     list_display = ('country','symbol')
     search_fields = ('transaction',' recipient',)
admin. site.register(Currency, CurrencyAdmin)



# admin.site.register(Account)
# admin.site.register(Wallet)
# admin.site.register(Transaction)
# admin.site.register(Currency)
# admin.site.register(Card)
# admin.site.register(ThirdParty)
# admin.site.register(Notification)
# admin.site.register(Receipt)
# admin.site.register(Loan)
# admin.site.register(Reward)




