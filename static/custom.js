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
		else if(data.intent == "resource"){
			$('.chat-container').append(`<div class="chat-message col-md-5 offset-md-7 bot-message"><a href ="https://${data.message}" style="color:#7CFC00	"> ${data.message} </a></div>`)

		}
		else if(data.intent == "food"){
			// $('.chat-container').append(`<div class="chat-message col-md-5 offset-md-7 bot-message">
			// <p>Food options on campus by building<br> You can get directions to the restaurants. examp "How do I get to Wendy's?"
			// <p><b>Student Union</b>  <br>-Bojangles<br>-Crown<br>-Bistro 49 <br>-Outtakes<br>-Sambazon<br>-Starbucks<br>-Wendy's<br>-Einstein Bros. Bagels<br></p>
			// <p><b>South Village Crossing</b>  <br>-Sovi<br>-Sovi2Go<br>-The Den<br>-Outtakes<br></p>
			// <p><b>Prospector</b> <br>-Smoked<br>-Chick-fil-A<br>-Mondo Subs<br>-Salsarita's<br>-Mamma Leone's<br>Feisty's<br></p>
			// <p><b>Cone Universtiy Center</b>  <br>-Subway<br>-Panda Express<br>-Bubble Tea<br> </p>
			// <p><b>Atkins Library</b>: Library Cafe </p>
			// <p><b>Student Activity Center</b>: Papa John's Pizza </p>
			// <p><b>Fretwell</b>: Fretwell Cafe </p>
			$('.chat-container').append(`<div class="chat-message col-md-5"> <img src="/static/images/Dining_Options.png" width="600" height="475"></img> 
			<p><b> Dining Hours and map: <b> <a href ="https://aux.uncc.edu/dining" style="color:#7CFC00	">aux.uncc.edu/dining</a>
			</div>`)
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
	function handle_resource(data){
		$('.chat-container').append(`<div class="chat-message col-md-5"> <img id="theImg" src=${data} style="max-width:auto; height:100%;"> </img> </div>`)
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
