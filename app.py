# /// script
# dependencies = ["nanodjango"]
# ///

from nanodjango import Django
from django.shortcuts import render
from django.db import models
# from django.contrib.auth.models import User 

app = Django()

class Comment(models.Model):
    '''
    Comments model
    '''
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # add the user
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE) 

    
@app.route('/comments')
def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        # add it to the database
        Comment.objects.create(text=comment)


    comments = Comment.objects.order_by('-created_at').all()
    context = {'comments': comments}
    return render(request, 'index.html', context)


if __name__ == "__main__":
    app.run()