let time = Math.random() * math.floor(3);
//let Button = document.querySelector('#magic_8_button');
//self.response.write(name)

//Button.addEventListener('click', e => {
// print(time)
//console.log(time)
//console.log("test")
function myFunction(time) {
  if (time == 0) {
    setTimeout(function() {
      window.location.href = "http://localhost:8080/results";
    }, 10000000);
  }
  else if (time == 1) {
    setTimeout(function() {
      window.location.href = "http://localhost:8080/results";
    }, 5000);
  }
  else if (time == 2) {
    setTimeout(function() {
      window.location.href = "http://localhost:8080/results";
    }, 10000);
  }
}

myFunction(time);
<<<<<<< HEAD

let countDownDate = new Date(10000).getTime();
let distance = countDownDate;
let seconds = distance;

let x = setInterval(function() {  // Update the count down every 1 second
  console.log(seconds)
  seconds = seconds - 1

  document.getElementById("countdown").innerHTML = seconds + "s ";

  if (distance < 0) {
    clearInterval(x); // If the count down is finished, write some text
    document.getElementById("countdown").innerHTML = "EXPIRED";
  }
}, 1000000);
=======
>>>>>>> master
//})
