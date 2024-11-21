// Tambahkan javascript disini 

function showPass() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function togglePopup() {
    const popup = document.getElementById('loginPop');
    const overlay = document.getElementById('overlay');
    const pageWrapper = document.getElementById('pageWrapper');

    popup.classList.toggle('hidden');
    popup.classList.toggle('flex');
    overlay.classList.toggle('hidden');
    pageWrapper.classList.toggle('blur-bg'); // Tambahkan efek blur
}

