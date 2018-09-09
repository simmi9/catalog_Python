#!/usr/bin/env python3


from flask import Flask, request, redirect, url_for

from catalogdb import get_posts, add_post

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB Catalog in Bootstrap</title>
    <title>Bootstrap 4 Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
  <link rel="stylesheet" src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\owl-carousel/css/owl.carousel.css">
  <link rel="stylesheet" src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\owl-carousel/css/owl.theme.css">
  <script type="text/javascript" src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\owl-carousel\js\owl.carousel.js"></script>
 
 
   <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <div "owl-carousel owl-theme">
    <div class="item"><h4>1</h4></div>
    <div class="item"><h4>2</h4></div>
    <div class="item"><h4>3</h4></div>
    <div class="item"><h4>4</h4></div>
    <div class="item"><h4>5</h4></div>
    <div class="item"><h4>6</h4></div>
    <div class="item"><h4>7</h4></div>
    <div class="item"><h4>8</h4></div>
    <div class="item"><h4>9</h4></div>
    <div class="item"><h4>10</h4></div>
    <div class="item"><h4>11</h4></div>
    <div class="item"><h4>12</h4></div>
     <!--<div style="width: 936.8px; margin-right: 20px; ><img src="harrypotter.jpeg" alt="harry"> article1 img </div>
      <div style="width: 936.8px; margin-right: 20px; ><img src="psiloveu.jpg" alt="ps"> article2 img </div>  -->   
    </div>

<div class="container-fluid">

    <h1>DB Forum</h1>
     <div class="container"
    <form method=post>
      <div><textarea id="content" name="content"></textarea></div>
      <div><button id="go" type="submit">Post message</button></div>
    </form>
    </div>
    <!-- post content will go here -->
%s
</div>
 <script type="text/javascript">
  $(document).ready(function() {
 $('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
});

});
    </script>
  </body>
</html>

'''
# HTML template for an individual comment
POST = '''\
    <div class=post><em class=date>%s</em><br>%s</div>
'''
#GET Request redirection to main page

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  posts = "".join(POST % (date, text) for text, date in get_posts())
  html = HTML_WRAP % posts
  return html

#POST Request ;saving Post content to Database
@app.route('/', methods=['POST'])
def post():
  '''New post submission.'''
  message = request.form['content']
  add_post(message)
  return redirect(url_for('main'))
#Running the app server on host 8000
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)


