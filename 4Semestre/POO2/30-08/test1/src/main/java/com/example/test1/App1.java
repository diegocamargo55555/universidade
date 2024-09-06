package com.example.test1;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.Region;
public class App1 extends Application {
    private Button btn1;
    private Button btn2;
    private Button btn3;
    public static void main(String[] args) {
        launch(args);
    }
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("VBox define os nós horizontalmente");
        // Cria um painel
        VBox hbox = new VBox();
        // define espa�amento de 10 pixels entre um n� e o outro no hbox
        hbox.setSpacing(10);
        btn1 = new Button("1º Botão");
        btn2 = new Button("2º Botão");
        btn3 = new Button("3º Botão");
        // Criar um espa�ador entre um n� e outro
        Region spacer = new Region();
        // Adiciona os n�s ao painel hbox
        // Inclui um n� espa�ador entre os dois primeiros bot�es e o terceiro
        hbox.getChildren().addAll(btn1, btn2, spacer, btn3);
        // define espa�amento em torno de hbox de 10 pixels
        hbox.setPadding(new Insets(10));
        // Configura spacer para se ajustar automaticamente na tela
        VBox.setVgrow(spacer, Priority.ALWAYS);
        hbox.setAlignment(Pos.CENTER);

        // Cria uma scene
        Scene scene = new Scene(hbox, 300, 200);
        // Adiciona uma scene ao stage
        primaryStage.setScene(scene);
        // Exibe o stage
        primaryStage.show();
    }
}