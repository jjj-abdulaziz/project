document.addEventListener('DOMContentLoaded', function() {
    const barr = document.getElementById('barr');
    const close = document.getElementById('close');
    const nav = document.getElementById('navbar');

    if (barr) {
        barr.addEventListener('click', () => {
            nav.classList.add('active');
        });
    }

    if (close) {
        close.addEventListener('click', () => {
            nav.classList.remove('active');
        });
    }
});

 


$(document).ready(function() {
    $("#add-to-cart-btn").on("click", function() {
        let quantity = $("#product-quantity").val();  
        let productType = $("#productType").val(); 
        let product_title = $(".product-title").val(); 
        let product_id = $(".product-id").val();  
        let product_price = $("#current-product-price").text();  
        // let product_pid = $(".product-pid").val();
        // let product_image = $(".product-image").src();
        let this_val = $(this);

        
        console.log("Quantity:", quantity);
        console.log("Type:", productType);
        console.log("Title:", product_title);  
        console.log("Product ID:", product_id);
        // console.log("PID:", product_pid);
        // console.log("Image:", product_image);
        console.log("Product Price:", product_price);
        console.log("Current Element:", this_val);

        $.ajax({
            url: '/add-to-cart/',
            data: {
                "id": product_id,
                // "pid": product_pid,
                // "image": product_image,
                "title": product_title,
                "quantity": quantity,
                "type": productType,
                "price": product_price
            },
            dataType: "json",
            beforeSend: function(){
                console.log("Adding product to cart...");
            },
            success: function(response){
                this_val.html("Item added to cart");
                console.log("Product added to cart...");
            }
        });
    });

    $(".delete-product").on("click", function() {    
        let product_id = $(this).attr("data-product")
        let this_val = $(this)
 
        console.log("Product ID:", product_id);

        $.ajax({
            url: "/delete-from-cart",
            data: {
                "id": product_id
            },
            dataType: "json",
            beforeSend: function() {
                this_val.hide();
            },
            success: function(response) {
                this_val.show(); // Fixed: Added missing parentheses
                $("#cart-list").html(response.data);
            }
        })
});

});



