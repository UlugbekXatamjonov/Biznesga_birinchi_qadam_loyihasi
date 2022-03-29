const bbbtt = document.querySelector("#bbbtt"),
  ikki = document.getElementById("ikki"),
  prev = document.getElementById("prev"),
  end = document.getElementById("buutttdds"),
  medya = document.getElementById("medya"),
  formd = document.getElementById('formd');
  
bbbtt.addEventListener("click", (e) => {
  e.preventDefault()
  ikki.classList.remove('d-none')
  bbbtt.classList.add('d-none')
  medya.classList.add('d-none')

});

prev.addEventListener('click',(e)=>{
  e.preventDefault()
  medya.classList.remove('d-none')
  ikki.classList.add('d-none')
  bbbtt.classList.remove('d-none')
})
const func =()=>{

}
end.addEventListener('click',(e)=>{
  // e.preventDefault()
  medya.classList.remove('d-none')
  ikki.classList.add('d-none')
  bbbtt.classList.remove('d-none')
  
})


