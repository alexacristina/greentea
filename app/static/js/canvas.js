var svg_array = ["ad", "ae", "af", "al", "ar" ,"au", "bd", "ba", "bi", "bm", "bz" ,"bt", "bv", "mt", "mh", "md", "gq", "gp",
 "gg","dz", "dm", "dk", "cr", "cc"];

var aria = 0;
$(function() {
  (function init() {
    var stage = new createjs.Stage("demoCanvas");
    var position = 0;
    for (var i = 0; i < 6; i++) {
      for (var j = 0; j < 4; j++) {
        var svg_bitmap = new createjs.Bitmap("/static/flags/1x1/" + svg_array[position++] + ".svg");
        var container = new createjs.Container();
        container.x = i * 100;
        container.y = j * 100;
        svg_bitmap.alpha = 0.01;
        svg_bitmap.hidden = true;
        var rectangle = new createjs.Shape();
        rectangle.graphics.drawRect(1, 1, 99, 99);
        $("#counter-value").html("Aria acoperita: "+ aria + " m" + "<sup>2</sup>");
        svg_bitmap.addEventListener("click", function(event) {
          if(event.target.hidden) {
            event.target.alpha = 1;
            event.target.hidden = false;
            aria++
            $("#counter-value").html("Aria acoperita: "+ aria + " m" + "<sup>2</sup>");
          } else {
            event.target.alpha = 0.01;
            event.target.hidden = true;
            aria--
            $("#counter-value").html("Aria acoperita: "+ aria + " m" + "<sup>2</sup>");
          }
          stage.update();
        });
        svg_bitmap.scaleX = 0.2;
        svg_bitmap.scaleY = 0.2;
        container.addChild(svg_bitmap, rectangle);
        stage.addChild(container);
          stage.update();
      }
    }
    stage.update();
  })();
});

// $(function() {
//   (function init() {
//     for (var i = 0; i < 3; i++) {
//       var img = new Image();
//       console.log(img);
//       img.src = "/static/flags/1x1/md.svg";
//       $(img).load(function(){
//           drawBitmap(i);
//       });

//       function drawBitmap() {
//         var stage = new createjs.Stage("demoCanvas");
//         var bitmap = new createjs.Bitmap(img);
//         var container = new createjs.Container();
//         debugger
//         bitmap.scaleX = 0.2;
//         bitmap.scaleY = 0.2;
//         container.addChild(bitmap);
//         console.log(container);
//         stage.addChild(container);
//         stage.update();
//       }
//     }

//   })();
// })


// $(function() {
//   (function init() {
//     var stage = new createjs.Stage("demoCanvas");
//     var position = 0;
//     for (var i = 0; i < 6; i++) {
//       for (var j = 0; j < 4; j++) {
//         var img = new Image(99, 99);
//         var src = "/static/flags/1x1/" + svg_array[position++] + ".svg";
//         img.onload = function () {
//           var svg_bitmap = new createjs.Bitmap(src);
//           var container = new createjs.Container();
//           container.x = i * 100;
//           container.y = j * 100;
//           if (i == 0 && j == 0) {
//             svg_bitmap.alpha = 1;
//             svg_bitmap.hidden = true;
//             stage.update();
//           } else {
//             svg_bitmap.hidden = false;
//             svg_bitmap.alpha = 1;
//           }
//           var rectangle = new createjs.Shape();
//           rectangle.graphics.drawRect(1, 1, 99, 99);
//           svg_bitmap.addEventListener("click", function(event) {
//             if(event.target.hidden) {
//               event.target.alpha = 1;
//               event.target.hidden = false;
//             } else {
//               event.target.alpha = 0.01;
//               event.target.hidden = true;
//             }
//             stage.update();
//           });
//           svg_bitmap.scaleX = 0.2;
//           svg_bitmap.scaleY = 0.2;
//           container.addChild(svg_bitmap, rectangle);
//           stage.addChild(container);
//           stage.update();
//         }
//         img.src = src;
//       }
//     }
//     stage.update();
//   })();
// });