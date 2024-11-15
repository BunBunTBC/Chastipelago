// gets mainToken from the URL
const hash = window.location.hash.substring(1);
const params = JSON.parse(decodeURIComponent(hash));
const mainToken = params.mainToken;

// extension renders here
const form = document.createElement('form');

// Create form inputs
const inputIP = document.createElement('input');
inputIP.type = 'text';
inputIP.name = 'serverIP';
inputIP.placeholder = 'Server IP';

const inputPort = document.createElement('input');
inputPort.type = 'text';
inputPort.name = 'serverPort';
inputPort.placeholder = 'Server Port';

const inputPassword = document.createElement('input');
inputPassword.type = 'password';
inputPassword.name = 'serverPassword';
inputPassword.placeholder = 'Server Password';

const inputPlayerName = document.createElement('input');
inputPlayerName.type = 'text';
inputPlayerName.name = 'playerName';
inputPlayerName.placeholder = 'Player Name';

const newButton = document.createElement('button');
newButton.type = 'submit';
newButton.textContent = 'Connect';

// Add elements to form
form.appendChild(inputIP);
form.appendChild(inputPort);
form.appendChild(inputPassword);
form.appendChild(inputPlayerName);
form.appendChild(newButton);

// Append form to the DOM
document.body.appendChild(form);

// passes all needed information to the backend
function sendData() {
    const formData = new FormData(form);
    formData.append('value', mainToken)
    
    fetch('/establishConnection',{
        method:'POST',
        body: formData
    }
)}

// calls the sendData function when the form is submitted
form.addEventListener('submit', (event) => {
    event.preventDefault();
    sendData();
})

