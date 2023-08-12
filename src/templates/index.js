const realFile = document.getElementById("realFile");
const customButton = document.getElementById("customButton");
const customText = document.getElementById("customText");

customButton.addEventListener("click", function() {
    realFile.click();
});

realFile.addEventListener("change", function() {
    if (realFile.value) {
        customText.textContent = realFile.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    } else {
        customText.textContent = "No file chosen";
    }
});