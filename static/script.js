$(document).ready(function() {
    // Add loading animation
    const loading = $('<div class="loading"></div>');
    $('#result').before(loading);

    $('#predictionForm').on('submit', function(e) {
        e.preventDefault();
        loading.show();
        $('#result').hide();
        
        const formData = {
            'Age': parseFloat($('#age').val()),
            'Pos': $('#position').val(),
            'PTS': parseFloat($('#pts').val()),
            'AST': parseFloat($('#ast').val()),
            'TRB': parseFloat($('#reb').val())
        };

        // Animate form fields on submit
        $('.form-control').addClass('submitted').delay(1000).queue(function(){
            $(this).removeClass('submitted').dequeue();
        });

        $.ajax({
            url: '/predict',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                loading.hide();
                if (response.status === 'success') {
                    $('#predictedSalary').text(response.predicted_salary);
                    $('#result').fadeIn(500);
                } else {
                    showError(response.message);
                }
            },
            error: function(error) {
                loading.hide();
                showError('Error making prediction. Please try again.');
            }
        });
    });

    // Add floating label effect
    $('.form-control').on('focus blur', function (e) {
        $(this).parents('.form-group').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
    }).trigger('blur');

    function showError(message) {
        const errorDiv = $('<div>')
            .addClass('alert alert-danger animate__animated animate__shakeX')
            .text(message);
        $('#result').html(errorDiv).show();
    }
});
