# /// script
# dependencies = ["nanodjango"]
# ///

from nanodjango import Django

app = Django()


@app.route('/comments')
def comments(request):
    return '<h1>Comments</h1>'
if __name__ == "__main__":
    app.run()