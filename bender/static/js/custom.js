function press(){
  var message = $('#chat-message');
  var li_ini = "<li class=\"left clearfix\">";
  var span_ini = "<span class=\"chat-img pull-left\">";
  var img = "<img src=\"./static/img/visitante.jpg\" alt=\"User Avatar\" class=\"img-circle\" />";
  //Cierra span
  var div1 = "<div class=\"chat-body clearfix\">";
  var div2 = "<div class=\"header\">";
  var strong = "<strong class=\"primary-font\">Visitante</strong>";
  //cierra div

  $('#message-box').submit(function (e) {
      e.preventDefault();
      if(!message.val() == ""){
         
          var mensaje = li_ini + span_ini + img + "</span>" + div1 +div2 +
          strong + "</div>" +"<p>" + message.val() +"</p>" + "</div> </li> <br>"

          $("#chat").append(mensaje);
          requestToChatbot(message.val());
          message.val('');
      }
  });
}


function requestToChatbot(texto){
  var request = new XMLHttpRequest();
  //var url = '/api/'+texto; //Esta es para cuando se debe ejecutar en teléfonos o tablets
  var url = 'http://127.0.0.1:8000/api/'+texto; //Esta es para ejecutar en la pc de servidor

  request.open('GET', url, true);
  request.setRequestHeader("Content-Type", "application/json");
  request.onreadystatechange = function() {
   
    if (this.readyState == 4 && this.status == 200) {
      var response = this.responseText;
      var objetoResponse = JSON.parse(response); 
      responseBot(objetoResponse.answer_text);       
    }
};
  
  request.send(); 
}


function responseBot(msg){

  var li_ini = "<li class=\"left clearfix\">";
  var span_ini = "<span class=\"chat-img pull-left\">";
  var img = "<img src=\"./static/img/botbender.jpg\" alt=\"User Avatar\" class=\"img-circle\" />";
  //Cierra span
  var div1 = "<div class=\"chat-body clearfix\">";
  var div2 = "<div class=\"header\">";
  var strong = "<strong class=\"primary-font\">Bot Bender</strong>";
  //cierra div
       
  var bot_respuesta = li_ini + span_ini + img + "</span>" + div1 +div2 +
  strong + "</div>" +"<p>" + msg +"</p>" + "</div> </li>  <br>"

  $("#chat").append(bot_respuesta);


};
