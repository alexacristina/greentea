 $(function() {

  // $('#task_container ')
  $('#task_container ').empty()
  .css('visibility', 'visible')
  .stop(true,true)
  .append( $('#task1').html() );

  $('#solution_container ').empty()
  .css('visibility', 'visible')
  .stop(true,true)
  .append( $('#solution1').html() );


//compute_puncte
  var widthRect = [200, 80, 70, 180, 60, 180, 170, 100, 160, 45];
  var heightRect = [80, 80, 70, 80, 100, 40, 90, 80, 80, 90];


  l1_text = ["6cm", "6cm", "5cm", "36cm", "68cm", "12cm", "16cm", "26cm", "15cm", "18cm"];
  l2_text = ["20cm", "6cm", "5cm", "95cm", "39cm", "31cm", "83cm", "29cm", "30cm", "8cm"];
  var l1_x = [210, 90, 85, 200, 80, 195, 180, 115, 175, 55];
  var l1_y = [50, 50, 50, 50, 50, 30, 55, 50, 50, 55];
  var l2_x = [80, 20, 15, 70, 0, 70, 65, 30, 55, 0];
  var l2_y = [105, 105, 100, 110, 125, 65, 120, 110, 105, 115];
  var solution_1 = ["Aria = 120cm<sup>2</sup>", "Aria = 50cm<sup>2</sup>", "Aria = 25cm<sup>2</sup>",
  "Aria = 3420cm<sup>2</sup>", "Aria = 2682cm<sup>2</sup>", "Aria = 372cm<sup>2</sup>", "Aria = 1238cm<sup>2</sup>",
   "Aria = 754cm<sup>2</sup>", "Aria = 450cm<sup>2</sup>", "Aria = 124cm<sup>2</sup>"];
  var rasp = [];
  var rasp_corect = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0];
  var puncte=0;

  var i = 0;

  document.getElementById("latura1").innerHTML = l1_text[i];
  document.getElementById("latura2").innerHTML = l2_text[i];
  document.getElementById("sol").innerHTML = solution_1[i];
  $("#patratel").attr("width", widthRect[i]);
  $("#patratel").attr("height", heightRect[i]);

  $("#latura1").attr("x", l1_x[i]);
  $("#latura1").attr("y", l1_y[i]);
  $("#latura2").attr("x", l2_x[i]);
  $("#latura2").attr("y", l2_y[i]);


  // document.getElementById("sol").innerHTML = rasp;
  // document.getElementById("sol").innerHTML = rasp;

  $(".answer_btn_da").click(function(){
   rasp.push(1)
   i++;
   document.getElementById("latura1").innerHTML = l1_text[i];
   document.getElementById("latura2").innerHTML = l2_text[i];
  document.getElementById("sol").innerHTML = solution_1[i];


  $("#patratel").attr("width", widthRect[i]);
  $("#patratel").attr("height", heightRect[i]);
  $("#latura1").attr("x", l1_x[i]);
  $("#latura1").attr("y", l1_y[i]);
  $("#latura2").attr("x", l2_x[i]);
  $("#latura2").attr("y", l2_y[i]);

if (rasp_corect[i-1]==1) {
  puncte++;
  document.getElementById("puncte").innerHTML ="Ai acumulat "+ puncte + " puncte" ;
}


});

  $(".answer_btn_nu").click(function(){

    rasp.push(0)
    i++;
    document.getElementById("latura1").innerHTML = l1_text[i];
    document.getElementById("latura2").innerHTML = l2_text[i];
  document.getElementById("sol").innerHTML = solution_1[i];


  $("#patratel").attr("width", widthRect[i]);
  $("#patratel").attr("height", heightRect[i]);
  $("#latura1").attr("x", l1_x[i]);
  $("#latura1").attr("y", l1_y[i]);
  $("#latura2").attr("x", l2_x[i]);
  $("#latura2").attr("y", l2_y[i]);
if (rasp_corect[i-1]==0) {
  puncte++;
   document.getElementById("puncte").innerHTML ="Ai acumulat "+ puncte + " puncte" ;
}

});

  // if(i>4){

  //   for(k=0; k<=nr_rasp; k++){
  //     document.getElementById("puncte").innerHTML =  rasp[k] + "Ai acumulat "+ puncte + " puncte" + rasp_corect[k] ;
  //     if(rasp[k]==rasp_corect[k])
  //       puncte++;
  //   };
  //   document.getElementById("puncte").innerHTML =  "Ai acumulat "+ puncte + " puncte";
  // };

});