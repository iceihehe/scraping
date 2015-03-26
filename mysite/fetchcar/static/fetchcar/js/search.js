var main = function(){
	$.get("/fetchcar/_brand_api", function(data){
		var data = JSON.parse(data).brands;
		for (var i = 0; i < data.length; i ++){
			$("#select_brand").append($("<option>").text(data[i].name).val(data[i].id))			
		}
	})
	$("#select_brand").change(function(){
		var brand_id = $(this).val()
		$("#select_cartype").empty()
		$.get("/fetchcar/_cartype_api?brandid=" + brand_id, function(data){
			var data = JSON.parse(data).cartypes;
			for (var i = 0; i < data.length; i ++){
				$("#select_cartype").append($("<option>").text(data[i].name).val(data[i].id))
			}
		})
	})
}

$(document).ready(main)