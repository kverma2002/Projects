package com.uscmarketplace.springbootfirebase.service;
import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.DocumentSnapshot;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import com.uscmarketplace.springbootfirebase.entity.User;
import org.springframework.stereotype.Service;

import java.util.concurrent.ExecutionException;

@Service
public class UserService {
    private static final String collection_name = "User";
    public String saveUser(User user) throws ExecutionException, InterruptedException {
        Firestore db = FirestoreClient.getFirestore();
        ApiFuture<WriteResult> userApiFuture = db.collection(collection_name).document(user.getEmail_address()).set(user);
        return userApiFuture.get().getUpdateTime().toString();

    }

    public User getUser(String documentName) throws ExecutionException, InterruptedException {
        Firestore db = FirestoreClient.getFirestore();
        DocumentReference df = db.collection(collection_name).document(documentName);
        ApiFuture<DocumentSnapshot> userFuture = df.get();
        DocumentSnapshot documentSnapshot = userFuture.get();
        return documentSnapshot.exists() ? documentSnapshot.toObject(User.class) : null;
    }

    public String updateUser(User user) throws ExecutionException, InterruptedException {
        return "";
    }

    public String deleteUser(String documentName) {
        Firestore db = FirestoreClient.getFirestore();
        ApiFuture<WriteResult> userApiFuture = db.collection(collection_name).document(documentName).delete();
        return "Deleted " + documentName;
    }
}
