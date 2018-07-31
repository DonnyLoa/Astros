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
    }, 1000);
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
//})
