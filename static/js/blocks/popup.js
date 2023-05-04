window.addEventListener("load",function(event) {
    const authenticatedButton = document.getElementById('authenticated')
    const menu = document.getElementById('popup_menu')
    const authenticatedButtonParent = document.getElementById('authenticatedParent')
    const authenticatedButtonChild = document.getElementsByClassName('popup_menu_child')

    if (authenticatedButton != null) {
        const authenticatedImg = authenticatedButton.childNodes[3]
        const authenticatedDiv = authenticatedButton.childNodes[1]
        const authenticatedDivP = authenticatedDiv.childNodes[1]
    }

    // menu.style.top = '-100px'

    let menuState = 'none'

    function sleep(milliseconds) {
      const date = Date.now();
      let currentDate = null;
      do {
        currentDate = Date.now();
      } while (currentDate - date < milliseconds);
    }


    if (authenticatedButton != null) {
        authenticatedButton.onclick = function () {
            let authenticatedButtonParentWidth = authenticatedButtonParent.getBoundingClientRect().width.toFixed(0)
            let authenticatedButtonParentHeight = authenticatedButtonParent.getBoundingClientRect().height.toFixed(0) + 'px'

            menu.style.width = authenticatedButtonParentWidth + 'px'

            for (let i = 0; i < authenticatedButtonChild.length; i++) {
                authenticatedButtonChild[i].style.width = authenticatedButtonParentWidth * 0.9 + 'px'
            }

            if (menuState == 'none') {
                menuState = 'block'
                menu.style.top = authenticatedButtonParentHeight
            } else {
                menuState = 'none'
                menu.style.top = '-100px'
            }

            document.onclick = function (event) {
                if (event.target != authenticatedButton && event.target != authenticatedImg && event.target != authenticatedDiv && event.target != authenticatedDivP) {
                    if (menuState == 'none') {

                    } else {
                        menuState = 'none'
                        menu.style.top = '-100px'
                    }
                }
            }
        }
    }

    // for mobile

    const mainNav = document.getElementById('main_nav')

    if (screen.width >= 320 && screen.width <= 767) {
        mainNav.innerHTML += '<div class="close_menu_cont" id="close_menu_cont" style="width: ' + screen.width + 'px;"><img src="../../static/img/buttons/close_menu.png" id="close_menu" class="close_menu" style="margin-left:' + (screen.width - Math.round(screen.width / 10)) / 2 + 'px;" width="' + Math.round(screen.width / 10) + 'px"></div>'
    }

    const home_href = document.getElementById('home_href')
    const img = document.getElementById('logo')
    const main_nav_ul = document.getElementById('main_nav_ul')
    const authenticatedParent = document.getElementById('authenticatedParent')
    const loginButton = document.getElementById('login')
    const popupMenuUpper = document.getElementsByClassName('popup_menu_upper')
    const closeMenuCont = document.getElementById('close_menu_cont')
    const closeMenu = document.getElementById('close_menu')
    const mainNavBack = document.getElementById('main_nav_back')

    let imgLeft = Math.round(screen.width / 10 / 4)
    let imgActLeft = imgLeft
    let imgVis = true

    let navTop = -600
    let navActTop = navTop

    let mainNavBackOp = 0

    let closeMenuTop = 0

    if (screen.width >= 320 && screen.width <= 767) {
        home_href.removeAttribute('href')
        img.style.width = Math.round(screen.width / 10) + 'px'

        img.style.position = 'fixed'
        img.style.left = Math.round(screen.width / 10 / 4) + 'px'
        img.style.top = Math.round(screen.width / 10 / 4) + 'px'

        main_nav_ul.style.top = '-600px'
        authenticatedParent.style.top = '-200px'

        main_nav_ul.style.width = screen.width + 'px'
        authenticatedParent.style.width = screen.width + 'px'

        closeMenuCont.style.position = 'absolute'

        mainNavBack.style.backgroundColor = 'white'

        if (loginButton != null) {
            loginButton.innerHTML = loginButton.innerHTML.toUpperCase()
        }

        if (popupMenuUpper[0] != undefined) {
            if (popupMenuUpper[0] != undefined && popupMenuUpper[1] != undefined) {
                popupMenuUpper[0].innerHTML = popupMenuUpper[0].innerHTML.toUpperCase()
                popupMenuUpper[1].innerHTML = popupMenuUpper[1].innerHTML.toUpperCase()
            }
            closeMenuTop = 130
        } else {
            closeMenuTop = 60
        }
    }

    function timer () {
        // if (screen.width >= 320 && screen.width <= 767) {
        //
        // }

        authenticatedParent.style.top = parseInt(main_nav_ul.style.top.slice(0, -2)) + 380 + 'px'
        closeMenuCont.style.top = parseInt(authenticatedParent.style.top.slice(0, -2)) + closeMenuTop + 'px'

        imgActLeft = parseInt(img.style.left.slice(0, -2))
        navActTop =  parseInt(main_nav_ul.style.top.slice(0, -2))

        img.onclick = function () {
            window.scrollTo(0, 0)

            if (imgVis == true) {
                imgVis = false

                mainNav.style.position = 'absolute'
                mainNav.style.left = 0
                mainNav.style.top = 0
                mainNav.style.height = screen.height + 'px'
                mainNav.style.width = screen.width + 'px'

                mainNavBack.style.position = 'absolute'
                mainNavBack.style.left = 0
                mainNavBack.style.top = 0
                mainNavBack.style.height = document.getElementsByTagName('html')[0].scrollHeight + 'px'
                mainNavBack.style.width = screen.width + 'px'
                mainNavBack.style.zIndex = '500'
                mainNavBackOp = 0.96

                document.body.style.overflowY = 'hiden'

                imgLeft = -50
                navTop = 0
            } else {
                imgVis = true

                imgLeft = Math.round(screen.width / 10 / 4)
                navTop = -600

                mainNav.style.display = 'block'
            }
        }

        if (imgLeft != imgActLeft) {
            if (imgLeft > imgActLeft) {
                img.style.left = imgActLeft + 1 + 'px'
            } else {
                img.style.left = imgActLeft - 1 + 'px'
            }
        }

        if (navTop != navActTop) {
            if (navTop > navActTop) {
                main_nav_ul.style.top = navActTop + 2 + 'px'
            } else {
                main_nav_ul.style.top = navActTop - 2 + 'px'
            }
        }

        if (mainNavBackOp != mainNavBack.style.opacity) {
            if (mainNavBackOp > mainNavBack.style.opacity) {
                mainNavBack.style.opacity = String(+mainNavBack.style.opacity + 0.01)
            } else {
                mainNavBack.style.opacity = String(+mainNavBack.style.opacity - 0.01)
            }
        }

        closeMenu.onclick = function () {
            navTop = -600
            imgLeft = Math.round(screen.width / 10 / 4)
            imgVis = true

            mainNavBackOp = 0

            mainNav.style.height = Math.round(screen.width / 8) + 'px'
            mainNav.style.width = mainNav.style.height

            mainNavBack.style.height = '0px'
            mainNavBack.style.width = '0px'

            document.body.style.overflowY = 'visible'
        }

        setTimeout(timer, 1)
    }

    setTimeout(timer, 1)

}, false)