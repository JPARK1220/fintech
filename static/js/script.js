function showPopup(year, content) {
    const popup = document.getElementById('popup');
    popup.innerHTML = `<strong>Year: ${year}</strong><p>${content}</p>`;
    popup.style.display = 'block';
}
