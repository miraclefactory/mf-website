
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

function toggle() {
    let project = document.getElementById("project-toggle").checked;
    if (project) {
        document.getElementById("projects").style.display = "block";
        document.getElementById("teams").style.display = "none";
    }
    else {
        document.getElementById("projects").style.display = "none";
        document.getElementById("teams").style.display = "block";
    }
}

function showSaveButton() {
    document.getElementById("form-button").style.display = "block";
}

function closeMessage() {
    document.getElementById("message-box").style.display = "none";
}
