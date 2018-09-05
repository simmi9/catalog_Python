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
   <header class="header"> Header</header>
   <div class"sidebar"> 
    <div class"sidebar-wrapper"> </div>
   </div>
   <!--Main Container>
  <main class="main-container">
   <section class="main-highlight">
    <div class="highlight-carousel slider-carousel">
     <div class="owl-carousel owl-loaded owl-drag" id="postCarousel">
      <div class="owl-stage-outer">
       <div class="owl-stage" style="transform:
       translate3d(-1913px, 0px, 0px); transition:all 0s ease 0s; width: 7655px;">
        <div class="owl-tem cloned" style="width:936.8px; margin-right: 20px;"> </div>
        <div class="owl-tem cloned" style="width:936.8px; margin-right: 20px;"> </div>
        <div class="owl-tem active" style="width:936.8px; margin-right: 20px;"> </div>
         <div class="item">
          <article class="post-box" style="background-image:url();">
           <div class="post-overlay"> </div>
           <a href="#" class="post-overlayLink"></a>
          </article>
         </div>
        </div>
        <div class="owl-item" style="width: 936.8px; margin-right: 20px;"></div>
         <div class="item"></div>
        </div>
        <div class="owl-item" style="width: 936.8px; margin-right: 20px;"></div>
         <div class="item"></div>
        </div>
        <div class="owl-item" style="width: 936.8px; margin-right: 20px;"></div>
         <div class="item"></div>
        </div>
        <div class="owl-item cloned" style="width: 936.8px; margin-right: 20px;"></div>
         <div class="item"></div>
        </div>
        <div class="owl-item cloned" style="width: 936.8px; margin-right: 20px;"></div>
         <div class="item"></div>
         ::after
        </div>
       </div>
       <div class="owl-nav"></div>
        <button type="button" role="presentation" class="owl-prev">
        </button>
        <button type="button" role="presentation" class="owl-next">
        </button> 
        </div>
        <div class="owl-dots">
         <button role="button" class="owl-dot active">></button>
         <button role="button" class="owl-dot"></button>
         <button role="button" class="owl-dot"></button>
         <button role="button" class="owl-dot"></button>
        </div>
       </div>
      </div>
     </section>
     <section class="main-content"> </selection>
      <div class="main-content-wrapper"></div>
     </section>
    </main>
    <!-- register -->
    <div class="m-modal-box" id="registerModal"></div>
     <div class="m-modal-overlay"></div>
     <div class="m-modal-content small"> </div>
    </div>
    
    <div class="m-modal-box" id="loginModal"></div>
     <div class="m-modal-overlay"></div>
     <div class="m-modal-content small"> </div>
    </div>

    <div class="m-modal-box" id="newsletterModal"></div>
     <div class="m-modal-overlay"></div>
     <div class="m-modal-content small"> </div>
    </div>
    <div class="overlay"> </div>
  

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

 <script src="plugins/zebra-tooltip/zebra_tooltips.min.js"></script>
    <script src="plugins/owl-carousel/owl.carousel.min.js"></script>
    <script type="text/javascript"></script>
  </body>
</html>
</iframe>
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


