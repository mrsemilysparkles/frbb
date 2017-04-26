$(function() {
  // let's go.
  app();
});

var app = function() {
  $(document).keypress(function(e) {
    console.log('key '+  e.which + 'pressed.');
    // see if we have a registered listener.
    var link = URL_KEY_MAP[e.which] || URL_KEY_MAP[e.which + 48];
    if (link) {
      // Go to the page
      window.location.href = link;
    }
    var action = ACTION_MAP[e.which] || ACTION_MAP[e.which + 48];
    if (action) {
      action();
    }
    var form = $("form");
    if (form.length) {
      form.submit();
    }
    // e.preventDefault();
  });
  console.log(URL_KEY_MAP);
  console.log(ACTION_MAP);
};


var setEl = function(from, to) {
  document.getElementById(from).value = document.getElementById(to).value;
};
