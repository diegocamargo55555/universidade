package com.example.demo;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;


public class HelloController {
    @FXML
    private TextField tfdUsuario;
    @FXML
    private PasswordField pfdSenha;
    @FXML
    private void btnAcessarOnAction(ActionEvent event) {
        String nomeUsuario = tfdUsuario.getText().trim();
        String senha = pfdSenha.getText();
        if (nomeUsuario.isEmpty()) {
            showAlertMessage(Alert.AlertType.ERROR, "Usuario necessário!", "Por favor digite o seu nome");
            return;
        }
        if (senha.isEmpty()) {
            showAlertMessage(Alert.AlertType.ERROR, "Senha necessária!", "Por favor digite a sua senha");
            return;
        }
        showAlertMessage(Alert.AlertType.INFORMATION, "Detalhes enviados para o Banco de Dados!", "Nome de usuário e senha enviados para serem validados no Banco de Dados");
    }
    public static void showAlertMessage(Alert.AlertType alertType, String title,
                                        String message) {
        Alert alert = new Alert(alertType);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.show();
    }
}