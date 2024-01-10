let btn = document.getElementById("btn")
let main = document.getElementById("main")
let rand = 0;
btn.addEventListener("click", () => {
    rand = Math.floor(Math.random() * 70);

    fetch(`http://localhost:8000/jokes-api/${(rand)}?format=json`).then((res) => {

        return res.json()
    }).then((data) => {

        main.innerText = data["desc"]
        main.classList.add("p-4")
    })
})