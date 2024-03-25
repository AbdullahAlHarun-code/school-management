jQuery( document ).ready(function( $ ) {

    function updateFeesAmount() {
        console.log('yes')
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
                    $('#id_fees_amount').attr("readonly", true); 
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

    function updateFeeCategories() {
        console.log('category')
        var studentId = $('#id_student').val();
        if (studentId) {
            // Fetch the fee categories via AJAX
            $.ajax({
                url: '/get-fee-categories/',
                data: {
                    'student_id': studentId
                },
                dataType: 'json',
                success: function(data) {
                    // Update the fee_category select options
                    var feeCategorySelect = $('#id_fee_category');
                    feeCategorySelect.empty();
                    $.each(data, function(key, value) {
                        feeCategorySelect.append($('<option>').text(value).attr('value', key));
                    });
                }
            });
        }
    }

    // Attach change event listener to student select field
    $('#id_student').change(function() {
        updateFeeCategories();
    });

    // Initial call to update fee_category options
    updateFeeCategories();

  
  });


