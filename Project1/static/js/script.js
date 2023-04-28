// ## DeepUI | 3D User interface builder
// ## Author: Jamie Coulter
// ## Depths can be defined on the html element as data-depth.
// ## Depth is calculated from the parent element with depth-ui set as true.

function deepUI() {

    /* =============================================================================
    Global Options
    ================================================================================ */
    
    const globalPerspective = 600; // Global perspective set to parent effect
    const sensitivity = 80; // Sets how much tilt we get, less is more in this case
    
    /* =============================================================================
    Chroma Options
    ================================================================================ */
    
    const chromaActive = true; // Turn on/off chromatic aberation
    const chromaFuzz = 1; // Amount of blur seen in the chromatic effect
    const chromaRed = 'rgba(255, 0, 0, 0.9)'; // Chromatic red rgba value
    const chromaYellow = 'rgba(255, 255, 0, 0.9)'; // Chromatic yellow rgba value
    const chromaBlue = 'rgba(0, 0, 255, 0.9)'; // Chromatic blue rgba value
    const chromaTeal = 'rgba(0, 255, 255, 0.9)'; // Chromatic teal rgba value
    const chromaMinOffset = 9; // Chromatic yellow / teal spread
    const chromaMaxOffset = 20; // Chromatic red / blue spread
    
    /* =============================================================================
    Elements
    ================================================================================ */
    
    const deepParent = $('*[data-deep-ui="true"]'); // Parent with deep active
    const deepElement = $('[data-depth]'); // Elements with depth
    const chromaElement = $('[data-chroma]'); // Elements with depth
    
    /* =============================================================================
    Set the perspective of every deep parent
    ================================================================================ */
    
    deepParent.each(function() {
        $(this).css({ // Set perspective of parent
            'perspective': `${globalPerspective}px`,
            'transform-style': 'preserve-3d'
        }); 
        setDepth(); // Set depths
    });

    /* =============================================================================
    Set the depths of all parent elements
    ================================================================================ */
    
    function setDepth() {
        // Set element depth
        deepElement.each(function() {
            $(this).css({
                'transform': `translatez(${$(this).data('depth')}px) translateY(-50%)`,
                'transform-style': 'preserve-3d' // Set CSS to all elements
            });
        });
    }

    /* =============================================================================
    Tilt the parent element depending on mouse position
    ================================================================================ */
    
    $(document).on('mousemove', e => {
        const x = -($(window).innerWidth() / 2 - e.pageX) / sensitivity; // Get current mouse x
        const y = ($(window).innerHeight() / 2 - e.pageY) / sensitivity; // Get current mouse y

        deepParent.css('transform', `rotateY(${x}deg) rotateX(${y}deg)`); // Set parent element rotation
        
        if(chromaActive) {
           deepChroma(x, y); // Set chromatic effects
        }
    });
    
    /* =============================================================================
    Set chromatic effect
    ================================================================================ */
    
    function deepChroma(x, y) {
        const chroma = 
            `${x / chromaMaxOffset}px ${y / chromaMaxOffset}px ${chromaFuzz}px ${chromaYellow}, 
             ${x / chromaMinOffset}px ${y / chromaMinOffset}px ${chromaFuzz}px ${chromaRed}, 
             ${-x / chromaMaxOffset}px ${-y / chromaMaxOffset}px ${chromaFuzz}px ${chromaTeal},
             ${-x / chromaMinOffset}px ${-y / chromaMinOffset}px ${chromaFuzz}px ${chromaBlue}`;
        const chromaImage = 
            `drop-shadow(${x / chromaMaxOffset}px ${y / chromaMaxOffset}px ${chromaFuzz}px ${chromaYellow})
             drop-shadow(${x / chromaMinOffset}px ${y / chromaMinOffset}px ${chromaFuzz}px ${chromaRed})
             drop-shadow(${-x / chromaMaxOffset}px ${-y / chromaMaxOffset}px ${chromaFuzz}px ${chromaTeal})
             drop-shadow(${-x / chromaMinOffset}px ${-y / chromaMinOffset}px ${chromaFuzz}px ${chromaBlue})`;
        chromaElement.each(function() {
            let element = $(this);
            if(element.data('chroma-text')) { // If element is text apply chroma effect as text shadow
                element.css('text-shadow', chroma);
            } else if(element.data('chroma-iamge')) { // If element normal apply chroma effect as box shadow
                element.css('box-shadow', chroma);
            } else {
                console.log(chromaImage)
                element.css('-webkit-filter', chromaImage);
            }
        });
    }
}

// Init
deepUI(); 

var vid = document.getElementById("myVideo"); 

function playVid() { 
    vid.play(); 
} 

$('.modal_button').click(function(){
    $('.modal').show();
    $(this).fadeOut(500);

    setTimeout(function(){
        playVid();
    },800);
 
    setTimeout(function(){
        $('h1,.text img,a').css('opacity','1');
        $('p').css('opacity','.6');
    },1700);
});

$('.close-modal').click(function(){
    // Fade the modal out:
    $('.modal').fadeOut(2000);
    

    
});