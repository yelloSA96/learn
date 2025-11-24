package me.thomassuebwicha.event;

import me.thomassuebwicha.event.publisher.CustomSpringEventPublisher;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class EventBasedApplication {

    private static CustomSpringEventPublisher customSpringEventPublisher;

    @Autowired
    public EventBasedApplication(CustomSpringEventPublisher customSpringEventPublisher) {
        this.customSpringEventPublisher = customSpringEventPublisher;
    }

	public static void main(String[] args) throws InterruptedException {
		SpringApplication.run(EventBasedApplication.class, args);

        while(true) {
            Thread.sleep(1000);
            customSpringEventPublisher.publishCustomEvent("Hello World Spring Custom Event Publisher");
        }
	}

}
