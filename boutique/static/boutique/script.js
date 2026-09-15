const menuToggle = document.getElementById("menuToggle");
const menu = document.getElementById("menu");

menuToggle.addEventListener("click", function () {
    menu.classList.toggle("ouvert");
});

const liens = menu.querySelectorAll("a");

liens.forEach(function (lien) {
    lien.addEventListener("click", function () {
        menu.classList.remove("ouvert");
    });
});