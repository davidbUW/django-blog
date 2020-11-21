from django.contrib import admin
from blogging.models import Post, Category

# and a new admin registration
# admin.site.register(Post)
# admin.site.register(Category)


class MembershipInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    # Fill me
    inlines = [
        MembershipInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    # Fill me
    inlines = [
        MembershipInline,
    ]
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
