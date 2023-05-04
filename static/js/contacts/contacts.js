window.addEventListener("load",function(event) {
    const checkbox = document.getElementById('is_report')

    const message = document.getElementsByClassName('message')

    let check_timer = window.setInterval(check, 100)

    const radiobutton1 = document.getElementById('bug_type1')
    const radiobutton2 = document.getElementById('bug_type2')
    const radiobutton3 = document.getElementById('bug_type3')

    const radiobuttons_p = document.getElementById('p_bug_type')

    const submit_button = document.getElementById('submit')

    radiobutton1.disabled = true
    radiobutton2.disabled = true
    radiobutton3.disabled = true

    radiobuttons_p.style.color = '#A0A0A0'

    checkbox.onclick = function () {
        if (checkbox.checked == true) {

            function radio_checker () {
                if (radiobutton1.checked == false && radiobutton2.checked == false && radiobutton3.checked == false && checkbox.checked == true) {
                    submit_button.disabled = true
                    submit_button.classList.remove('form_submit_hover')
                } else {
                    submit_button.disabled = false
                    submit_button.classList.add('form_submit_hover')
                    clearInterval(timer)
                }
            }

            let timer = setInterval(radio_checker, 10);

            radiobutton1.disabled = false
            radiobutton2.disabled = false
            radiobutton3.disabled = false

            radiobuttons_p.style.color = 'black'
        } else {
            radiobutton1.disabled = true
            radiobutton2.disabled = true
            radiobutton3.disabled = true

            radiobuttons_p.style.color = '#A0A0A0'
        }
    }

    function check () {
        if (typeof message[0] != 'undefined') {
            window.clearInterval(check_timer)
            console.log(message[0])
            message[0].style.opacity = '100%'
            let clear_timer = window.setInterval(clear, 1000)
        }
    }

    function clear () {
        if (typeof message[0] != 'undefined') {
            if (typeof clear_timer != 'undefined') {
                window.clearInterval(clear_timer)
            }
        }
    }
},false);


