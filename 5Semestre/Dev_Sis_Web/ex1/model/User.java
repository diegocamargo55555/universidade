package projeto1.appmitologia.model;

public class User {
    private String userName;
    private String password;
    private String heroiId;

    public User() {}

    public String getHeroiId() {
        return heroiId;
    }

    public void setHeroiId(String heroiId) {
        this.heroiId = heroiId;
    }

    public User(String userName, String password) {
        this.password = password;
        this.userName = userName;
    }
    public String getPassword() {
        return this.password;
    }
    public String getUserName() {
        return userName;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    public void setUserName(String userName) {
        this.userName = userName;
    }


}

