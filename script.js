let cartItems = [];

function addToCart(product, price) {
    cartItems.push({product, price});
    updateCart();
}

function updateCart() {
    let cartList = document.getElementById("cart-items");
    let totalElement = document.getElementById("total");
    let total = 0;

    cartList.innerHTML = "";
    cartItems.forEach(item => {
        let listItem = document.createElement("li");
        listItem.innerText = `${item.product} - $${item.price}`;
        cartList.appendChild(listItem);
        total += item.price;
    });

    totalElement.innerText = total;
}




// Add product and cart logic similar to the previous example

function checksout() {
    alert('Thank you for your purchase!');
}
