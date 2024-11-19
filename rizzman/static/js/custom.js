// Tambahkan javascript disini 
let isColorChanged = false;

document.getElementById('ubah-warna-bg').addEventListener('click', () => {
    const loginContainer = document.getElementById('login-container');
    if (loginContainer) {
        if (!isColorChanged) {
            loginContainer.classList.remove('bg-gray-100');
            loginContainer.classList.add('bg-green-500');
            isColorChanged = true;
        } else {
            loginContainer.classList.remove('bg-green-500');
            loginContainer.classList.add('bg-gray-100');
            isColorChanged = false;
        }
    }
});

function showPass() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}