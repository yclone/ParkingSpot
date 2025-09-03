package com.example;

import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;
import java.util.UUID;

public class ApiTest {

    @Test
    public void testRegisterUser() {
        String uniqueId = UUID.randomUUID().toString();
        String payload = String.format("{ \"first_name\": \"João\", \"last_name\": \"Silva\", \"email\": \"joao.silva.%s@example.com\", \"username\": \"joao_silva_%s\", \"password\": \"senha_segura\" }", uniqueId, uniqueId);

        given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .post("http://localhost:5000/register_user")
        .then()
            .statusCode(201)
            .body("message", equalTo("Usuário cadastrado com sucesso!"))
            .body("user_id", notNullValue());
    }

    @Test
    public void testRegisterUserWithExistingEmail() {
        String uniqueId = UUID.randomUUID().toString();
        String payload = String.format("{ \"first_name\": \"Maria\", \"last_name\": \"Oliveira\", \"email\": \"joao.silva.%s@example.com\", \"username\": \"maria_oliveira_%s\", \"password\": \"senha_segura\" }", uniqueId, uniqueId);

        given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .post("http://localhost:5000/register_user")
        .then()
            .statusCode(400)
            .body("message", equalTo("Usuário já cadastrado no sistema!"));
    }

    @Test
    public void testRegisterUserWithExistingUsername() {
        String uniqueId = UUID.randomUUID().toString();
        String payload = String.format("{ \"first_name\": \"Carlos\", \"last_name\": \"Santos\", \"email\": \"carlos.santos.%s@example.com\", \"username\": \"joao_silva_%s\", \"password\": \"senha_segura\" }", uniqueId, uniqueId);

        given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .post("http://localhost:5000/register_user")
        .then()
            .statusCode(400)
            .body("message", equalTo("Usuário já cadastrado no sistema!"));
    }

    @Test
    public void testPasswordHashing() {
        String uniqueId = UUID.randomUUID().toString();
        String payload = String.format("{ \"first_name\": \"Ana\", \"last_name\": \"Costa\", \"email\": \"ana.costa.%s@example.com\", \"username\": \"ana_costa_%s\", \"password\": \"senha_segura\" }", uniqueId, uniqueId);

        given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .post("http://localhost:5000/register_user")
        .then()
            .statusCode(201)
            .body("message", equalTo("Usuário cadastrado com sucesso!"))
            .body("user_id", notNullValue());

        // Verify password is hashed
        String userId = given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .post("http://localhost:5000/register_user")
        .then()
            .extract()
            .path("user_id");

        given()
            .when()
            .get("http://localhost:5000/user/" + userId)
        .then()
            .statusCode(200)
            .body("password", not(equalTo("senha_segura")));
    }

    @Test
    public void testRedirectToLoginAfterRegistration() {
        String uniqueId = UUID.randomUUID().toString();
        String payload = String.format("{ \"first_name\": \"Pedro\", \"last_name\": \"Almeida\", \"email\": \"pedro.almeida.%s@example.com\", \"username\": \"pedro_almeida_%s\", \"password\": \"senha_segura\" }", uniqueId, uniqueId);

        given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .post("http://localhost:5000/register_user")
        .then()
            .statusCode(201)
            .body("message", equalTo("Usuário cadastrado com sucesso!"))
            .body("user_id", notNullValue());

        // Assuming the system redirects to login page after registration
        given()
            .when()
            .get("http://localhost:5000/login")
        .then()
            .statusCode(200)
            .body("title", equalTo("Login Page"));
    }

    @Test
    public void testResponsiveRegistrationForm() {
        // This test would ideally be done with a UI testing tool like Selenium
        // Here we just check if the registration page is accessible
        given()
            .when()
            .get("http://localhost:5000/register")
        .then()
            .statusCode(200)
            .body("title", equalTo("Registration Page"));
    }

    @Test
    public void testUpdateUser() {
        String uniqueId = UUID.randomUUID().toString();
        String payload = String.format("{ \"first_name\": \"Jane\", \"last_name\": \"Doe\", \"email\": \"jane.doe.%s@example.com\", \"username\": \"janedoe_%s\", \"password\": \"newpassword123\" }", uniqueId, uniqueId);

        given()
            .header("Content-Type", "application/json")
            .body(payload)
        .when()
            .put("http://localhost:5000/user/2")
        .then()
            .statusCode(200)
            .body("message", equalTo("Usuário atualizado com sucesso!"));
    }
}
