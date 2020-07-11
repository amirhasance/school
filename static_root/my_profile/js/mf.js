function f (index){
		
    var center_element = document.getElementById('center')
    
     $.ajax(
         {
         url: "ajax/", 

         data : {
            'index':index
         },

         dataType : 'json',

         success: function(result){
                   $("#div1").html(result);
                   console.log(result)}
                   
   });

}