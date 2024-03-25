jQuery( document ).ready(function( $ ) {

    function updateFeesAmount() {
        var feeCategoryId = $('#id_fee_category').val();
        if (feeCategoryId) {
            // Fetch the fees_amount via AJAX
            $.ajax({
                url: '/get-fees-amount/',
                data: {
                    'fee_category_id': feeCategoryId
                },
                dataType: 'json',
                success: function(data) {
                    // Update the fees_amount field with the fetched value
                    $('#id_fees_amount').val(data.fees_amount);
                }
            });
        }
    }

    // Attach change event listener to fee_category field
    $('#id_fee_category').change(function() {
        updateFeesAmount();
    });

    // Initial call to update fees_amount field
    updateFeesAmount();
  
  });


