document.addEventListener("DOMContentLoaded", () => {
  const cartItemsElement = document.getElementById("cartItems");
  const emptyCartMessage = document.getElementById("emptyCartMessage");
  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  function updateCart() {
    cartItemsElement.innerHTML = "";
    if (cart.length === 0) {
      emptyCartMessage.classList.remove("hidden");
    } else {
      emptyCartMessage.classList.add("hidden");
      cart.forEach((item, index) => {
        const cartItemElement = document.createElement("li");
        cartItemElement.classList.add(
          "flex",
          "items-center",
          "justify-between",
          "card",
          "p-3",
          "rounded-xl",
          "mb-3",
          "hover:shadow-2xl",
          "transition",
          "duration-300"
        );
        cartItemElement.innerHTML = `
                        <div class="flex items-center">
                            <img src="${item.image}" alt="${item.name}" class="w-16 h-16 object-cover circle">
                            <div class="ml-2">
                                <h3 class="text-xl font-semibold text-orange-800">${item.name}</h3>
                                <p class="text-gray-800">$${item.price}</p>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <input type="number" min="1" value="${item.quantity}" class="quantity-input w-16 text-center border border-black bg-gray-200" data-index="${index}">
                            <button class="remove-button ml-2 bg-red-600 text-white px-2 py-1 rounded text-white text-base font-medium rounded-md w-full shadow-xl hover:bg-red-800 text-center transition-all duration-300 transform" data-index="${index}">Remove</button>
                        </div>
                    `;
        cartItemsElement.appendChild(cartItemElement);
      });
    }
  }

  updateCart();

  cartItemsElement.addEventListener("change", (e) => {
    if (e.target.classList.contains("quantity-input")) {
      const index = e.target.getAttribute("data-index");
      cart[index].quantity = parseInt(e.target.value);
      localStorage.setItem("cart", JSON.stringify(cart));
    }
  });

  cartItemsElement.addEventListener("click", (e) => {
    if (e.target.classList.contains("remove-button")) {
      const index = e.target.getAttribute("data-index");
      cart.splice(index, 1);
      localStorage.setItem("cart", JSON.stringify(cart));
      updateCart();
    }
  });
});
