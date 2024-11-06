# /// script
# dependencies = ["nanodjango"]
# ///

from nanodjango import Django
from django.shortcuts import render

app = Django()


@app.route('/comments')
def comments(request):
    return render(request, 'index.html')


if __name__ == "__main__":
    app.run()