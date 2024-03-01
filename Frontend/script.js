let modal = document.getElementById("myResume");
let btn = document.getElementById("resume-button");

let span = document.getElementsByClassName("close")[0];
btn.onclick = () => {
  modal.style.display = "block";
};

span.onclick = () => {
  modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};
