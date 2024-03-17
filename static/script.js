const closebtn = document.querySelector(".messages button");
if (closebtn)
  closebtn.addEventListener("click", (e) => e.target.closest("li").remove());
