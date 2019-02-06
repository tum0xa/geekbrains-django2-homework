window.onload = function () {


    $('.pro-remove').on('click', 'a', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/remove/" + t_href.dataset.remove,

            success: function (data) {
                $('.basket_list').html(data.result);
                $('.header-mini-cart').html(data.basket_info);
                $('.cart-total').html(data.basket_total);
            },
        });

        return true;
    });

    var btn_add = $('#add_to_basket');
    try {
        var pk = btn_add[0].dataset.pk;
        var input = $(".pro-qty > input");

        btn_add.on('click', function () {

            var quantity = input[0].value;

            $.ajax({
                url: "/basket/add/" + pk + "/" + quantity,
                success: function (data) {
                    $('.header-mini-cart').html(data.basket_info);
                },
            });

            event.preventDefault();
        });
    }
    catch (e) {
        console.log("");
    }

    $('.basket_list').on('click', 'input, span', function () {
        var obj = event.target;
        // console.log(obj);
        var pk = obj.dataset.pk;
        // console.log(pk);
        var quantity = $('input[data-pk='+ pk +']')[0].value;
        $.ajax({
            url: "/basket/edit/" + pk + "/" + quantity,

            success: function (data) {
                $('.basket_list').html(data.result);
                $('.header-mini-cart').html(data.basket_info);
                $('.cart-total').html(data.basket_total);
            },
        });
        return false;
        event.preventDefault();
    });
    $('.action-buttons').on('click', '.add_to_cart', function () {
        var obj = event.target;
        // console.log(obj);
        var pk = obj.dataset.pk;
        // console.log(pk);
        var quantity = 1;
        $.ajax({
            url: "/basket/add/" + pk + "/" + quantity,

            success: function (data) {
                // $('.basket_list').html(data.result);
                $('.header-mini-cart').html(data.basket_info);
                // $('.cart-total').html(data.basket_total);
            },
        });
        return false;
        event.preventDefault();
    });

    $('.action-buttons').on('click', '.add_to_wishlist', function () {
        var obj = event.target;
        // console.log(obj);
        var pk = obj.dataset.pk;
        // console.log(pk);
        alert("Продукт добавлен в список желаемого!");
        $.ajax({
            url: "/wishlist/add/" + pk + "/",

            success: function (data) {

                $('.header-wishlist').html(data.wishlist_info);

            },
        });
        // return false;
        // event.preventDefault();
    });
    $('.action-buttons').on('click', '.remove_from_wishlist', function () {
        var obj = event.target;

        var pk = obj.dataset.pk;
        alert("Продукт удален из списка желаемого!");
        $.ajax({
            url: "/wishlist/remove/" + pk + "/",

            success: function (data) {

                $('.header-wishlist').html(data.wishlist_info);

            },
        });
        // return false;
        // event.preventDefault();
    });
};
// var windows = $(window);
//
// /*--
//     Menu Sticky
// -----------------------------------*/
// var sticky = $('.header-sticky');
//
// windows.on('scroll', function() {
//     var scroll = windows.scrollTop();
//     if (scroll < 300) {
//         sticky.removeClass('is-sticky');
//     }
//     else{
//         sticky.addClass('is-sticky');
//     }
// });