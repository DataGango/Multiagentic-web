package com.example.webapp;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.ResponseEntity;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
class ApplicationTests {

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    void contextLoads() {
    }

    @Test
    void greetingEndpointReturnsMessage() {
        ResponseEntity<String> response = restTemplate.getForEntity("/api/greeting", String.class);
        assertThat(response.getBody()).contains("Hello from the Java Web Agent Backend!");
        assertThat(response.getStatusCodeValue()).isEqualTo(200);
    }
}
