#!/usr/bin/env python3


from flask import Flask, request, redirect, url_for

from catalogdb import get_posts1,get_posts2,get_posts3

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
   <div id="owl-demo">
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a9.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a10.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a11.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a5.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a6.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a7.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a8.jpg" alt="Owl Image"></div>
  <div class="item"><img src="OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\a9.jpg" alt="Owl Image"></div>
<!--</div>-->
</div>


<div class="container-fluid">

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

  #posts = "".join(POST % (date, text) for text, date in get_posts())
  #html = HTML_WRAP % posts
  #return html
  posts=""
  popular_article_posts1 = get_posts1()
  popular_article_posts2 = get_posts2()
  popular_article_posts3 = get_posts3()
  posts1 = "<br/>".join('\n Title:\t %s \t\t||\t\t views:\t %s \t  \n' % (text) for text in popular_article_posts1)
  posts2=  "<br/>".join('\n Author Name:\t %s \t\t||\t\t article:\t  %s \t  \n' % (text) for text in popular_article_posts2)
  posts3=  "<br/>".join('\n Day:\t %s \t\t||\t\t Error Percent:  %s \t  \n' % (text) for text in popular_article_posts3)
  posts+="<ul>"
  posts="<li> Most Popular Articles</li>"+ posts1 + "<br/> <li> Most Popular Authors of Popular Articles</li>" + posts2 +"<br/> <li> max error reported in percentage</li> "+ posts3+"</ul>"
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


