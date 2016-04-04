var main = function() {
  $("a[name ='menu-button']").hover(
  	function() {
  		$('.submenu').show()
  	},
    function() {
  		$('.submenu').hide()
  	})
  	$('.submenu').hide()
};
$('document').ready(main)