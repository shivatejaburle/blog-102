// Get the alert message by css class name 'alert'
var alert_messages = document.getElementsByClassName("alert-dismissible");

// Remove the alert box after 10 seconds
setTimeout(function() {
    for (let i = 0; i < alert_messages.length; i++) {
        alert_messages[i].remove();
      }
}, 10000);
