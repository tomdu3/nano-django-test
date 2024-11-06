# /// script
# dependencies = ["nanodjango"]
# ///

from nanodjango import Django
from django.shortcuts import render
from django.db import models

app = Django()

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    
@app.route('/comments')
def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        # add it to the database
        print(comment)
    return render(request, 'index.html')


if __name__ == "__main__":
    app.run()