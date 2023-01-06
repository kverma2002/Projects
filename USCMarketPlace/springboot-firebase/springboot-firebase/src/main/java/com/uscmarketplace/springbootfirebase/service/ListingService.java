package com.uscmarketplace.springbootfirebase.service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;

import javax.annotation.Nonnull;

import org.springframework.stereotype.Service;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.CollectionReference;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.DocumentSnapshot;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.cloud.firestore.QuerySnapshot;
import com.google.cloud.firestore.WriteResult;
//import com.google.cloud.firestore.v1.FirestoreClient;
import com.uscmarketplace.springbootfirebase.entity.Listing;
import com.google.firebase.cloud.FirestoreClient;
import com.google.firebase.internal.NonNull;
import com.google.firestore.v1.Document;


@Service
public class ListingService {

    public String createListing(@Nonnull Listing listing) throws ExecutionException, InterruptedException{
        Firestore dbFirestore = FirestoreClient.getFirestore();
        ApiFuture<WriteResult> collectionsApiFuture = dbFirestore.collection("Listings").document(listing.getID()+"").set(listing);
        return collectionsApiFuture.get().getUpdateTime().toString();
    }

    public Listing getListing(@Nonnull String listingId) throws ExecutionException, InterruptedException{
        Firestore dbFirestore = FirestoreClient.getFirestore();
        DocumentReference docReference = dbFirestore.collection("Listings").document(listingId);
        ApiFuture<DocumentSnapshot> future = docReference.get();
        DocumentSnapshot document = future.get();
        Listing listing;
        if(document.exists()) {
            listing = document.toObject(Listing.class);
            return listing;
        }
        return null;

    }

    public String deleteListing(@Nonnull String listingId) throws ExecutionException, InterruptedException{
        Firestore dbFirestore = FirestoreClient.getFirestore();
        ApiFuture<WriteResult> writeResult = dbFirestore.collection("Listings").document(listingId).delete();
        return "Succesfully deleted";
    }

    public List<Listing> getAllListings() throws ExecutionException, InterruptedException {
        /* 
        Firestore dbFirestore = FirestoreClient.getFirestore();
        CollectionReference colRef = collection(dbFirestore, "Listings");
        DocumentSnapshot docsSnap = await getDocs(colRef);
        */
        Firestore dbFirestore = FirestoreClient.getFirestore();
        ApiFuture<QuerySnapshot> future = dbFirestore.collection("Listings").get();
       
        List<QueryDocumentSnapshot> documents = future.get().getDocuments();
        List<Listing> res = new ArrayList<Listing>();
        for (QueryDocumentSnapshot document : documents) {
            res.add(document.toObject(Listing.class));
        }
        return res;


    }
    
}
