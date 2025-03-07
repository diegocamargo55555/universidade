package projeto1.appmitologia.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import projeto1.appmitologia.dao.UserDAO;
import projeto1.appmitologia.model.User;

import java.sql.SQLException;

public class CadastroUserController {

    @FXML
    private Button bCadastro;

    @FXML
    private TextField nome, img;

    @FXML
    private PasswordField pass;



    @FXML
    private void bCadastroOnAction(ActionEvent event) {
        User user = new User();
        user.setUserName(nome.getText());
        user.setPassword(pass.getText());

        Alert alert = new Alert(Alert.AlertType.CONFIRMATION, "Deseja inserir o Usuario?", ButtonType.CANCEL, ButtonType.OK);
        alert.setTitle("Usuario pode ser cadastrado!");
        alert.setHeaderText("Informação");

        alert.showAndWait().ifPresent(response -> {
            if (response == ButtonType.OK) {
                UserDAO userDAO = new UserDAO();
                try {
                    userDAO.insere(user);
                    Alert successAlert = new Alert(Alert.AlertType.INFORMATION, "usuario cadastrado com sucesso!", ButtonType.OK);
                    successAlert.setTitle("Sucesso");
                    successAlert.setHeaderText("Informação");
                    successAlert.show();
                } catch (SQLException e1) {
                    Alert errorAlert = new Alert(Alert.AlertType.ERROR, "Erro ao cadastrar!", ButtonType.OK);
                    errorAlert.setTitle("Erro");
                    errorAlert.setHeaderText("Informação");
                    errorAlert.show();
                    e1.printStackTrace();
                }
            } else {
                Alert cancelAlert = new Alert(Alert.AlertType.INFORMATION, "Cadastro de usuario cancelado.", ButtonType.OK);
                cancelAlert.setTitle("Cancelado");
                cancelAlert.setHeaderText("Informação");
                cancelAlert.show();
            }
        });
    }
}
