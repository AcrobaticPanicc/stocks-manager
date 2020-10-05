let res = document.getElementsByClassName('num');


for (let i = 0; i < res.length; i++) {
    if (parseFloat(res[i].innerHTML.match(/(-?\d+)/g)[0]) > 0) {
        res[i].classList.add('g');
    } else if (parseFloat(res[i].innerHTML.match(/(-?\d+)/g)[0]) < 0) {
        res[i].classList.add('r');
    }
}
