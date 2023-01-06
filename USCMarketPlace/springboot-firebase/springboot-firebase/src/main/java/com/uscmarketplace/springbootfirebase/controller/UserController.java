package com.uscmarketplace.springbootfirebase.controller;
import com.uscmarketplace.springbootfirebase.entity.User;
import com.uscmarketplace.springbootfirebase.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.concurrent.ExecutionException;

@RestController
@RequestMapping("/api")
public class UserController {
    @Autowired
    private UserService userService;

    @PostMapping("/user/create")
    public String saveUser(@RequestBody User user) throws ExecutionException, InterruptedException {
        return userService.saveUser(user);
    }
    @GetMapping("/user/get")
    public User getUser(@RequestParam String userDocId) throws ExecutionException, InterruptedException {
        return userService.getUser(userDocId);
    }
    @GetMapping("/user/delete")
    public String deleteUser(@RequestParam String documentName) throws ExecutionException, InterruptedException {
        return userService.deleteUser(documentName);
    }
}
