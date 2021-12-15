const navBar = document.querySelector('.nav-bar')
const button = document.querySelector('.three_dots')
button.addEventListener('click', function(){
    navBar.classList.toggle('active')
})