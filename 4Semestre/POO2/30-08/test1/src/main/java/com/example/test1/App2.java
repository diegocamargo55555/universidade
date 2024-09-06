package com.example.test1;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.VBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.Region;
public class App2 extends Application {
    private Button btn1;
    private Button btn2;
    private Button btn3;
    private Button btn4;
    private Button btn5;

    public static void main(String[] args) {
        launch(args);
    }
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("VBox define os nós horizontalmente");
        // Cria um painel
        VBox vbox = new VBox();
        HBox hbox = new HBox();

        // define espa�amento de 10 pixels entre um n� e o outro no vbox
        vbox.setSpacing(10);
        btn1 = new Button("1º Botão");
        btn4 = new Button("4º Botão");
        btn5 = new Button("5 Botão");
        // Criar um espa�ador entre um n� e outro


        hbox.setSpacing(10);
        btn2 = new Button("2º Botão");
        btn3 = new Button("3º Botão");


        Region spacer = new Region();
        // Adiciona os n�s ao painel vbox
        // Inclui um n� espa�ador entre os dois primeiros bot�es e o terceiro
        vbox.getChildren().addAll(btn1, spacer, btn4, spacer, btn5);
        hbox.getChildren().addAll(btn2, spacer, btn3);
        // define espa�amento em torno de vbox de 10 pixels
        //vbox.setPadding(new Insets(10));
        // Configura spacer para se ajustar automaticamente na tela
        VBox.setVgrow(spacer, Priority.ALWAYS);
        vbox.setAlignment(Pos.CENTER);

        HBox.setHgrow(spacer, Priority.ALWAYS);
        //hbox.setAlignment(Pos.CENTER);


        // Cria uma scene
        Scene scene = new Scene(vbox, 600, 400);
        Scene scene2 = new Scene(hbox, 600, 400);
        // Adiciona uma scene ao stage
        primaryStage.setScene(scene);
        primaryStage.setScene(scene2);

        // Exibe o stage
        primaryStage.show();
    }
}