var vote = (hot) => {
  if(hot) {
    $.ajax({
      url: hotURL,
      dataType: "json",
      success: handleResponse
    })
  } else {
    $.ajax({
      url: notURL,
      dataType: "json",
      success: handleResponse
    })
  }
}

var handleResponse = (ro) => {
  if(ro.end) {
    endVoting();
    return;
  }
  hotURL = ro.hotURL;
  notURL = ro.notURL;
  $("#option-img").attr('src', ro.optionURL);
}

var endVoting = () => {
  $("#option-img").remove();
  $("#option-panel").append("<div class='finish-message text-center'>Thanks for voting!</div>").css('height', 367);
  $("#hot-btn").removeAttr('onclick');
  $("#not-btn").removeAttr('onclick');
}

$("#hot-btn").attr('onclick', 'vote(1)');
$("#not-btn").attr('onclick', 'vote(0)');
