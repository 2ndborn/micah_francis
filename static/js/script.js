function PlaySound(soundId) {
    let thissound = document.getElementById(soundId);
    let form = document.getElementById('conForm');

    form.addEventListener("submit", function (event) {
        if(form.reportValidity()) {
            event.preventDefault();  // Prevent the form from submitting
            thissound.play();
            thissound.volume = 0.2;  // Play the sound
            thissound.playbackRate = 0.5;  // Play the sound

            // Submit the form after the sound has finished playing
            thissound.onended = function() {
                form.submit();
            }
        }
    });
}

PlaySound('whoosh');