function PlaySound(soundId) {
    let thissound = document.getElementById(soundId);
    let form = document.getElementById('conForm');

    form.addEventListener("submit", function (event) {
        if(form.checkValidity()) {
            thissound.play();
        }
    });
  }

  PlaySound('whoosh');