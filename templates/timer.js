
let time = Math.floor(Math.random() * 2);
//let Button = document.querySelector('#magic_8_button');
//self.response.write(name)

//Button.addEventListener('click', e => {
// print(time)
//console.log(time)
//console.log("test")
function myFunction(time) {
  document.write(time)
  console.log("pleaseshowup")
  typeof(time)
  if (time == 0) {
    setTimeout(function() {
      window.location.href = "http://localhost:8080/results3";
    }, 15000);

    let countDownDate = new Date(15).getTime();
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
    }, 1000);
  }
  else if (time == 1) {
    setTimeout(function() {
      window.location.href = "http://localhost:8080/results3";
    }, 30000);

    let countDownDate = new Date(30).getTime();
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
    }, 1000);
  }
}

myFunction(time);


//})
