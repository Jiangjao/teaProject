let menus = document.getElementById('com_headtop');
    var links = menus.getElementsByTagName('a');
    console.log(links)
    for (var i = 0; i < links.length; i++) {
        links[i].onmouseclick = function () {
            for (var j = 0; j < links.length; j++) {
                console.log(j)
                if(links[j] == this) {
                    this.style.color = '#226934f5';
                    this.style.cursor = 'pointer'
                    console.log(this)
                } else {
                    links[j].style.color = '';
                }
            }
        }
}