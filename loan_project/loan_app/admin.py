from django.contrib.auth.decorators import user_passes_test
from django.contrib import admin
from .models import LoanAccount

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def approve_loan(request, loan_id):
    loan = get_object_or_404(LoanAccount, id=loan_id)
    loan.status = "Approved"
    loan.save()
    return redirect('pending')

@user_passes_test(is_admin)
def reject_loan(request, loan_id):
    loan = get_object_or_404(LoanAccount, id=loan_id)
    loan.status = "Rejected"
    loan.save()
    return redirect('pending')

class LoanAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'loan_type', 'amount', 'interest_rate', 'status']
    actions = ['approve_selected_loans', 'reject_selected_loans']

    def approve_selected_loans(self, request, queryset):
        # Update the status of selected loans to 'Approved'
        updated = queryset.update(status='Approved')
        self.message_user(request, f'{updated} loan(s) approved.')

    def reject_selected_loans(self, request, queryset):
        # Update the status of selected loans to 'Rejected'
        updated = queryset.update(status='Rejected')
        self.message_user(request, f'{updated} loan(s) rejected.')

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser or obj.user == request.user  # Users can see only their own data

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can modify

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can delete

    def has_add_permission(self, request):
        return True  # Allow users to add their own loans

admin.site.register(LoanAccount, LoanAdmin)
