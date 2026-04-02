from django.contrib import admin
from .models import Company,Job,Application,ApplicantProfile, RecruiterProfile,User,Skill 

class JobInline(admin.TabularInline):
    model = Job
    extra = 1

class ApplicantProfileInline(admin.TabularInline):
    model = ApplicantProfile
    extra = 1 

class RecruiterProfileInline(admin.TabularInline):
    model = RecruiterProfile 
    extra = 1

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter  = ('name',)
    search_fields = ('name',)
    inlines = [JobInline]

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'salary_min', 'salary_max', 'posted_at')
    list_filter = ('company', 'posted_at')
    search_fields = ('title', 'company__name')

@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ('company','experience')

@admin.register(ApplicantProfile)
class ApplicantProfileAdmin(admin.ModelAdmin):
    list_display = ('resume',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name','username', 'email', 'role')
    search_fields = ('username',)
    inlines = [ApplicantProfileInline,RecruiterProfileInline]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'applicant', 'cover_letter', 'status', 'applied_at')
    list_filter = ('job','status')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name')
