// SMART FOOD APP

console.log("Smart Food App Loaded Successfully");

// Welcome Alert

function welcomeMessage(){

    console.log("Welcome To Smart Food");

}

// Button Click Effect

const buttons = document.querySelectorAll("button");

buttons.forEach(button => {

    button.addEventListener("click", () => {

        button.style.transform = "scale(0.95)";

        setTimeout(() => {

            button.style.transform = "scale(1)";

        }, 100);

    });

});