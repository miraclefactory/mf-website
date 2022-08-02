
var clientH = window.innerHeight || document.documentElement.clientHeight
var clientW = window.innerWidth || document.documentElement.clientWidth;

let form_join = "<form action='/join' method='post'><div class='form-group'><label for='name'>What should we call you?</label><input type='text' name='name' id='dialog-join-name' class='form-control' placeholder='Your name' required maxlength='50'></div><div class='form-group'><label for='email'>Give us an email to stay in touch</label><input type='email' name='email' id='dialog-join-email' class='form-control' placeholder='Your email' required maxlength='50'></div><div class='form-group hide'><input name='email2' type='text' maxlength='50' /></div><div class='form-group'><label for='message'>Tell us more about you</label><textarea name='message' id='dialog-join-message' class='form-control' placeholder='Your message' required maxlength='1000'></textarea></div><div class='form-group'><input type='submit' name='submit' id='dialog-join-submit' class='btn btn-primary' value='Send'></div></form>";
let form_contact = "<form action='/contact' method='post'><div class='form-group'><label for='name'>What should we call you?</label><input type='text' name='name' id='dialog-contact-name' class='form-control' placeholder='Your name' required maxlength='50'></div><div class='form-group'><label for='email'>Give us an email to stay in touch</label><input type='email' name='email' id='dialog-contact-email' class='form-control' placeholder='Your email' required maxlength='50'></div><div class='form-group hide'><input name='email2' type='text' maxlength='50' /></div><div class='form-group'><label for='message'>What do you what to talk about?</label><textarea name='message' id='dialog-contact-message' class='form-control' autocomplete='off' placeholder='Your message' required maxlength='1000'></textarea></div><div class='form-group'><input type='submit' name='submit' id='dialog-contact-submit' class='btn btn-primary' value='Send'></div></form>";

window.onscroll = function()
{
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    let children = document.getElementById("intro-wrapper").children;
    if(scrollTop > 0)
    {
        // document.getElementById("header").style.transform = "translateY(" +  (-(scrollTop/2)) + "px)";
        if (scrollTop > clientH / 2)
        {
            for(let i = 1; i < children.length; i++)
            {
                children[i].style.opacity = 1;
                children[i].style.transform = "translateY(0)";
            }
            // document.getElementById("type").style.webkitAnimationPlayState = "running";
        }
        else
        {
            for(let i = 1; i < children.length; i++)
            {
                children[i].style.opacity = 0;
                children[i].style.transform = "translateY(100px)";
            }
        }
    }
}

window.onload = function()
{
    // dynamically allocate the forms when html is loaded
    // anti-spam protection: honeypot and dynamic html content
    document.getElementById("join-form").innerHTML = form_join;
    document.getElementById("contact-form").innerHTML = form_contact;
}


function showDialogJoin()
{
    document.getElementById("dialog-join").style.display = "block";
    document.getElementById("dialog-join-bk").style.display = "block";
    document.body.style.overflowY = "hidden";
    document.getElementById("dialog-join-name").focus();
}

function showDialogContact()
{
    document.getElementById("dialog-contact").style.display = "block";
    document.getElementById("dialog-contact-bk").style.display = "block";
    document.body.style.overflowY = "hidden";
    document.getElementById("dialog-contact-name").focus();
}

function closeDialog()
{
    document.getElementById("dialog-join").style.display = "none";
    document.getElementById("dialog-join-bk").style.display = "none";
    document.getElementById("dialog-contact").style.display = "none";
    document.getElementById("dialog-contact-bk").style.display = "none";
    document.body.style.overflowY = "auto";
}

function closeBookmark()
{
    document.getElementById("bookmark").style.opacity = 0;
    document.getElementById("bookmark").style.transform = "translateX(100%)";
}
