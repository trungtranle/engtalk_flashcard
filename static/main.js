counter = function() {
    var value = $('#id_essay').val();

    if (value.length == 0) {
        $('#wordCount').html(0);
      
        return;
    }

    var regex = /\s+/gi;
    var wordCount = value.trim().replace(regex, ' ').split(' ').length;
    

    $('#wordCount').html(wordCount);
    
};

$(document).ready(function() {
    $('#count').click(counter);
    $('#id_essay').change(counter);
    $('#id_essay').keydown(counter);
    $('#id_essay').keypress(counter);
    $('#id_essay').keyup(counter);
    $('#id_essay').blur(counter);
    $('#id_essay').focus(counter);
});