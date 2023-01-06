package com.uscmarketplace.springbootfirebase;

import com.uscmarketplace.springbootfirebase.firebase.FirebaseInitialization;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;


@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class })
public class SpringbootFirebaseApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringbootFirebaseApplication.class, args);
	}

}
