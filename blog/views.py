from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# DRF imports for API endpoint
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth.models import User


# Create your views here.
class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html`
    """

    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = "post_list"


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """

    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


@api_view(['POST'])
@permission_classes([AllowAny])
def auto_create_post(request):
    """
    API endpoint for auto-creating posts (e.g., from external services).

    Expects JSON payload:
      - title: (string)
      - content: (string)
      - excerpt: (string, optional)
      - status: (int, optional) - defaults to 1 (published)

    Security:
      - Requires API key in Authorization header: 'Bearer <KEY>'

    Returns:
      - 201 Created on success
      - 400 Bad Request on missing data
      - 401 Unauthorized on missing/incorrect API key
    """
    try:
        # Security: Check API key from header
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return Response({"error": "Missing Bearer token."}, status=401)
        token = auth_header.split('Bearer ')[1]
        valid_token = getattr(settings, 'DJANGO_API_KEY', None)
        if not valid_token or token != valid_token:
            return Response({"error": "Invalid API key."}, status=401)

        # Get data from request
        title = request.data.get("title")
        content = request.data.get("content")
        excerpt = request.data.get("excerpt", "")
        status = request.data.get("status", 1)  # Default to published

        if not title or not content:
            return Response({"error": "Title and content are required."}, status=400)

        # Get or create the default author
        try:
            default_author = User.objects.get(username='auto-publisher')
        except User.DoesNotExist:
            default_author = User.objects.create_user(
                username='auto-publisher',
                email='auto-publisher@example.com',
                password=User.objects.make_random_password()
            )

        # Create the post
        post = Post.objects.create(
            title=title,
            content=content,
            excerpt=excerpt,
            status=status,
            author=default_author,            
        )
        
        return Response({
            "success": True,
            "post_id": post.id,
            "slug": post.slug,
            "title": post.title,
            "status": post.status
        }, status=201)

    except Exception as e:
        return Response({
            "error": str(e),
            "detail": "An error occurred while creating the post."
        }, status=500)


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
