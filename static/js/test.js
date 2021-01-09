$(document).ready(function(){
  // $("#myInput").on("keyup", function() {
  //   var value = $(this).val().toLowerCase();
  //   $(".room_post").filter(function() {
  //     $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
  //   });
  // });

  var x ="";


  $(".dropdown-item").on("click",function(){


    $(".active").on("click",function(){
      $(this).removeClass("active");
      console.log("a");
      return;
    })

    $(this).addClass("active");
    x = $(".active").text();
    return







  })





  $("#search-btn").on("click",function(){
    x+=" "  + $("#myInput").val().toLowerCase();
    alert(x);
    $(".room_post").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(x) > -1)

    });
    x="";


  })
});