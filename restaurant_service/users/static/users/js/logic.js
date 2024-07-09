document.addEventListener("DOMContentLoaded", () => {
  const foodCards = document.querySelectorAll(".food-card");
  const modal = document.getElementById("foodModal");
  const modalImage = document.getElementById("modalImage");
  const modalName = document.getElementById("modalName");
  const modalDescription = document.getElementById("modalDescription");
  const modalPrice = document.getElementById("modalPrice");
  const modalRating = document.getElementById("modalRating");
  const closeModal = document.getElementById("closeModal");
  const item_id = document.querySelector('.item_id');
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
      item_id.value = menuItemId
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

  $('#addToCartButton').click(function (e) {
        e.preventDefault();
        var item_id = document.querySelector('.item_id').value;
        var item_qty = document.querySelector('.item_qty').value;
        console.log(item_id, item_qty);
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
          method: "POST",
          url: "/add-to-cart",
          data: {
            'item_id':item_id,
            'item_qty':item_qty,
            csrfmiddlewaretoken: token
          },
          success: function (response) {
            alertify.success(response.status)
          }
        });
      })

  $('.changeQuantity').on('change', function (e) {
        e.preventDefault();
        var item_id = $(this).siblings('.item_id').val();
        var item_qty = $(this).val();
        console.log(item_id, item_qty);
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'item_id': item_id,
                'item_qty': item_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                // alertify.success(response.status);
            }
        });
      });
      

  $(document).on('click', '.delete-cart-item', function (e) { 
        e.preventDefault();

        var item_id = $(this).siblings('.item_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
          method: "POST",
          url: "delete-cart-item",
          data: {
            'item_id': item_id,
            csrfmiddlewaretoken: token
          },
          success: function (response) {
             alertify.success(response.status);
             $('.cartdata').load(location.href + " .cartdata");
          }
        });
        
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
