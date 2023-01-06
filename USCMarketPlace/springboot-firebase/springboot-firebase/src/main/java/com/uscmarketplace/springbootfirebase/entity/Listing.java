package com.uscmarketplace.springbootfirebase.entity;



public class Listing {

    private int id;
    private String title;
    private double price;
    private String description;
    private String category;
    private String imageUrl;
    private int owner_id;



    // public Listing(String title, double price, String description, String category, String imageUrl, int userId) {
    //     this.title = title;
    //     this.price = price;
    //     this.category = category;
    //     this.imageUrl = imageUrl;
    //     this.userId = userId;
    //     this.description = description;
    // }

    public int getID() {
		return this.id;
	}

	public void setID(int iD) {
        this.id = iD;
    }
	
    public String getDescription() {
		return this.description;
    }

    public void setDescription(String description) {
		this.description = description;
	}

    public int getowner_id() {
        return this.owner_id;
    }

    public void setOwner_id(int userId) {
        this.owner_id = userId;
    }



    public double getPrice() {
        return this.price;
    }
    public void setPrice(double price) {
        this.price = price;
    }
/* 
	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}
*/
	public String getTitle() {
		return this.title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getCategory() {
		return this.category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public String getImageUrl() {
		return this.imageUrl;
	}

	public void setImageUrl(String imageUrl) {
		this.imageUrl = imageUrl;
	}



	






}
