// static/script.js
document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const totalSum = document.getElementById('totalSum');
    const totalInput = document.getElementById('totalInput');
  
    function updateTotal() {
      let total = 0;
      checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
          total += parseFloat(checkbox.value);
        }
      });
      document.getElementById('totalSum').textContent = `${total}€`;
      document.getElementById('totalInput').value = total; 

    }
  
    checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', updateTotal);
    });
  });
  