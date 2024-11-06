# /// script
# dependencies = ["nanodjango"]
# ///

from nanodjango import Django
from django.shortcuts import render
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


app = Django()

User = get_user_model()

class Comment(models.Model):
    '''
    Comments model
    '''
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # add the user
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class CommentSchema(app.ninja.Schema):
    id: int
    text: str
    created_at: datetime



@app.api.get('/comments/', response=list[CommentSchema])
def api_comments(request):
    return Comment.objects.all().order_by('-created_at')


@app.route('/comments')
def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = User.objects.first() 
        # add it to the database
        if comment:
            Comment.objects.create(text=comment, created_by=user) 


    comments = Comment.objects.filter(created_by=user).order_by('-created_at')
    context = {'comments': comments}
    return render(request, 'index.html', context)


if __name__ == "__main__":
    app.run()