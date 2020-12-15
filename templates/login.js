function getToken(){

    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
            
// Sending and receiving data in JSON format using POST method
//
    if ( username == "Matti" && password == "testi"){
        alert ("Login successfully");
        window.location = "order.html"; // Redirecting to other page.

        return false;
    }
        else{
        attempt --;// Decrementing by one.
        alert("You have left "+attempt+" attempt;");
        // Disabling fields after 3 attempts.
        if( attempt == 0){
        document.getElementById("username").disabled = true;
        document.getElementById("password").disabled = true;
        document.getElementById("submit").disabled = true;
        return false;
        }
    
    
    }
 
};