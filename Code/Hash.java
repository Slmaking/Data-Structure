public class User {

    private long id;
    private String name;
    private String email;

    // standard getters/setters/constructors
        
    @Override
    public int hashCode() {
        return  1;
    }
        
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null) return false;
        if (this.getClass() != o.getClass()) return false;
        User user = (User) o;
        return id == user.id  
          && (name.equals(user.name)  
          && email.equals(user.email));
    }
    
    // getters and setters here
}

$$Double

public final class Double
{
private final double value;
...
public int hashCode()
{
long bits = doubleToLongBits(value);
return (int) (bits ^ (bits >>> 32));
}
}
