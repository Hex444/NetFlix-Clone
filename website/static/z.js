flash_dismiss = document.querySelector('.dismiss')
flash = document.querySelector('.flashed')


document.querySelector('.dismiss').addEventListener('click', function(){
    document.querySelector('.flashed').style.display = 'none';
})