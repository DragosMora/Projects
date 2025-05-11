package org.example.lab6;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

public class SignupController {
    private Service service;

    public void setService(Service service) {
        this.service = service;
    }

    @FXML
    private Button backButtonScene2;

    @FXML
    public void switchToLoginScene() throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("hello-view.fxml"));
        Parent root = fxmlLoader.load();

        HelloController controller = fxmlLoader.getController();
        controller.setService(service);

        Stage stage = (Stage) backButtonScene2.getScene().getWindow();
        Scene scene = new Scene(root, 300, 300);
        stage.setTitle("Login");
        stage.setScene(scene);

    }

    @FXML
    private TextField signUpUserId, signUpName, signUpGender, signUpAge, signUpLocation, signUpPhone;

    @FXML
    private TextArea signUpDescription;

    @FXML
    public void signUpUser() throws Exception {
        int user_id = Integer.parseInt(signUpUserId.getText());
        String name = signUpName.getText();
        String gender = signUpGender.getText();
        int age = Integer.parseInt(signUpAge.getText());
        String location = signUpLocation.getText();
        String phone = signUpPhone.getText();
        String description = signUpDescription.getText();
        service.store(user_id, name, gender, age, location, description, phone);
    }
}
