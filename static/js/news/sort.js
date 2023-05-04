// window.onload = function () {
//     const posts = document.getElementsByClassName('news_post')
//
//     const sort_button = document.getElementById('sort_button')
//     const sort_select = document.getElementById('sort_select')
//
//     const null_posts = document.getElementById('null_posts')
//
//     console.log(posts)
//
//     sort_button.onclick = function () {
//         let sort_value = sort_select.value
//
//         let news_counter = 0
//
//         for (let i = 0; i < posts.length; i++) {
//             let post = posts[i]
//             let title = post.getElementsByTagName('h1')[0]
//
//             let h1_text = title.textContent.toLowerCase()
//
//             null_posts.style.display = 'none'
//
//             if (sort_value == 1) {
//                 post.style.display = 'block'
//                 news_counter++
//             } else if (sort_value == 2) {
//                 if ((h1_text.includes('update')) || (h1_text.includes('updates'))) {
//                     news_counter++
//                     post.style.display = 'block'
//                 } else {
//                     post.style.display = 'none'
//                 }
//             } else if (sort_value == 3) {
//                 if ((h1_text.includes('product')) || (h1_text.includes('products'))) {
//                     news_counter++
//                     post.style.display = 'block'
//                 } else {
//                     post.style.display = 'none'
//                 }
//             } else if (sort_value == 4) {
//                 if ((h1_text.includes('server'))) {
//                     news_counter++
//                     post.style.display = 'block'
//                 } else {
//                     post.style.display = 'none'
//                 }
//             }
//         }
//
//         if (news_counter == 0) {
//             null_posts.style.display = 'block'
//         }
//     }
// }



window.addEventListener("load",function(event) {
    const posts = document.getElementsByClassName('news_post')

    const sort_button = document.getElementById('sort_button')
    const sort_select = document.getElementById('sort_select')

    const null_posts = document.getElementById('null_posts')

    console.log(posts)

    sort_button.onclick = function () {
        let sort_value = sort_select.value

        let news_counter = 0

        for (let i = 0; i < posts.length; i++) {
            let post = posts[i]
            let title = post.getElementsByTagName('h1')[0]

            let h1_text = title.textContent.toLowerCase()

            null_posts.style.display = 'none'

            if (sort_value == 1) {
                post.style.display = 'block'
                news_counter++
            } else if (sort_value == 2) {
                if ((h1_text.includes('update')) || (h1_text.includes('updates'))) {
                    news_counter++
                    post.style.display = 'block'
                } else {
                    post.style.display = 'none'
                }
            } else if (sort_value == 3) {
                if ((h1_text.includes('product')) || (h1_text.includes('products'))) {
                    news_counter++
                    post.style.display = 'block'
                } else {
                    post.style.display = 'none'
                }
            } else if (sort_value == 4) {
                if ((h1_text.includes('server'))) {
                    news_counter++
                    post.style.display = 'block'
                } else {
                    post.style.display = 'none'
                }
            }
        }

        if (news_counter == 0) {
            null_posts.style.display = 'block'
        }
    }
},false);