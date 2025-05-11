package org.example.lab6;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloController {
    private Service service;

    public void setService(Service service) {
        this.service = service;
    }

    @FXML
    private Button signUpButtonScene1;

    @FXML
    public void switchToSignupScene() throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("signup-view.fxml"));
        Parent root = fxmlLoader.load();

        SignupController controller = fxmlLoader.getController();
        controller.setService(service);

        Stage stage = (Stage) signUpButtonScene1.getScene().getWindow();
        Scene scene = new Scene(root, 700, 700);
        stage.setTitle("SignUp");
        stage.setScene(scene);
    }

    @FXML
    private TextField loginUserId;

    @FXML
    public void switchToMainScene() throws Exception {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("app-view.fxml"));
        Parent root = fxmlLoader.load();

        AppController controller = fxmlLoader.getController();
        controller.setService(service);

        Stage stage = (Stage) loginUserId.getScene().getWindow();
        Scene scene = new Scene(root, 600, 415);
        stage.setTitle("App");
        stage.setScene(scene);

        controller.setUser_id(Integer.parseInt(loginUserId.getText()));
        controller.initView();
    }
}