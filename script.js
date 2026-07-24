// Data structures matching your Python script
const utilizador = {
    username: "",
    password: "",
    tentativas: 0,
    bloqueada: false
};

const historico_logins = [];

// DOM Elements
const registerSection = document.getElementById("register-section");
const loginSection = document.getElementById("login-section");
const messageBox = document.getElementById("message");

// Function: Register User
function registarUtilizador() {
    const userIn = document.getElementById("reg-username").value.trim();
    const passIn = document.getElementById("reg-password").value.trim();

    if (!userIn || !passIn) {
        showMessage("Por favor, preencha todos os campos do registo.", "error");
        return;
    }

    utilizador.username = userIn;
    utilizador.password = passIn;
    utilizador.tentativas = 0;
    utilizador.bloqueada = false;

    showMessage("Registo efetuado com sucesso! Agora pode fazer login.", "success");

    // Hide register form and show login form
    registerSection.style.display = "none";
    loginSection.style.display = "block";
}

// Function: Perform Login
function efetuarLogin() {
    if (utilizador.bloqueada) {
        showMessage("A sua conta está bloqueada devido a 2 tentativas incorretas consecutivas.", "error");
        return;
    }

    const userIn = document.getElementById("login-username").value.trim();
    const passIn = document.getElementById("login-password").value.trim();

    if (userIn === utilizador.username && passIn === utilizador.password) {
        utilizador.tentativas = 0; // Reset on success
        historico_logins.push("Sucesso");
        showMessage("Bem-vindo de volta! Login efetuado com sucesso.", "success");
    } else {
        utilizador.tentativas += 1;
        historico_logins.push("Insucesso");

        const tentativasRestantes = 2 - utilizador.tentativas;

        if (utilizador.tentativas >= 2) {
            utilizador.bloqueada = true;
            showMessage("Atingiu o limite de 2 erros consecutivos. A sua conta foi bloqueada!", "error");
        } else {
            showMessage(`Dados inválidos. Resta-lhe ${tentativasRestantes} tentativa(s).`, "error");
        }
    }
}

// Function: Helper to display messages on screen
function showMessage(msg, type) {
    messageBox.textContent = msg;
    messageBox.className = type;
}
