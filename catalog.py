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
 <!-- Bootstrap Scripts -->
 <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
 

 <link href="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\dist\assets\owl.carousel.css" rel="stylesheet" type="text/css">
  
<link href="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\OwlCarousel2-2.3.4\OwlCarousel2-2.3.4\docs\assets\css\docs.theme.min.css" rel="stylesheet" type="text/css">
 <style>
   div img{ object-fit: cover; max-width: 100%%;}
   
   #owl-demo .item{
    background: #fff;
    padding: 30px 0px;
    margin: 5px;
    color: #FFF;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    text-align: center;
}


.owl-carousel .owl-wrapper:after {
  content: ".";
  display: block;
  clear: both;
  visibility: hidden;
  line-height: 0;
  height: 0;
}
/* display none until init */
.owl-carousel {
  display: none;
  position: relative;
  width: 100%%;
  -ms-touch-action: pan-y;
}
.owl-carousel .owl-wrapper {
  display: none;
  position: relative;
  -webkit-transform: translate3d(0px, 0px, 0px);
}
.owl-carousel .owl-wrapper-outer {
  overflow: hidden;
  position: relative;
  width: 100%%;
}
.owl-carousel .owl-wrapper-outer.autoHeight {
  -webkit-transition: height 500ms ease-in-out;
  -moz-transition: height 500ms ease-in-out;
  -ms-transition: height 500ms ease-in-out;
  -o-transition: height 500ms ease-in-out;
  transition: height 500ms ease-in-out;
}
.owl-carousel .owl-item {
  float: left;
}
.owl-controls .owl-page, .owl-controls .owl-buttons div {
  cursor: pointer;
}
.owl-controls {
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
/* mouse grab icon */
.grabbing {
  cursor: url(grabbing.png) 8 8, move;
}
/* fix */
.owl-carousel .owl-wrapper, .owl-carousel .owl-item {
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -ms-backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  -moz-transform: translate3d(0, 0, 0);
  -ms-transform: translate3d(0, 0, 0);
}


/* PRODUCTS SLIDER = */
.owl-item .item {
  margin: 0 10px;
}
.slider-items {
  position: relative;
}
.slider-items .item {
  text-align: center;
}
.owl-buttons {
  opacity: 1;
}
.product-flexslider {
  margin:5px -10px;
}


.owl-theme .owl-controls {
  margin-top: 10px;
  text-align: center;
}
.owl-pagination {
  top: -26px;
  text-align: center;
  position: absolute;
  right: 15px;
  background: #fff;
  padding-left: 10px;
}
.owl-theme .owl-controls .owl-page {
  display: inline-block;
  zoom: 1;
}
.owl-controls .owl-page, .owl-controls .owl-buttons div {
  cursor: pointer;
}
.owl-theme .owl-controls .owl-page span {
  display: block;
  width: 8px;
  height: 15px;
  margin: 5px 2px;
  filter: Alpha(Opacity=50);
}
.owl-theme .owl-controls .owl-page.active span, .owl-theme .owl-controls.clickable .owl-page:hover span {
  filter: Alpha(Opacity=100);
  opacity: 1;
}
.owl-theme .owl-controls .owl-buttons div {
  color: #FFF;
  display: inline-block;
  zoom: 1;
  margin: 5px;
  padding: 1px 0;
  font-size: 12px;
  -webkit-border-radius: 30px;
  -moz-border-radius: 30px;
  border-radius: 30px;
  background: #869791;
  filter: Alpha(Opacity=50);
  opacity: 1;
  display: none;
}
.slider-items .owl-buttons a {
  background: #fff;
  display: block;
  height: 38px;
  margin: 0px 0 0 -30px;
  position: absolute;
  top: 50%%;
  width: 38px;
  z-index: 5;
  color: #888;
  border: 1px #eaeaea solid;
}
.slider-items .owl-buttons .owl-prev a:before {
  font-family: 'FontAwesome';
  font-style: normal;
  font-weight: normal;
  speak: none;
  -webkit-font-smoothing: antialiased;
  content: "\f104";
  text-transform: none;
  font-size: 26px;
  line-height: 35px;
  padding: 6px 6px 6px 6px;
}
.slider-items .owl-buttons .owl-next a {
  top: 50%%;
  padding: 2px;
}
.slider-items .owl-buttons .owl-next a:before {
  font-family: 'FontAwesome';
  font-style: normal;
  font-weight: normal;
  speak: none;
  -webkit-font-smoothing: antialiased;
  content: "\f105";
  text-transform: none;
  font-size: 24px;
  padding: 6px 6px 6px 6px;
  line-height: 30px;
}
.slider-items .owl-buttons .owl-next {
  position: absolute;
  right: -32px;
  top: 30%%;
}
.slider-items .owl-buttons .owl-prev {
  position: absolute;
  left: -13px;
  top: 30%%;
}
.owl-carousel .col-lg-4, .owl-carousel .col-md-3, .owl-carousel .col-sm-4, .owl-carousel .col-xs-6-12{ width:100%%}

.owl-carousel .product{padding:0px!important;}

.owl-carousel .product .product_info {top:32%%!important;}

section.home-instagram.wow.fadeIn div.owl-pagination { right: 0; }
</style>
    
  </head>
  <body>
  <div class="row text-center">
  <h1 style="align:center"> Article Catalog </h1>
<div class="container-fluid text-center">

%s
</div>
</div>
  <div class="row ">
   <div id="owl-demo">
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a9.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a10.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a11.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a5.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a6.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a7.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a8.jpg" alt="Owl Image"></div>
  <div class="item"><img src="C:\Users\ashis\udacity-git-webdev\fullstack-nanodegree-vm-master\fullstack-nanodegree-vm-master\vagrant\catalog\a9.jpg" alt="Owl Image"></div>
<!--</div>-->
</div>
</div>

 <script type="text/javascript">
   $(document).ready(function() {

  var owl = $("#owl-demo");

  owl.owlCarousel({
    autoPlay : true,
    responsive: true,
    items : 6, //10 items above 1000px browser width
    itemsDesktop : [1024,4], //5 items between 1024px and 901px
    itemsDesktopSmall : [900,3], // 3 items betweem 900px and 601px
    itemsTablet: [600,2], //2 items between 600 and 0;
    itemsMobile : [320,1],
    navigation : true,
    slideSpeed : 500,
    pagination : true,
    navigation : false,
  });

});
/*
 *  jQuery OwlCarousel v1.31
 *
 *  Copyright (c) 2013 Bartosz Wojciechowski
 *  http://www.owlgraphic.com/owlcarousel/
 *
 *  Licensed under MIT
 *
 */

if ( typeof Object.create !== "function" ) {
  Object.create = function( obj ) {
    function F() {};
    F.prototype = obj;
    return new F();
  };
}
(function( $, window, document, undefined ) {

  var Carousel = {
    init :function(options, el){
      var base = this;

      base.$elem = $(el);

      // options passed via js override options passed via data attributes
      base.options = $.extend({}, $.fn.owlCarousel.options, base.$elem.data(), options);

      base.userOptions = options;
      base.loadContent();
    },

    loadContent : function(){
      var base = this;

      if (typeof base.options.beforeInit === "function") {
        base.options.beforeInit.apply(this,[base.$elem]);
      }

      if (typeof base.options.jsonPath === "string") {
        var url = base.options.jsonPath;

        function getData(data) {
          if (typeof base.options.jsonSuccess === "function") {
            base.options.jsonSuccess.apply(this,[data]);
          } else {
            var content = "";
            for(var i in data["owl"]){
              content += data["owl"][i]["item"];
            }
            base.$elem.html(content);
          }
          base.logIn();
        }
        $.getJSON(url,getData);
      } else {
        base.logIn();
      }
    },

    logIn : function(action){
      var base = this;

      base.$elem.data("owl-originalStyles", base.$elem.attr("style"))
        .data("owl-originalClasses", base.$elem.attr("class"));

      base.$elem.css({opacity: 0});
      base.orignalItems = base.options.items;
      base.checkBrowser();
      base.wrapperWidth = 0;
      base.checkVisible;
      base.setVars();
    },

    setVars : function(){
      var base = this;
      if(base.$elem.children().length === 0){return false}
      base.baseClass();
      base.eventTypes();
      base.$userItems = base.$elem.children();
      base.itemsAmount = base.$userItems.length;
      base.wrapItems();
      base.$owlItems = base.$elem.find(".owl-item");
      base.$owlWrapper = base.$elem.find(".owl-wrapper");
      base.playDirection = "next";
      base.prevItem = 0;
      base.prevArr = [0];
      base.currentItem = 0;
      base.customEvents();
      base.onStartup();
    },

    onStartup : function(){
      var base = this;
      base.updateItems();
      base.calculateAll();
      base.buildControls();
      base.updateControls();
      base.response();
      base.moveEvents();
      base.stopOnHover();
      base.owlStatus();

      if(base.options.transitionStyle !== false){
        base.transitionTypes(base.options.transitionStyle);
      }
      if(base.options.autoPlay === true){
        base.options.autoPlay = 5000;
      }
      base.play();

      base.$elem.find(".owl-wrapper").css("display","block")

      if(!base.$elem.is(":visible")){
        base.watchVisibility();
      } else {
        base.$elem.css("opacity",1);
      }
      base.onstartup = false;
      base.eachMoveUpdate();
      if (typeof base.options.afterInit === "function") {
        base.options.afterInit.apply(this,[base.$elem]);
      }
    },

    eachMoveUpdate : function(){
      var base = this;

      if(base.options.lazyLoad === true){
        base.lazyLoad();
      }
      if(base.options.autoHeight === true){
        base.autoHeight();
      }
      base.onVisibleItems();

      if (typeof base.options.afterAction === "function") {
        base.options.afterAction.apply(this,[base.$elem]);
      }
    },

    updateVars : function(){
      var base = this;
      if(typeof base.options.beforeUpdate === "function") {
        base.options.beforeUpdate.apply(this,[base.$elem]);
      }
      base.watchVisibility();
      base.updateItems();
      base.calculateAll();
      base.updatePosition();
      base.updateControls();
      base.eachMoveUpdate();
      if(typeof base.options.afterUpdate === "function") {
        base.options.afterUpdate.apply(this,[base.$elem]);
      }
    },

    reload : function(elements){
      var base = this;
      setTimeout(function(){
        base.updateVars();
      },0)
    },

    watchVisibility : function(){
      var base = this;

      if(base.$elem.is(":visible") === false){
        base.$elem.css({opacity: 0});
        clearInterval(base.autoPlayInterval);
        clearInterval(base.checkVisible);
      } else {
        return false;
      }
      base.checkVisible = setInterval(function(){
        if (base.$elem.is(":visible")) {
          base.reload();
          base.$elem.animate({opacity: 1},200);
          clearInterval(base.checkVisible);
        }
      }, 500);
    },

    wrapItems : function(){
      var base = this;
      base.$userItems.wrapAll("<div class=\"owl-wrapper\">").wrap("<div class=\"owl-item\"></div>");
      base.$elem.find(".owl-wrapper").wrap("<div class=\"owl-wrapper-outer\">");
      base.wrapperOuter = base.$elem.find(".owl-wrapper-outer");
      base.$elem.css("display","block");
    },

    baseClass : function(){
      var base = this;
      var hasBaseClass = base.$elem.hasClass(base.options.baseClass);
      var hasThemeClass = base.$elem.hasClass(base.options.theme);

      if(!hasBaseClass){
        base.$elem.addClass(base.options.baseClass);
      }

      if(!hasThemeClass){
        base.$elem.addClass(base.options.theme);
      }
    },

    updateItems : function(){
      var base = this;

      if(base.options.responsive === false){
        return false;
      }
      if(base.options.singleItem === true){
        base.options.items = base.orignalItems = 1;
        base.options.itemsCustom = false;
        base.options.itemsDesktop = false;
        base.options.itemsDesktopSmall = false;
        base.options.itemsTablet = false;
        base.options.itemsTabletSmall = false;
        base.options.itemsMobile = false;
        return false;
      }

      var width = $(base.options.responsiveBaseWidth).width();

      if(width > (base.options.itemsDesktop[0] || base.orignalItems) ){
        base.options.items = base.orignalItems;
      }

      if(typeof(base.options.itemsCustom) !== 'undefined' && base.options.itemsCustom !== false){
        //Reorder array by screen size
        base.options.itemsCustom.sort(function(a,b){return a[0]-b[0];});
        for(var i in base.options.itemsCustom){
          if(typeof(base.options.itemsCustom[i]) !== 'undefined' && base.options.itemsCustom[i][0] <= width){
            base.options.items = base.options.itemsCustom[i][1];
          }
        }
      } else {

        if(width <= base.options.itemsDesktop[0] && base.options.itemsDesktop !== false){
          base.options.items = base.options.itemsDesktop[1];
        }

        if(width <= base.options.itemsDesktopSmall[0] && base.options.itemsDesktopSmall !== false){
          base.options.items = base.options.itemsDesktopSmall[1];
        }

        if(width <= base.options.itemsTablet[0]  && base.options.itemsTablet !== false){
          base.options.items = base.options.itemsTablet[1];
        }

        if(width <= base.options.itemsTabletSmall[0]  && base.options.itemsTabletSmall !== false){
          base.options.items = base.options.itemsTabletSmall[1];
        }

        if(width <= base.options.itemsMobile[0] && base.options.itemsMobile !== false){
          base.options.items = base.options.itemsMobile[1];
        }
      }

      //if number of items is less than declared
      if(base.options.items > base.itemsAmount && base.options.itemsScaleUp === true){
        base.options.items = base.itemsAmount;
      }
    },

    response : function(){
      var base = this,
          smallDelay;
      if(base.options.responsive !== true){
        return false
      }
      var lastWindowWidth = $(window).width();

      base.resizer = function(){
        if($(window).width() !== lastWindowWidth){
          if(base.options.autoPlay !== false){
            clearInterval(base.autoPlayInterval);
          }
          clearTimeout(smallDelay);
          smallDelay = setTimeout(function(){
            lastWindowWidth = $(window).width();
            base.updateVars();
          },base.options.responsiveRefreshRate);
        }
      }
      $(window).resize(base.resizer)
    },

    updatePosition : function(){
      var base = this;
      base.jumpTo(base.currentItem);
      if(base.options.autoPlay !== false){
        base.checkAp();
      }
    },

    appendItemsSizes : function(){
      var base = this;

      var roundPages = 0;
      var lastItem = base.itemsAmount - base.options.items;

      base.$owlItems.each(function(index){
        var $this = $(this);
        $this
          .css({"width": base.itemWidth})
          .data("owl-item",Number(index));

       
        $this.data("owl-roundPages",roundPages)
      });
    },

    appendWrapperSizes : function(){
      var base = this;
      var width = 0;

      var width = base.$owlItems.length * base.itemWidth;

      base.$owlWrapper.css({
        "width": width*2,
        "left": 0
      });
      base.appendItemsSizes();
    },

    calculateAll : function(){
      var base = this;
      base.calculateWidth();
      base.appendWrapperSizes();
      base.loops();
      base.max();
    },

    calculateWidth : function(){
      var base = this;
      base.itemWidth = Math.round(base.$elem.width()/base.options.items)
    },

    max : function(){
      var base = this;
      var maximum = ((base.itemsAmount * base.itemWidth) - base.options.items * base.itemWidth) * -1;
      if(base.options.items > base.itemsAmount){
        base.maximumItem = 0;
        maximum = 0
        base.maximumPixels = 0;
      } else {
        base.maximumItem = base.itemsAmount - base.options.items;
        base.maximumPixels = maximum;
      }
      return maximum;
    },

    min : function(){
      return 0;
    },

    loops : function(){
      var base = this;

      base.positionsInArray = [0];
      base.pagesInArray = [];
      var prev = 0;
      var elWidth = 0;

      for(var i = 0; i<base.itemsAmount; i++){
        elWidth += base.itemWidth;
        base.positionsInArray.push(-elWidth);

        if(base.options.scrollPerPage === true){
          var item = $(base.$owlItems[i]);
          var roundPageNum = item.data("owl-roundPages");
          if(roundPageNum !== prev){
            base.pagesInArray[prev] = base.positionsInArray[i];
            prev = roundPageNum;
          }
        }
      }
    },

    buildControls : function(){
      var base = this;
      if(base.options.navigation === true || base.options.pagination === true){
        base.owlControls = $("<div class=\"owl-controls\"/>").toggleClass("clickable", !base.browser.isTouch).appendTo(base.$elem);
      }
      if(base.options.pagination === true){
        base.buildPagination();
      }
      if(base.options.navigation === true){
        base.buildButtons();
      }
    },

    buildButtons : function(){
      var base = this;
      var buttonsWrapper = $("<div class=\"owl-buttons\"/>")
      base.owlControls.append(buttonsWrapper);

      base.buttonPrev = $("<div/>",{
        "class" : "owl-prev",
        "html" : base.options.navigationText[0] || ""
      });

      base.buttonNext = $("<div/>",{
        "class" : "owl-next",
        "html" : base.options.navigationText[1] || ""
      });

      buttonsWrapper
        .append(base.buttonPrev)
        .append(base.buttonNext);

      buttonsWrapper.on("touchstart.owlControls mousedown.owlControls", "div[class^=\"owl\"]", function(event){
        event.preventDefault();
      })

      buttonsWrapper.on("touchend.owlControls mouseup.owlControls", "div[class^=\"owl\"]", function(event){
        event.preventDefault();
        if($(this).hasClass("owl-next")){
          base.next();
        } else{
          base.prev();
        }
      })
    },

    buildPagination : function(){
      var base = this;

      base.paginationWrapper = $("<div class=\"owl-pagination\"/>");
      base.owlControls.append(base.paginationWrapper);

      base.paginationWrapper.on("touchend.owlControls mouseup.owlControls", ".owl-page", function(event){
        event.preventDefault();
        if(Number($(this).data("owl-page")) !== base.currentItem){
          base.goTo( Number($(this).data("owl-page")), true);
        }
      });
    },

    updatePagination : function(){
      var base = this;
      if(base.options.pagination === false){
        return false;
      }

      base.paginationWrapper.html("");

      var counter = 0;
   
          var paginationButton = $("<div/>",{
            "class" : "owl-page"
          });
          var paginationButtonInner = $("<span></span>",{
            "text": base.options.paginationNumbers === true ? counter : "",
            "class": base.options.paginationNumbers === true ? "owl-numbers" : ""
          });
          paginationButton.append(paginationButtonInner);

          paginationButton.data("owl-page",lastPage === i ? lastItem : i);
          paginationButton.data("owl-roundPages",counter);

          base.paginationWrapper.append(paginationButton);
        }
      }
      base.checkPagination();
    },
    checkPagination : function(){
      var base = this;
      if(base.options.pagination === false){
        return false;
      }
      base.paginationWrapper.find(".owl-page").each(function(i,v){
        if($(this).data("owl-roundPages") === $(base.$owlItems[base.currentItem]).data("owl-roundPages") ){
          base.paginationWrapper
            .find(".owl-page")
            .removeClass("active");
          $(this).addClass("active");
        }
      });
    },

    checkNavigation : function(){
      var base = this;

      if(base.options.navigation === false){
        return false;
      }
      if(base.options.rewindNav === false){
        if(base.currentItem === 0 && base.maximumItem === 0){
          base.buttonPrev.addClass("disabled");
          base.buttonNext.addClass("disabled");
        } else if(base.currentItem === 0 && base.maximumItem !== 0){
          base.buttonPrev.addClass("disabled");
          base.buttonNext.removeClass("disabled");
        } else if (base.currentItem === base.maximumItem){
          base.buttonPrev.removeClass("disabled");
          base.buttonNext.addClass("disabled");
        } else if(base.currentItem !== 0 && base.currentItem !== base.maximumItem){
          base.buttonPrev.removeClass("disabled");
          base.buttonNext.removeClass("disabled");
        }
      }
    },

    updateControls : function(){
      var base = this;
      base.updatePagination();
      base.checkNavigation();
      if(base.owlControls){
        if(base.options.items >= base.itemsAmount){
          base.owlControls.hide();
        } else {
          base.owlControls.show();
        }
      }
    },

    destroyControls : function(){
      var base = this;
      if(base.owlControls){
        base.owlControls.remove();
      }
    },

    next : function(speed){
      var base = this;

      if(base.isTransition){
        return false;
      }

      base.currentItem += base.options.scrollPerPage === true ? base.options.items : 1;
      if(base.currentItem > base.maximumItem + (base.options.scrollPerPage == true ? (base.options.items - 1) : 0)){
        if(base.options.rewindNav === true){
          base.currentItem = 0;
          speed = "rewind";
        } else {
          base.currentItem = base.maximumItem;
          return false;
        }
      }
      base.goTo(base.currentItem,speed);
    },

    prev : function(speed){
      var base = this;

      if(base.isTransition){
        return false;
      }

      if(base.options.scrollPerPage === true && base.currentItem > 0 && base.currentItem < base.options.items){
        base.currentItem = 0
      } else {
        base.currentItem -= base.options.scrollPerPage === true ? base.options.items : 1;
      }
      if(base.currentItem < 0){
        if(base.options.rewindNav === true){
          base.currentItem = base.maximumItem;
          speed = "rewind"
        } else {
          base.currentItem =0;
          return false;
        }
      }
      base.goTo(base.currentItem,speed);
    },

    goTo : function(position,speed,drag){
      var base = this;

      if(base.isTransition){
        return false;
      }
      if(typeof base.options.beforeMove === "function") {
        base.options.beforeMove.apply(this,[base.$elem]);
      }
      if(position >= base.maximumItem){
        position = base.maximumItem;
      }
      else if( position <= 0 ){
        position = 0;
      }

      base.currentItem = base.owl.currentItem = position;
      if( base.options.transitionStyle !== false && drag !== "drag" && base.options.items === 1 && base.browser.support3d === true){
        base.swapSpeed(0)
        if(base.browser.support3d === true){
          base.transition3d(base.positionsInArray[position]);
        } else {
          base.css2slide(base.positionsInArray[position],1);
        }
        base.afterGo();
        base.singleItemTransition();

        return false;
      }
      var goToPixel = base.positionsInArray[position];

      if(base.browser.support3d === true){
        base.isCss3Finish = false;

        if(speed === true){
          base.swapSpeed("paginationSpeed");
          setTimeout(function() {
            base.isCss3Finish = true;
          }, base.options.paginationSpeed);

        } else if(speed === "rewind" ){
          base.swapSpeed(base.options.rewindSpeed);
          setTimeout(function() {
            base.isCss3Finish = true;
          }, base.options.rewindSpeed);

        } else {
          base.swapSpeed("slideSpeed");
          setTimeout(function() {
            base.isCss3Finish = true;
          }, base.options.slideSpeed);
        }
        base.transition3d(goToPixel);
      } else {
        if(speed === true){
          base.css2slide(goToPixel, base.options.paginationSpeed);
        } else if(speed === "rewind" ){
          base.css2slide(goToPixel, base.options.rewindSpeed);
        } else {
          base.css2slide(goToPixel, base.options.slideSpeed);
        }
      }
      base.afterGo();
    },

    jumpTo : function(position){
      var base = this;
      if(typeof base.options.beforeMove === "function") {
        base.options.beforeMove.apply(this,[base.$elem]);
      }
      if(position >= base.maximumItem || position === -1){
        position = base.maximumItem;
      }
      else if( position <= 0 ){
        position = 0;
      }
      base.swapSpeed(0)
      if(base.browser.support3d === true){
        base.transition3d(base.positionsInArray[position]);
      } else {
        base.css2slide(base.positionsInArray[position],1);
      }
      base.currentItem = base.owl.currentItem = position;
      base.afterGo();
    },

    afterGo : function(){
      var base = this;

      base.prevArr.push(base.currentItem);
      base.prevItem = base.owl.prevItem = base.prevArr[base.prevArr.length -2];
      base.prevArr.shift(0)

      if(base.prevItem !== base.currentItem){
        base.checkPagination();
        base.checkNavigation();
        base.eachMoveUpdate();

        if(base.options.autoPlay !== false){
          base.checkAp();
        }
      }
      if(typeof base.options.afterMove === "function" && base.prevItem !== base.currentItem) {
        base.options.afterMove.apply(this,[base.$elem]);
      }
    },

    stop : function(){
      var base = this;
      base.apStatus = "stop";
      clearInterval(base.autoPlayInterval);
    },

    checkAp : function(){
      var base = this;
      if(base.apStatus !== "stop"){
        base.play();
      }
    },

    play : function(){
      var base = this;
      base.apStatus = "play";
      if(base.options.autoPlay === false){
        return false;
      }
      clearInterval(base.autoPlayInterval);
      base.autoPlayInterval = setInterval(function(){
        base.next(true);
      },base.options.autoPlay);
    },

    swapSpeed : function(action){
      var base = this;
      if(action === "slideSpeed"){
        base.$owlWrapper.css(base.addCssSpeed(base.options.slideSpeed));
      } else if(action === "paginationSpeed" ){
        base.$owlWrapper.css(base.addCssSpeed(base.options.paginationSpeed));
      } else if(typeof action !== "string"){
        base.$owlWrapper.css(base.addCssSpeed(action));
      }
    },

    addCssSpeed : function(speed){
      var base = this;
      return {
        "-webkit-transition": "all "+ speed +"ms ease",
        "-moz-transition": "all "+ speed +"ms ease",
        "-o-transition": "all "+ speed +"ms ease",
        "transition": "all "+ speed +"ms ease"
      };
    },

    removeTransition : function(){
      return {
        "-webkit-transition": "",
        "-moz-transition": "",
        "-o-transition": "",
        "transition": ""
      };
    },

    doTranslate : function(pixels){
      return {
        "-webkit-transform": "translate3d("+pixels+"px, 0px, 0px)",
        "-moz-transform": "translate3d("+pixels+"px, 0px, 0px)",
        "-o-transform": "translate3d("+pixels+"px, 0px, 0px)",
        "-ms-transform": "translate3d("+pixels+"px, 0px, 0px)",
        "transform": "translate3d("+pixels+"px, 0px,0px)"
      };
    },

    transition3d : function(value){
      var base = this;
      base.$owlWrapper.css(base.doTranslate(value));
    },

    css2move : function(value){
      var base = this;
      base.$owlWrapper.css({"left" : value})
    },

    css2slide : function(value,speed){
      var base = this;

      base.isCssFinish = false;
      base.$owlWrapper.stop(true,true).animate({
        "left" : value
      }, {
        duration : speed || base.options.slideSpeed ,
        complete : function(){
          base.isCssFinish = true;
        }
      });
    },

    checkBrowser : function(){
      var base = this;

      //Check 3d support
      var translate3D = "translate3d(0px, 0px, 0px)",
          tempElem = document.createElement("div");

      tempElem.style.cssText= "  -moz-transform:"    + translate3D +
        "; -ms-transform:"     + translate3D +
        "; -o-transform:"      + translate3D +
        "; -webkit-transform:" + translate3D +
        "; transform:"         + translate3D;
      var regex = /translate3d\(0px, 0px, 0px\)/g,
          asSupport = tempElem.style.cssText.match(regex),
          support3d = (asSupport !== null && asSupport.length === 1);

      var isTouch = "ontouchstart" in window || navigator.msMaxTouchPoints;

      base.browser = {
        "support3d" : support3d,
        "isTouch" : isTouch
      }
    },

    moveEvents : function(){
      var base = this;
      if(base.options.mouseDrag !== false || base.options.touchDrag !== false){
        base.gestures();
        base.disabledEvents();
      }
    },

;
  };

  $.fn.owlCarousel.options = {

    items : 5,
    itemsCustom : false,
    itemsDesktop : [1199,4],
    itemsDesktopSmall : [979,3],
    itemsTablet : [768,2],
    itemsTabletSmall : false,
    itemsMobile : [479,1],
    singleItem : false,
    itemsScaleUp : false,

    slideSpeed : 200,
    paginationSpeed : 800,
    rewindSpeed : 1000,

    autoPlay : false,
    stopOnHover : false,

    navigation : false,
    navigationText : ["prev","next"],
    rewindNav : true,
    scrollPerPage : false,

    pagination : true,
    paginationNumbers : false,

    responsive : true,
    responsiveRefreshRate : 200,
    responsiveBaseWidth : window,


    baseClass : "owl-carousel",
    theme : "owl-theme",

    lazyLoad : false,
    lazyFollow : true,
    lazyEffect : "fade",

    autoHeight : false,

    jsonPath : false,
    jsonSuccess : false,

    dragBeforeAnimFinish : true,
    mouseDrag : true,
    touchDrag : true,

    addClassActive : false,
    transitionStyle : false,

    beforeUpdate : false,
    afterUpdate : false,
    beforeInit : false,
    afterInit : false,
    beforeMove : false,
    afterMove : false,
    afterAction : false,
    startDragging : false,
    afterLazyLoad: false

  };
})( jQuery, window, document );

</script>
  </body>
</html>

'''
# HTML template for an individual comment
POSTS = '''\
<ul><li> Most Popular Articles</li>%s<br/> <li> Most Popular Authors of Popular Articles</li> %s<br/> <li> max error reported in percentage</li> %s</ul>
    
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


