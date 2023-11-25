function redirectToMyUrl() {

    var Uname = document.getElementById('name').value
    var email = document.getElementById('inputEmail').value;
    var message = document.getElementById('message').value;
    var radioButtons = document.querySelectorAll('input[name="optradio"]:checked').length;

    if (!email || !message || radioButtons == 0) {
        alert('Please fill in all required fields.'); 
        exit()
    }

var mailFormat =  /\S+@\S+\.\S+/;
  if (!email.match(mailFormat)) {
    alert("Invalid email address!")
    exit()
  }
    
    alert('thank you ' + Uname + '. Will revert back to you as soon as possible. Enjoy!');
    
    var redirectUrl = myUrl 
    window.location.href =  redirectUrl 

  }


  
