from datetime import datetime

from nanodjango import Django
from ninja import NinjaAPI

from .models import Comment


class CommentSchema(app.ninja.Schema):
    id: int
    text: str
    created_at: datetime


app = Django()
api = NinjaAPI()


@api.get("/comments/", response=list[CommentSchema])
def api_comments(request):
    return Comment.objects.all().order_by("-created_at")
