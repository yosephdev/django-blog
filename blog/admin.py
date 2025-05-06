from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ("author", "body", "approved", "created_on")
    readonly_fields = ("author", "created_on")
    ordering = ("-created_on",)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    Adds inline comments editing.
    """

    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "body", "approved", "created_on")
    list_filter = ("approved", "created_on")
    search_fields = ("body", "author__username", "post__title")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} comments approved.")
    approve_comments.short_description = "Approve selected comments"
