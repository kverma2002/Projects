package com.uscmarketplace.springbootfirebase.controller;

import java.util.List;
import java.util.concurrent.ExecutionException;

import javax.annotation.Nonnull;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.uscmarketplace.springbootfirebase.entity.Listing;
import com.uscmarketplace.springbootfirebase.service.ListingService;


@RestController

public class ListingController {

    public ListingService listingService;

    public ListingController(@Nonnull ListingService lService) {
        this.listingService = lService;
    }

    @PostMapping("/listing/create")
    public String createListing(@RequestBody @Nonnull Listing listing) throws InterruptedException, ExecutionException {
        return listingService.createListing(listing);
    }

    @GetMapping("/listing/get")
    public Listing getListing(@RequestParam @Nonnull String listingId) throws InterruptedException, ExecutionException {
        return listingService.getListing(listingId);

    }

    @PutMapping("/listing/delete")
    public String deleteListing(@RequestParam @Nonnull String listingId) throws InterruptedException, ExecutionException {
        return listingService.deleteListing(listingId);
    }

    @GetMapping("/listing/all") 
    public List<Listing> getAllListings() throws InterruptedException, ExecutionException {
        return listingService.getAllListings();
    }

    //@GetMapping("/listing/{}")
    
    
    @GetMapping("/listing/test")
    public ResponseEntity<String> testGetEndpoint() { return ResponseEntity.ok("Test Enpoint Works"); }
}
