let button = document.getElementById("changeprofileimage");
let image = document.getElementById("profileimage");

button.onchange = () => {
    let reader = new FileReader();
    reader.readAsDataURL(button.files[0]);
    reader.onload = () => {
        image.setAttribute("src",reader.result);
    }
}