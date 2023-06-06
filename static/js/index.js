var clientH = window.innerHeight || document.documentElement.clientHeight
var clientW = window.innerWidth || document.documentElement.clientWidth;

// addEventListener("scroll", function() {
//     var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
//     let children = document.getElementById("intro-wrapper").children;
//     // let navStyle = document.querySelector("#nav-wrapper").style;
//     if (scrollTop > clientH / 2)
//     {
//         for(let i = 1; i < children.length; i++)
//         {
//             children[i].style.opacity = 1;
//             children[i].style.transform = "translateY(0)";
//         }
//         // if(scrollTop > clientH)
//         // {
//         //     navStyle.backgroundColor = "rgba(0, 0, 0, 0.8)";
//         //     navStyle.backdropFilter = "blur(20px)";
//         //     navStyle.webkitBackdropFilter = "blur(20px)";
//         //     navStyle.borderBottom = "0.5px solid rgba(0, 0, 0, 0.3)";
//         // }
//         // else
//         // {
//         //     navStyle.backgroundColor = "transparent";
//         //     navStyle.backdropFilter = "blur(0px)";
//         //     navStyle.webkitBackdropFilter = "blur(0px)";
//         //     navStyle.borderBottom = "0.5px solid rgba(0, 0, 0, 0)";
//         // }
//     }
//     else
//     {
//         for(let i = 1; i < children.length; i++)
//         {
//             children[i].style.opacity = 0;
//             children[i].style.transform = "translateY(25px)";
//         }
//     }
// })

window.onload = function()
{
    // assign the alt attribute to the images
    document.getElementById("img-github").alt = "Github-Homepage-img";
    document.getElementById("img-project").alt = "Project-Submarine-img";
}

function showDialog(obj)
{
    document.getElementById("dialog-bk").style.display = "block";
    document.body.style.overflowY = "hidden";
    let desktopEmail = document.getElementById("desktop-search");
    let mobileEmail = document.getElementById("mobile-search"); 
    let email = document.getElementById("dialog_join_email");
    email.value = desktopEmail.value || mobileEmail.value;
    desktopEmail.value = "";
    mobileEmail.value = "";
    if(obj.innerHTML == "Join Us")
    {
        document.getElementById("dialog-join").style.display = "block";
        document.getElementById("dialog_join_name").focus();
    }
    else
    {
        document.getElementById("dialog-contact").style.display = "block";
        document.getElementById("dialog_join_name").focus();
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

