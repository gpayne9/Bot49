// /static/custom.js

function submit_message(message) {
	$.post("/send_message", {message: message}, handle_response);

	function handle_response(data) {
		// append the bot repsonse to the div
		// $('.chat-container').append(`<div class="chat-message col-md-5 offset-md-7 bot-message">${data.message}</div>`)

		if(data.intent == "directions"){
			$('.chat-container').append(`<div class="chat-message col-md-5 offset-md-7 bot-message">${"Directions to " + data.message}</div>`)

			$.post("/bot_49", {message: data.message, intent: data.intent}, handle_directions);
		}
		else if(data.intent == "pictures"){
			$('.chat-container').append(`<div class="chat-message col-md-5 offset-md-7 bot-message">${data.message}</div>`)

			$.post("/bot_49", {message: data.message, intent: data.intent}, handle_pictures);
		}
		else {
			$('.chat-container').append(`<div class="chat-message col-md-5 offset-md-7 bot-message">${data.message}</div>`)
		}

		// remove the loading indicator
		$( "#loading" ).remove(); 
	}

	function handle_directions(data){
		$('.chat-container').append(`<div class="chat-message col-md-5"> <iframe allowfullscreen="" class="maps" frameborder="0" id="mapnavi" name="mapnavi" src=${data.fulfillmentText}> </iframe> </div>`)	
	}

	function handle_pictures(data){
		$('.chat-container').append(`<div class="chat-message col-md-5"> <img id="theImg" src=${data} style="max-width:auto; height:100%;"> </img> </div>`)

		// $('#theDiv').prepend('<img id="theImg" src="theImg.png" />')
	}
}


$('#target').on('submit', function(e){
	e.preventDefault();
	const input_message = $('#input_message').val()
	// return if the user does not enter any text
	if (!input_message) {
	return
	}
	
	$('.chat-container').append(`<div class="chat-message col-md-5 human-message">${input_message}</div>`)
	
	// loading
	$('.chat-container').append(` <div class="chat-message text-center col-md-2 offset-md-10 bot-message" id="loading"><b>...</b></div>`)
	
	// clear the text input
	$('#input_message').val('')
	
	// send the message to index.py to be sent to Dialog-Flow
	submit_message(input_message)
});
