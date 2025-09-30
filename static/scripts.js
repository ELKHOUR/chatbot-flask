const numStars = 100;
const body = document.body;

for (let i = 0; i < numStars; i++) {
  const star = document.createElement("div");
  star.classList.add("star");

  const top = Math.random() * window.innerHeight;
  const left = Math.random() * window.innerWidth;
  star.style.top = `${top}px`;
  star.style.left = `${left}px`;

  const size = Math.random() * 2 + 1;
  star.style.width = `${size}px`;
  star.style.height = `${size}px`;

  // Random twinkle duration, very slow horizontal movement
  star.style.animationDuration = `${Math.random() * 2 + 1}s, ${Math.random() * 150 + 150}s`;

  body.appendChild(star);
}


function getUserResonse(){
    userInput = $('#userInput').val();
    userInputHTML = "<p class='botText'>" + userInput + "</p>"
    $('#userInput').val('');
    $('.texts').append(userInputHTML);
    $.get('/get', {user_input:userInput}).done(function(data){
     var botHTML = "<p class='userText'>" + data + "</p>"
      $('.texts').append(botHTML);
      document.querySelector(".texts").scrollTop = document.querySelector(".texts").scrollHeight
    });

}
$('#userInput').keypress(function(e){
    if( e.which == 13 & $('#userInput').val().trim() != ''){
        getUserResonse();
    }
 });

$('#send').click(function(){
    if ($('#userInput').val().trim() != ''){
        getUserResonse()
    }
})























