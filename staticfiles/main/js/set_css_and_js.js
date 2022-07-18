if (document.documentElement.clientWidth > 500) {
var $head = document.head,
        $link = document.querySelector('link');

    $link.rel = 'stylesheet';
    $link.href = "{% static 'main/css/main.css' %}";

    $head.appendChild($link);
}
else if (document.documentElement.clientWidth <= 500) {
var $head = document.head,
        $link = document.querySelector('link');

    $link.rel = 'stylesheet';
    $link.href = "{% static 'main/css/main_telephone.css' %}";

    $head.appendChild($link);

    var $body = document.body,
        $divindiv_close = document.createElement('div');
        $divindiv_close.class = 'div_for_close_divindiv';
    $body.appendChild($divindiv_close);

    var $body = document.body,
        $div_for_close = document.createElement('div');
        $div_for_close.class = "div_for_close";
        $divindiv_close.appendChild($div_for_close);

    var $body = document.body,
        $aside = document.querySelector('aside');
        $toggle = document.createElement('div');
        $toggle.class = "toggle";
        $aside.appendChild($toggle)

    var $body = document.body,
        $script_toggle = document.createElement('script');
        $script_toggle.innerHTML = "var toggle = document.querySelector('.toggle');toggle.onclick = function() {var navigation = document.querySelector('.divindivaside');navigation.classList.toggle('active');var close = document.querySelector('.div_for_close');close.classList.toggle('active_close');var close_div = document.querySelector('.div_for_close_divindiv');close_div.classList.toggle('for_close_divindiv_2');";
        $body.appendChild($script_toggle);
}