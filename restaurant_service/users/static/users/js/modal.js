document.addEventListener("DOMContentLoaded", () => {
  const foodCards = document.querySelectorAll(".food-card");
  const modal = document.getElementById("foodModal");
  const modalImage = document.getElementById("modalImage");
  const modalName = document.getElementById("modalName");
  const modalDescription = document.getElementById("modalDescription");
  const modalPrice = document.getElementById("modalPrice");
  const modalRating = document.getElementById("modalRating");
  const addToCartButton = document.getElementById("addToCartButton");
  const closeModal = document.getElementById("closeModal");

  let currentMenuItem = null;

  foodCards.forEach((card) => {
    card.addEventListener("click", () => {
      const name = card.getAttribute("data-name");
      const description = card.getAttribute("data-description");
      const price = card.getAttribute("data-price");
      const image = card.getAttribute("data-image");
      const rating = card.getAttribute("data-rating");
      const menuItemId = card.getAttribute("data-id");

      modalName.textContent = name;
      modalDescription.textContent = description;
      modalPrice.textContent = `$${price}`;
      modalImage.src = image;
      currentMenuItem = {
        id: menuItemId,
        name,
        description,
        price,
        rating,
        image,
      };

      const stars = modalRating.querySelectorAll("svg");
      stars.forEach((star, index) => {
        if (index < rating) {
          star.classList.add("text-yellow-600");
          star.classList.remove("text-gray-300");
        } else {
          star.classList.add("text-gray-300");
          star.classList.remove("text-yellow-600");
        }
      });

      modal.classList.remove("hidden");
      modal.style.display = "block";
    });
  });

  addToCartButton.addEventListener("click", () => {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    const itemIndex = cart.findIndex((item) => item.id === currentMenuItem.id);
    if (itemIndex > -1) {
      cart[itemIndex].quantity += 1;
    } else {
      currentMenuItem.quantity = 1;
      cart.push(currentMenuItem);
    }
    localStorage.setItem("cart", JSON.stringify(cart));
    alert(
      "Item added to Cart successfully! , view the cart to modify item quantity"
    );
    modal.classList.add("hidden");
  });

  closeModal.addEventListener("click", () => {
    modal.classList.add("hidden");
    modal.style.display = "none";
  });

  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.classList.add("hidden");
      modal.style.display = "none";
    }
  });
});
