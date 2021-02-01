function reply_click(obj){

$.ajax({
 url:"/"+ obj.id,
 type: 'POST',
 success: function(data){
  $("#result").text(data);
          }
})

}

