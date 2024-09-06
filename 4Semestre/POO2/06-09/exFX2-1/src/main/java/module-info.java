module com.example.exfx21 {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires org.kordamp.bootstrapfx.core;

    opens com.example.exfx21 to javafx.fxml;
    exports com.example.exfx21;
}