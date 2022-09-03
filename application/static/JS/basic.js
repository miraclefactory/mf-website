
var clientH = window.innerHeight || document.documentElement.clientHeight
var clientW = window.innerWidth || document.documentElement.clientWidth;

let form_join = "<form action='/join' method='post'><div class='form-group'><label for='name'>What should we call you?</label><input type='text' name='name' id='dialog-join-name' class='form-control' placeholder='Your name' required maxlength='50'></div><div class='form-group'><label for='email'>Give us an email to stay in touch</label><input type='email' name='email' id='dialog-join-email' class='form-control' placeholder='Your email' required maxlength='50'></div><div class='form-group hide'><input name='email2' type='text' maxlength='50' /></div><div class='form-group'><label for='message'>Tell us more about you</label><textarea name='message' id='dialog-join-message' class='form-control' placeholder='Briefly introduce yourself :)' required maxlength='1000'></textarea></div><div class='form-group'><input type='submit' name='submit' id='dialog-join-submit' class='btn btn-primary' value='Send'></div></form>";
let form_contact = "<form action='/contact' method='post'><div class='form-group'><label for='name'>What should we call you?</label><input type='text' name='name' id='dialog-contact-name' class='form-control' placeholder='Your name' required maxlength='50'></div><div class='form-group'><label for='email'>Give us an email to stay in touch</label><input type='email' name='email' id='dialog-contact-email' class='form-control' placeholder='Your email' required maxlength='50'></div><div class='form-group hide'><input name='email2' type='text' maxlength='50' /></div><div class='form-group'><label for='message'>What do you wish to discuss?</label><textarea name='message' id='dialog-contact-message' class='form-control' autocomplete='off' placeholder='Your thoughts' required maxlength='1000'></textarea></div><div class='form-group'><input type='submit' name='submit' id='dialog-contact-submit' class='btn btn-primary' value='Send'></div></form>";

// window.onscroll = function()
// {
//     var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
//     let children = document.getElementById("intro-wrapper").children;
//     // document.getElementById("header").style.transform = "translateY(" +  (-(scrollTop/2)) + "px)";
//     if (scrollTop > clientH / 2)
//     {
//         for(let i = 1; i < children.length; i++)
//         {
//             children[i].style.opacity = 1;
//             children[i].style.transform = "translateY(0)";
//         }
//         document.getElementById("down").style.transform = "rotate(180deg)";
//         // document.getElementById("type").style.webkitAnimationPlayState = "running";
//         if(scrollTop > clientH)
//         {
//             document.getElementById("nav-wrapper").style.backgroundColor = "inherit";
//             // document.getElementById("nav-links").style.mixBlendMode = "difference";
//             if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
//                 document.getElementById("nav-links").style.color = "#333";
//             }
//             document.getElementById("nav-wrapper").style.boxShadow = "0px 0px 14px rgba(0, 0, 0, 0.3)";
//         }
//         else
//         {
//             document.getElementById("nav-wrapper").style.backgroundColor = "transparent";
//             // document.getElementById("nav-links").style.mixBlendMode = "normal";
//             document.getElementById("nav-links").style.color = "white";
//             document.getElementById("nav-wrapper").style.boxShadow = "none";
//         }
//     }
//     else
//     {
//         for(let i = 1; i < children.length; i++)
//         {
//             children[i].style.opacity = 0;
//             children[i].style.transform = "translateY(25px)";
//         }
//         document.getElementById("down").style.transform = "rotate(0deg)";
//     }
// }

addEventListener("scroll", function() {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    let children = document.getElementById("intro-wrapper").children;
    let navStyle = document.querySelector("#nav-wrapper").style;
    if (scrollTop > clientH / 2)
    {
        for(let i = 1; i < children.length; i++)
        {
            children[i].style.opacity = 1;
            children[i].style.transform = "translateY(0)";
        }
        document.getElementById("down").style.transform = "rotate(180deg)";
        if(scrollTop > clientH)
        {
            navStyle.backgroundColor = "inherit";
            navStyle.color = "rgb(132, 78, 235)";
            navStyle.boxShadow = "0px 0px 14px rgba(0, 0, 0, 0.3)";
            navStyle.borderBottom = "0.5px solid rgba(0, 0, 0, 0.3)";
        }
        else
        {
            navStyle.backgroundColor = "transparent";
            navStyle.color = "white";
            navStyle.boxShadow = "none";
            navStyle.borderBottom = "0.5px solid rgba(0, 0, 0, 0)";
        }
    }
    else
    {
        for(let i = 1; i < children.length; i++)
        {
            children[i].style.opacity = 0;
            children[i].style.transform = "translateY(25px)";
        }
        document.getElementById("down").style.transform = "rotate(0deg)";
    }
})

window.onload = function()
{
    // dynamically allocate the forms when html is loaded
    // anti-spam protection: honeypot and dynamic html content
    document.getElementById("join-form").innerHTML = form_join;
    document.getElementById("contact-form").innerHTML = form_contact;
    document.getElementById("img-github").alt = "Github-Homepage-img";
    document.getElementById("img-project").alt = "Project-Submarine-img";
}

function showDialog(obj)
{
    document.getElementById("dialog-bk").style.display = "block";
    document.body.style.overflowY = "hidden";
    let desktopEmail = document.getElementById("desktop-email");
    let mobileEmail = document.getElementById("mobile-email"); 
    let email = document.getElementById("dialog-join-email");
    email.value = desktopEmail.value || mobileEmail.value;
    desktopEmail.value = "";
    mobileEmail.value = "";
    if(obj.innerHTML == "Join Us")
    {
        document.getElementById("dialog-join").style.display = "block";
        document.getElementById("dialog-join-name").focus();
    }
    else
    {
        document.getElementById("dialog-contact").style.display = "block";
        document.getElementById("dialog-contact-name").focus();
    }
}

function closeDialog()
{
    document.getElementById("dialog-join").style.display = "none";
    document.getElementById("dialog-bk").style.display = "none";
    document.getElementById("dialog-contact").style.display = "none";
    document.body.style.overflowY = "auto";
}

function closeBookmark()
{
    let bookmark = document.querySelector("#bookmark").style;
    bookmark.opacity = 0;
    bookmark.transform = "translateX(100%)";
}

function showMobileNav()
{
    let mobileNav = document.querySelector("#mobile-nav").style;
    mobileNav.display = "block";
    document.body.style.overflowY = "hidden";
}

function closeMobileNav()
{
    let mobileNav = document.querySelector("#mobile-nav").style;
    mobileNav.display = "none";
    document.body.style.overflowY = "auto";
}
