document.addEventListener('DOMContentLoaded', function(){
	const anuncio = document.getElementById('promo-banner');
	const botonCerrar = document.getElementById('promo-close-button');
	
	if (anuncio&&botonCerrar){
		botonCerrar.addEventListener('click', function(){
			anuncio.style.display = 'none';
		});
	} else {
		console.error("El anuncio o el boton de cierre no se encontraron.");
	}
});	