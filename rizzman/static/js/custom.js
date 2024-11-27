// Tambahkan javascript disini 
function loginPopup() {
    const popup = document.getElementById('loginPop');
    const overlay = document.getElementById('overlay');
    const pageWrapper = document.getElementById('pageWrapper');

    if (popup.classList.contains('hidden')) {
        // Saat popup dibuka
        popup.classList.remove('hidden');
        popup.classList.add('popup-enter'); // Tambahkan animasi masuk
        overlay.classList.remove('hidden');
        pageWrapper.classList.add('blur-bg');

        // Hapus kelas animasi setelah animasi selesai
        setTimeout(() => {
            popup.classList.remove('popup-enter');
            popup.classList.add('flex'); // Tetapkan gaya flex setelah masuk
        }, 100); // Durasi animasi sesuai dengan CSS (0.3s)
    } else {
        // Saat popup ditutup
        popup.classList.remove('flex');
        popup.classList.add('popup-exit-active'); // Tambahkan animasi keluar
        overlay.classList.add('hidden');
        pageWrapper.classList.remove('blur-bg');

        // Sembunyikan popup setelah animasi selesai
        setTimeout(() => {
            popup.classList.add('hidden');
            popup.classList.remove('popup-exit-active');
        }, 300); // Durasi animasi sesuai dengan CSS (0.3s)
    }
}

const openBtn = document.querySelector('#open-btn');
const overlay = document.getElementById('overlay');

openBtn.addEventListener('click', () => {
    HSOverlay.open('#hs-unstyled-modal');
    overlay.classList.remove('hidden');
});

overlay.addEventListener('click', () => {
    HSOverlay.close('#hs-unstyled-modal');
    overlay.classList.add('hidden');
});