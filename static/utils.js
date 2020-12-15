function copyToClipboard(element) {
    var $temp = $("<textarea>");
    var brRegex = /<br\s*[\/]?>/gi;
    $("body").append($temp);
    $temp.val($(element).html().replace(brRegex, "\r\n")).select();
    document.execCommand("copy");
    $temp.remove();
  }
  
  $( "#FailCopy" ).click(function() {
    alert("Well done! div #error-details has been copy to your clipboard, now paste it in the notepad or email!");
  });