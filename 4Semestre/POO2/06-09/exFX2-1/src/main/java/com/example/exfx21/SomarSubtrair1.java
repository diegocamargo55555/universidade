package com.example.exfx21;

import javafx.application.*;
import javafx.stage.*;
import javafx.scene.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.Insets;

public class SomarSubtrair1 extends Application {
    private Button btnOla;
    private Button btnSair;
    private Label smg;
    private Label olaSmg;



    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) {

        btnOla = new Button();
        btnOla.setText("olá");
        btnSair = new Button();
        btnSair.setText("sair");
        smg = new Label();
        smg.setText("digite seu nome");
        olaSmg = new Label();
        olaSmg.setText("ola " );
        TextField textField = new TextField ();
        olaSmg.setStyle("-fx-text-fill: blue;");

        btnOla.setOnAction(e -> {
            String nome = new String();
            nome = "ola " +textField.getText();

            olaSmg.setText(nome);
        });

        btnSair.setOnAction(e -> {
                stage.close();
        });

        VBox vBox = new VBox(10);
        vBox.getChildren().addAll(smg, textField , olaSmg, btnOla,btnSair);

        vBox.setPadding(new Insets(10)); // define espa�amento de 10 pixels em torno de hbox
        Scene scene = new Scene(vBox, 600, 300); // Adiciona o painel � scene
        stage.setScene(scene); // Adiciona a scene ao stage
        stage.setTitle("input nome");// configura o t�tulo
        stage.show(); // exibe o stage
    }
}
