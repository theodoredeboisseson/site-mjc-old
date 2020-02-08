// Map pin svg change color when hovered
$(".mappinfooter").on("mouseover", function() {
    $("#mappinfooterID").attr( 'fill','white');
    }).on("mouseleave", function() {
    $("#mappinfooterID").attr( 'fill','red');
    });
    
    
// Profile svg change color when hovered
$(".userprofile").on("mouseover", function() {
    $("#userProfileCircle").attr( 'fill','white');
    $("#userProfileUser").attr( 'fill','#DD5600');
    }).on("mouseleave", function() {
    $("#userProfileCircle").attr( 'fill','#DD5600');
    $("#userProfileUser").attr( 'fill','white');
    });
    
    
// Image link
function goTo(url) {
    window.location.href = url;
}

// Nav link
function goToNavbar(url) {
    if ($(window).width() > 767) {
      window.location.href = url;
    }
    else {
      ;
    }
}

// Go back button
function goBack() {
        window.history.back();
    }
    
// Filters feature

let filtersCitiesArray          = [];
let filtersDaysArray            = [];
let filtersPeriodArray          = [];
let filtersAnimationTypeArray   = [];


function FilterActivities(value,filter,category) {
            
    value  = value.toLowerCase()
    filter = filter.toLowerCase()
    timer  = 0;
    
    if($('#FilterToggle_'+value+'_input').is(':checked')) {
        
        // change style applied to the toggle switch
        $('#FilterToggle_'+value+'_label').addClass("bg-filter-on");
        $('#FilterToggle_'+value+'_label').removeClass("bg-filter-off");
        
        if (category == "city") { 
            
            // Hide all elements (reset)
            $("[data-filter-city]").hide(timer);
            // Add new filter
            filtersCitiesArray.push(filter);
            
        };
        
        if (category == "day") { 
            
            // Hide all elements (reset)
            $("[data-filter-day]").hide(timer);
            // Add new filter
            filtersDaysArray.push(filter);
            
        };
        
        if (category == "time") {
            
            // Hide all elements (reset)
            $("[data-filter-time-start]").hide(timer);
            // Add new filter
            filtersPeriodArray.push(filter);
    
        };
        
        if (category == "animation_type") {
            
            // Hide all elements (reset)
            $("[data-filter-animation_type]").hide(timer);
            // Add new filter
            filtersAnimationTypeArray.push(filter);
            
            // Show only those with filters
            let blocks = $("*").filter(dataFilterOR(filtersAnimationTypeArray,"data-filter-animation_type"))
            blocks.finish();
            blocks.show(timer);
        };
        
        
    } else {
        
        // change style applied to the toggle switch
        $('#FilterToggle_'+value+'_label').addClass("bg-filter-off");
        $('#FilterToggle_'+value+'_label').removeClass("bg-filter-on")

        if (category == "city") { 
            
            // Hide all elements (reset)
            $("[data-filter-city]").hide(timer);
            // Remove filter from array
            filterRemove(filtersCitiesArray, filter);
            
        };
        
        if (category == "day") { 
            
            // Hide all elements (reset)
            $("[data-filter-day]").hide(timer);
            // Remove filter from array
            filterRemove(filtersDaysArray, filter);
            
        };
        
        if (category == "time") {
            
            // Hide all elements (reset)
            $("[data-filter-time-start]").hide(timer);
            // Add new filter
            filterRemove(filtersPeriodArray, filter);
            
        };
        
        if (category == "animation_type") { 
            
            // Hide all elements (reset)
            $("[data-filter-animation_type]").hide(timer);
            // Remove filter from array
            filterRemove(filtersAnimationTypeArray, filter);
            // Show only the elements with filters in the array ("OR")
            
            // Show only those with filters
            let blocks = $("*").filter(dataFilterOR(filtersAnimationTypeArray,"data-filter-animation_type"))
            blocks.finish();
            blocks.show(timer);
        };

    }
        
        // select and show
        let lines =  $("*").filter(dataFilterOR(filtersCitiesArray, "data-filter-city"))
              .filter(dataFilterOR(filtersDaysArray, "data-filter-day"))
              .filter(timeFilterOR(filtersPeriodArray, "data-filter-time-start" , 5));
        
        lines.finish();
        lines.show(timer);


        hideEmptyAnimations();
        hideEmptyTypes();

}

function dataFilterOR(array, attribute) {
    
    // Show only those with listed filters
    let filtersString = "";
    
    let l  = array.length;
    
    for (i=0 ; i < l ; i++) {
        
        // jQuery selector
        filtersString += "[" + attribute + "*=" + array[i] + "]";
        
        // OR : add a "," if more than one filter (and not the last one)
        if (l > 1 && i != (l-1) ) {
            filtersString += ",";
        };
    };
    
    return filtersString
    
}

function timeFilterOR(array, attribute, range) {
    
    // Show only those with listed filters
    let filtersString2 = "";
    
    let l  = array.length;
    
    for (i=0 ; i < l ; i++) {
        
        for (j=0 ; j < range ; j++) {
            n = parseInt(array[i]) + j;
            
            // jQuery selector
            if (n < 10) {
                filtersString2 += "[" + attribute + "=0" + n + "]";  
            }
            else {
                filtersString2 += "[" + attribute + "=" + n + "]";
            }
            
            // OR : add a "," if more than one filter (and not the last one)
            if (j != range-1 ) {
                filtersString2 += ",";
            };
            
        };
        
        // OR : add a "," if more than one filter (and not the last one)
        if (l > 1 && i != (l-1) ) {
            filtersString2 += ",";
        };
        
    };
    
    return filtersString2
    
}

// Remove one filter from the array
function filterRemove(array, filter) {
    
    var index = array.indexOf(filter);
    if (index > -1) {
      array.splice(index, 1);
    };

};


function hideEmptyAnimations() {

    $(".wrapper_animation").each(function() {

        var lines_all = $(this).find("table>tbody>tr");
        var lines_hidden = $(this).find("table>tbody>tr[style='display: none;']");

        if (lines_hidden.length == lines_all.length) {
            $(this).hide();
        } else {
            $(this).show();
        }

    })

};

function hideEmptyTypes() {
 
    $(".wrapper_type").each(function() {
     
        var animations = $(this).find(".wrapper_animation");
        var animations_hidden = $(this).find(".wrapper_animation[style='display: none;']");

        if (animations.length == animations_hidden.length) {
            $(this).children(".no-results").show();
        } else {
            $(this).children(".no-results").hide();
        }
    
    });

};


function Initialisation() {
      $('.filter-initialisation').hide(); 
  }

window.onload = Initialisation() 

