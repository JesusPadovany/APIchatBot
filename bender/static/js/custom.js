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
      var messagesContainer = $('.messages');

      messagesContainer.append([
          '<li class="other">',
          objetoResponse.answer_text,
          '</li>'
      ].join(''));    }
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

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

//SDFSDF

var element = $('.floating-chat');
var myStorage = localStorage;

if (!myStorage.getItem('chatID')) {
    myStorage.setItem('chatID', createUUID());
}

setTimeout(function() {
    element.addClass('enter');
}, 1000);

element.click(openElement);

function openElement() {
    var messages = element.find('.messages');
    var textInput = element.find('.text-box');
    element.find('>i').hide();
    element.addClass('expand');
    element.find('.chat').addClass('enter');
    var strLength = textInput.val().length * 2;
    textInput.keydown(onMetaAndEnter).prop("disabled", false).focus();
    element.off('click', openElement);
    element.find('.header button').click(closeElement);
    element.find('#sendMessage').click(sendNewMessage);
    messages.scrollTop(messages.prop("scrollHeight"));
}

function closeElement() {
    element.find('.chat').removeClass('enter').hide();
    element.find('>i').show();
    element.removeClass('expand');
    element.find('.header button').off('click', closeElement);
    element.find('#sendMessage').off('click', sendNewMessage);
    element.find('.text-box').off('keydown', onMetaAndEnter).prop("disabled", true).blur();
    setTimeout(function() {
        element.find('.chat').removeClass('enter').show()
        element.click(openElement);
    }, 500);
}

function createUUID() {
    // http://www.ietf.org/rfc/rfc4122.txt
    var s = [];
    var hexDigits = "0123456789abcdef";
    for (var i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";

    var uuid = s.join("");
    return uuid;
}

function sendNewMessage() {
    var userInput = $('.text-box');
    var newMessage = userInput.html().replace(/\<div\>|\<br.*?\>/ig, '\n').replace(/\<\/div\>/g, '').trim().replace(/\n/g, '<br>');
    
    if (!newMessage) return;

    var messagesContainer = $('.messages');

    messagesContainer.append([
        '<li class="self">',
        newMessage,
        '</li>'
    ].join(''));

    // clean out old message
    userInput.html('');
    // focus on input
    userInput.focus();

    messagesContainer.finish().animate({
        scrollTop: messagesContainer.prop("scrollHeight")
    }, 250);
    requestToChatbot(newMessage);
}

function sendNewMessageBot(msg) {
  var newMessage = requestToChatbot(msg);

  console.log("newMssage:")
  console.log(newMessage);
  if (!newMessage) return;

  var messagesContainer = $('.messages');

  messagesContainer.append([
      '<li class="other">',
      newMessage,
      '</li>'
  ].join(''));

  // clean out old message
  userInput.html('');
  // focus on input
  userInput.focus();

  messagesContainer.finish().animate({
      scrollTop: messagesContainer.prop("scrollHeight")
  }, 250);
}

function onMetaAndEnter(event) {
    if ((event.metaKey || event.ctrlKey) && event.keyCode == 13) {
        sendNewMessage();
    }
}

